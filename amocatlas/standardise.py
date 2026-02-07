"""Standardisation functions for AMOC observing array datasets.

These functions take raw loaded datasets and:
- Rename variables to standard names
- Add variable-level metadata
- Add or update global attributes
- Prepare datasets for downstream analysis

Currently implemented:
- SAMBA
"""

import xarray as xr
from collections import OrderedDict
import re
import warnings
from datetime import datetime, timezone
from amocatlas import logger, utilities, defaults
from amocatlas.logger import log_debug

log = logger.log  # Use the global logger

# Extracted from OG1.0 spec “## Global attributes” (cf. turn1view0) :contentReference[oaicite:0]{index=0}
_GLOBAL_ATTR_ORDER = defaults.GLOBAL_ATTR_ORDER

_INSTITUTION_CORRECTIONS = defaults.INSTITUTION_CORRECTIONS


def reorder_metadata(attrs: dict) -> dict:
    """Return a new dict with keys ordered according to the OG1.0 global‐attribute list.
    Any attrs not in the spec list are appended at the end, in their original order.
    """
    # Shallow copy so we can pop
    remaining = dict(attrs)
    ordered = OrderedDict()

    for key in _GLOBAL_ATTR_ORDER:
        # Some attributes are case-sensitive and must match exactly
        if key in ["Conventions", "featureType", "featureType_vocabulary"]:
            if key in remaining:
                ordered[key] = remaining.pop(key)
        else:
            # look for any remaining key whose lower() matches
            to_remove = None
            for orig in remaining:
                if orig.lower() == key.lower():
                    to_remove = orig
                    break
            if to_remove is not None:
                ordered[to_remove] = remaining.pop(to_remove)

    # finally, append all the rest in their original insertion order
    for orig, val in remaining.items():
        ordered[orig] = val

    return dict(ordered)


def normalize_and_add_vocabulary(
    attrs: dict, normalizations: dict[str, tuple[dict[str, str], str]]
) -> dict:
    """For each (attr, (value_map, vocab_url)) in `normalizations`.

      - If `attr` exists in attrs:
          * Map attrs[attr] using value_map (or leave it if unmapped)
          * Add attrs[f"{attr}_vocabulary"] = vocab_url

    Parameters
    ----------
    attrs : dict
        Metadata attributes, already cleaned & renamed.
    normalizations : dict
        Keys are canonical attr names (e.g. "platform"), values are
        (value_map, vocabulary_url) tuples.

    Returns
    -------
    dict
        attrs with normalized values and added <attr>_vocabulary entries.

    """
    for attr, (value_map, vocab_url) in normalizations.items():
        if attr in attrs:
            raw = attrs[attr]
            mapped = value_map.get(raw, raw)
            if mapped != raw:
                log_debug("Normalized '%s': %r → %r", attr, raw, mapped)
            attrs[attr] = mapped

            vocab_key = f"{attr}_vocabulary"
            # only set if not already present
            if vocab_key not in attrs:
                attrs[vocab_key] = vocab_url
                log_debug("Added vocabulary for '%s': %s", attr, vocab_url)

    return attrs


def get_dynamic_version() -> str:
    """Get the actual software version using multiple detection methods.

    Priority:
    1. Git describe (for development in git repo)
    2. Installed package version (for pip/conda installs)
    3. Fallback to __version__ file

    Returns
    -------
    str
        Software version string

    """
    import subprocess
    import os

    # Method 1: Try git describe for development versions
    try:
        # Get the directory of this file to find git repo root
        current_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.dirname(current_dir)  # Go up from amocatlas/ to repo root

        result = subprocess.run(
            ["git", "describe", "--tags", "--dirty", "--always"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            git_version = result.stdout.strip()

            # Strip everything after vX.X.X pattern (remove commit info and dirty flag)
            import re

            version_match = re.match(r"(v?\d+\.\d+\.\d+)", git_version)
            if version_match:
                clean_version = version_match.group(1)
                log_debug(
                    f"Using cleaned git version: {clean_version} (from {git_version})"
                )
                return clean_version

            log_debug(f"Using git version: {git_version}")
            return git_version
    except (subprocess.SubprocessError, FileNotFoundError, OSError):
        pass

    # Method 2: Try installed package version
    try:
        import importlib.metadata

        installed_version = importlib.metadata.version("amocatlas")
        log_debug(f"Using installed package version: {installed_version}")
        return installed_version
    except (importlib.metadata.PackageNotFoundError, ImportError):
        pass

    # Method 3: Fallback to __version__ file
    from amocatlas._version import __version__

    log_debug(f"Using fallback version from __version__: {__version__}")
    return __version__


def clean_metadata(attrs: dict, preferred_keys: dict = None) -> dict:
    """Clean up a metadata dictionary.

    - Normalize key casing
    - Merge aliases with identical values
    - Apply standard naming (via preferred_keys mapping)
    """
    # Step 0: normalize whitespace everywhere
    attrs = utilities.normalize_whitespace(attrs)

    if preferred_keys is None:
        preferred_keys = defaults.METADATA_KEY_MAPPINGS

    # Step 1: merge any identical aliases first
    merged_attrs = merge_metadata_aliases(attrs, preferred_keys)

    # Step 2: normalize remaining cases and resolve conflicts
    cleaned = {}
    for key, value in merged_attrs.items():
        # key is already canonical if it was an alias
        if key in cleaned:
            if cleaned[key] == value:
                log_debug(f"Skipping identical '{key}'")
                continue
            if len(str(value)) > len(str(cleaned[key])):
                log_debug(
                    f"Replacing '{key}' value with longer one ("
                    f"{len(str(cleaned[key]))}→{len(str(value))} chars)"
                )
                cleaned[key] = value
            else:
                log_debug(f"Keeping existing '{key}', ignoring shorter from merge")
        else:
            cleaned[key] = value

    # Step 3: consolidate contributors and institutions
    cleaned = _consolidate_contributors(cleaned)
    return cleaned


def _consolidate_contributors(cleaned: dict) -> dict:
    """Consolidate creators, PIs, publishers, and contributors into unified fields.

    These include:
    - contributor_name, contributor_role, contributor_email, contributor_id aligned one-to-one
    - contributing_institutions, with placeholders for vocabularies/roles
    """
    log_debug("Starting _consolidate_contributors with attrs: %s", cleaned)

    role_map = defaults.CONTRIBUTOR_ROLE_MAP

    # Step A: extract email & URL buckets
    email_buckets = {}
    url_buckets = {}
    bucket_order = []
    for key in list(cleaned.keys()):
        if key.endswith("_email"):
            raw = cleaned.pop(key)
            parts = [
                v.strip() for v in str(raw).replace(";", ",").split(",") if v.strip()
            ]
            email_buckets[key] = parts
            bucket_order.append(("email", key))
        elif key.endswith("_url"):
            raw = cleaned.pop(key)
            parts = [
                v.strip() for v in str(raw).replace(";", ",").split(",") if v.strip()
            ]
            url_buckets[key] = parts
            bucket_order.append(("url", key))
    log_debug("Email buckets: %s", email_buckets)
    log_debug("URL buckets: %s", url_buckets)

    # Step B: extract names, roles, sources
    names, roles, sources = [], [], []
    for key in list(cleaned.keys()):
        if key in role_map:
            raw = cleaned.pop(key)
            parts = [
                v.strip() for v in str(raw).replace(";", ",").split(",") if v.strip()
            ]
            for p in parts:
                names.append(p)
                roles.append(role_map[key])
                sources.append(key)
    log_debug("Names: %s; Roles: %s; Sources: %s", names, roles, sources)

    # Step B2: deduplicate names and consolidate emails for the same person
    if names and email_buckets:
        # Collect all available emails from any email bucket
        all_emails = []
        for email_list in email_buckets.values():
            all_emails.extend(email_list)

        # Check if we have emails that might belong to specific people
        if all_emails and any(email.strip() for email in all_emails):
            # Look for duplicate names that might need deduplication
            name_counts = {}
            for name in names:
                name_counts[name] = name_counts.get(name, 0) + 1

            duplicates_found = any(count > 1 for count in name_counts.values())
            log_debug(
                "Name counts: %s, Duplicates found: %s", name_counts, duplicates_found
            )

            if duplicates_found:
                # We have duplicated names - try to consolidate with emails
                # Since emails could be in any field (publisher_email, contributor_email, etc.)
                # we'll try to match emails to the last occurrence of duplicated names

                # Create mapping: find emails for people with duplicate names
                name_to_emails = {}

                # Strategy: if "M. Susan Lozier" appears twice and we have
                # "susan.lozier@gatech.edu" in emails, assign it to M. Susan Lozier
                for name in names:
                    if name_counts[name] > 1:  # This name is duplicated
                        # Look for matching email in all_emails
                        name_parts = name.lower().split()
                        if len(name_parts) >= 2:
                            # Extract meaningful name components, skipping initials
                            meaningful_parts = []
                            for part in name_parts:
                                # Skip single letters or initials like "m."
                                if len(part) > 2 or (
                                    len(part) == 2 and not part.endswith(".")
                                ):
                                    meaningful_parts.append(part)

                            if len(meaningful_parts) >= 2:
                                # Use first meaningful name and last name
                                first_meaningful = meaningful_parts[0]
                                last = meaningful_parts[-1]

                                for email in all_emails:
                                    if email.strip():
                                        email_lower = email.strip().lower()
                                        # Check if email contains meaningful name parts
                                        if (
                                            first_meaningful in email_lower
                                            and last in email_lower
                                        ):
                                            if name not in name_to_emails:
                                                name_to_emails[name] = []
                                            name_to_emails[name].append(email.strip())
                            elif len(meaningful_parts) == 1:
                                # Handle case with only one meaningful part (like single surnames)
                                single_part = meaningful_parts[0]
                                for email in all_emails:
                                    if email.strip():
                                        email_lower = email.strip().lower()
                                        if single_part in email_lower:
                                            if name not in name_to_emails:
                                                name_to_emails[name] = []
                                            name_to_emails[name].append(email.strip())

                log_debug("Name to emails mapping: %s", name_to_emails)

                # Deduplicate names while preserving order of first occurrence
                dedupe_names, dedupe_roles, dedupe_sources = [], [], []
                seen_names = set()
                for name, role, source in zip(names, roles, sources):
                    if name not in seen_names:
                        dedupe_names.append(name)
                        dedupe_roles.append(role)
                        dedupe_sources.append(source)
                        seen_names.add(name)

                # Create consolidated email list aligned with deduplicated names
                consolidated_emails = []
                for name in dedupe_names:
                    emails_for_name = name_to_emails.get(name, [])
                    consolidated_emails.append(
                        emails_for_name[0] if emails_for_name else ""
                    )

                # Update email buckets with consolidated emails
                # Use contributor_email as the primary target
                email_buckets["contributor_email"] = consolidated_emails
                names, roles, sources = dedupe_names, dedupe_roles, dedupe_sources
                log_debug(
                    "After deduplication - Names: %s; Emails: %s",
                    names,
                    consolidated_emails,
                )

    # Step C: build contributor fields
    if names:
        # C1: names + roles
        cleaned["contributor_name"] = ", ".join(names)
        cleaned["contributor_role"] = cleaned.get("contributor_role", ", ".join(roles))
        log_debug(
            "Set contributor_name=%r, contributor_role=%r",
            cleaned["contributor_name"],
            cleaned["contributor_role"],
        )

        # C2: align emails one‑to‑one
        # If we have already aligned emails from deduplication, use those
        if "contributor_email" in email_buckets and len(
            email_buckets["contributor_email"]
        ) == len(names):
            # Use the already correctly aligned emails from deduplication
            aligned_emails = email_buckets["contributor_email"]
            log_debug("Using deduplicated emails: %s", aligned_emails)
        else:
            # Fall back to original alignment logic
            aligned_emails = []
            email_copy = {k: v.copy() for k, v in email_buckets.items()}
            for src in sources:
                base = src[:-5] if src.endswith("_name") else src
                ek = f"{base}_email"
                aligned_emails.append(
                    email_copy.get(ek, []).pop(0) if email_copy.get(ek) else ""
                )
        cleaned["contributor_email"] = ", ".join(aligned_emails)
        log_debug("Aligned contributor_email=%r", cleaned["contributor_email"])

        # C3: align URLs → contributor_id
        aligned_ids = []
        url_copy = {k: v.copy() for k, v in url_buckets.items()}
        for src in sources:
            base = src[:-5] if src.endswith("_name") else src
            uk = f"{base}_url"
            aligned_ids.append(url_copy.get(uk, []).pop(0) if url_copy.get(uk) else "")
        cleaned["contributor_id"] = ", ".join(aligned_ids)
        log_debug("Aligned contributor_id=%r", cleaned["contributor_id"])

    elif bucket_order:
        # Email-only (or URL-only) fallback
        # Build flat lists preserving email/url order
        flat_emails, flat_ids, placeholder_roles = [], [], []
        for typ, bk in bucket_order:
            role = role_map.get(bk.rsplit("_", 1)[0], "")
            if typ == "email":
                for e in email_buckets.get(bk, []):
                    flat_emails.append(e)
                    placeholder_roles.append(role)
            else:  # typ == "url"
                for u in url_buckets.get(bk, []):
                    flat_ids.append(u)
                    # ensure a role slot for each URL too
                    placeholder_roles.append(role)

        cleaned["contributor_name"] = ", ".join([""] * len(placeholder_roles))
        cleaned["contributor_role"] = ", ".join(placeholder_roles)
        cleaned["contributor_email"] = ", ".join(flat_emails)
        cleaned["contributor_id"] = ", ".join(flat_ids)
        log_debug("Placeholder contributor_email=%r", cleaned["contributor_email"])
        log_debug("Placeholder contributor_id=%r", cleaned["contributor_id"])

    # Step D: consolidate institution keys
    inst_vocab_map = defaults.INSTITUTION_VOCABULARY_MAP
    # Build normalized lookup (keys are already whitespace‑cleaned and casefolded)
    inst_vocab_norm = {
        re.sub(r"\s+", " ", key.casefold().strip()): url
        for key, url in inst_vocab_map.items()
    }
    for raw_key, url in inst_vocab_map.items():
        k2 = re.sub(r"\s+", " ", raw_key.replace("\u00a0", " ")).strip().lower()
        k2 = " ".join(raw_key.strip().casefold().split())
        inst_vocab_norm[k2] = url

        insts = []
        inst_vocabs = []
        for attr_key in list(cleaned.keys()):
            if attr_key.lower() in (
                "institution",
                "publisher_institution",
                "contributor_institution",
            ):
                raw_inst = cleaned.pop(attr_key)

                # apply any known corrections
                fixed = _INSTITUTION_CORRECTIONS.get(raw_inst, raw_inst)

                # split on semicolons only (commas inside names are preserved)
                if ";" in fixed:
                    parts = [p.strip() for p in fixed.split(";") if p.strip()]
                else:
                    parts = [fixed.strip()]

                for inst in parts:
                    # normalize for lookup
                    lookup = re.sub(r"\s+", " ", inst.casefold().strip())

                    # try exact match
                    url = inst_vocab_norm.get(lookup, "")

                    # fallback: substring match
                    if not url:
                        for k_norm, v in inst_vocab_norm.items():
                            if lookup == k_norm or lookup in k_norm:
                                url = v
                                break

                    insts.append(inst)
                    inst_vocabs.append(url)
                    log_debug("Matched institution %r → %r → %r", inst, lookup, url)

        if insts:
            # dedupe institutions, preserving order
            unique_insts = list(dict.fromkeys(insts))
            # align vocab list to those unique insts
            seen = set()
            unique_vocabs = []
            for inst, url in zip(insts, inst_vocabs):
                if inst not in seen:
                    seen.add(inst)
                    unique_vocabs.append(url)

            cleaned["contributing_institutions"] = ", ".join(unique_insts)
            cleaned["contributing_institutions_vocabulary"] = ", ".join(unique_vocabs)
            cleaned.setdefault("contributing_institutions_role", "")
            cleaned.setdefault("contributing_institutions_role_vocabulary", "")
    log_debug("Finished _consolidate_contributors: %s", cleaned)
    return cleaned


def merge_metadata_aliases(attrs: dict, preferred_keys: dict) -> dict:
    """Consolidate and rename metadata keys case‑insensitively (except featureType),
    using preferred_keys to map aliases to canonical names.

    Parameters
    ----------
    attrs : dict
        Metadata dictionary with potential duplicates.
    preferred_keys : dict
        Mapping of lowercase alias keys to preferred canonical keys.

    Returns
    -------
    dict
        Metadata dictionary with duplicates merged and keys renamed.

    """
    merged = {}
    for orig_key, value in attrs.items():
        # Preserve 'featureType' exactly
        if orig_key == "featureType":
            canonical = "featureType"
        elif orig_key == "Conventions":
            canonical = "Conventions"
        else:
            low = orig_key.lower()
            # 1) if we have a mapping for this lowercase alias, rename
            if low in preferred_keys:
                canonical = preferred_keys[low]
            # 2) otherwise use the lowercased key
            else:
                canonical = low

        # Log any renaming
        if canonical != orig_key:
            log_debug("Renaming key '%s' → '%s'", orig_key, canonical)

        # Merge duplicates by keeping the first or identical values
        if canonical in merged:
            if merged[canonical] == value:
                log_debug(
                    "Skipped duplicate (identical) key '%s' → '%s'", orig_key, canonical
                )
            else:
                log_debug(
                    "Conflict for '%s' from '%s'; keeping first value",
                    canonical,
                    orig_key,
                )
            continue

        merged[canonical] = value

    return merged


def standardize_time_coordinate(ds: xr.Dataset) -> xr.Dataset:
    """Standardize TIME coordinate to comply with AMOCatlas specifications.

    All datasets with a TIME coordinate should have standardized attributes:
    - data type: datetime64[ns]
    - long_name: "Time elapsed since 1970-01-01T00:00:00Z"
    - standard_name: "time"
    - calendar: "gregorian"
    - units: "seconds since 1970-01-01T00:00:00Z"
    - vocabulary: "http://vocab.nerc.ac.uk/collection/OG1/current/TIME/"

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to standardize TIME coordinate for.

    Returns
    -------
    xr.Dataset
        Dataset with standardized TIME coordinate attributes.

    """
    if "TIME" not in ds.coords and "TIME" not in ds.dims:
        return ds

    # Ensure TIME is a coordinate
    if "TIME" in ds.dims and "TIME" not in ds.coords:
        # If TIME is only a dimension, create a coordinate
        log_debug("TIME dimension found without coordinate - creating coordinate")
        if "TIME" in ds.data_vars:
            # If there's a TIME data variable, promote it to coordinate
            ds = ds.set_coords("TIME")
        else:
            # Create a simple index coordinate
            ds = ds.assign_coords(TIME=range(ds.sizes["TIME"]))

    time_coord = ds["TIME"]

    # Convert to datetime64[ns] if not already
    if time_coord.dtype.kind != "M":  # Not datetime64 type
        log_debug(
            f"Converting TIME coordinate from {time_coord.dtype} to datetime64[ns]"
        )

        if time_coord.dtype.kind in ["f", "i"]:  # numeric type (seconds since epoch)
            # Convert numeric time to datetime64[ns]
            import pandas as pd

            try:
                # Handle different epoch references - assume 1970-01-01 if no units specified
                units = time_coord.attrs.get(
                    "units", "seconds since 1970-01-01T00:00:00Z"
                )
                if "since" in units.lower():
                    # Parse the units and convert
                    time_datetime = pd.to_datetime(
                        time_coord.values,
                        unit="s",
                        origin="1970-01-01",
                        errors="coerce",
                    )
                else:
                    # Assume seconds since 1970-01-01
                    time_datetime = pd.to_datetime(
                        time_coord.values,
                        unit="s",
                        origin="1970-01-01",
                        errors="coerce",
                    )

                ds["TIME"] = ("TIME", time_datetime.astype("datetime64[ns]"))
            except Exception as e:
                log_debug(f"Failed to convert numeric TIME to datetime64[ns]: {e}")
                # Keep original values but warn
                ds["TIME"] = time_coord
        else:
            log_debug(f"Unknown TIME coordinate dtype: {time_coord.dtype}")
            # Keep original values
            ds["TIME"] = time_coord
    elif time_coord.dtype != "datetime64[ns]":
        # Convert datetime64 to nanosecond precision
        log_debug("Converting datetime64 TIME coordinate to nanosecond precision")
        import pandas as pd

        time_datetime = pd.to_datetime(time_coord.values, errors="coerce").astype(
            "datetime64[ns]"
        )
        ds["TIME"] = ("TIME", time_datetime)

    # Set standard TIME coordinate attributes for datetime64 format
    standard_time_attrs = {
        "long_name": "Time",
        "standard_name": "time",
        "calendar": "gregorian",
        "units": "datetime64[ns]",  # Use datetime64 units for clarity
        "vocabulary": "http://vocab.nerc.ac.uk/collection/P01/current/ELTMEP01/",
    }

    # Note: 'units' attribute not needed for datetime64 coordinates per CF conventions

    # Update TIME coordinate attributes
    ds["TIME"].attrs.update(standard_time_attrs)
    log_debug("Standardized TIME coordinate attributes")

    return ds


def standardize_longitude_coordinate(ds: xr.Dataset) -> xr.Dataset:
    """Standardize LONGITUDE coordinate to comply with AMOCatlas specifications.

    All datasets with a LONGITUDE coordinate should have standardized attributes:
    - data type: double
    - long_name: "longitude east (WGS84)"
    - standard_name: "longitude"
    - units: "degrees_east"

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to standardize LONGITUDE coordinate for.

    Returns
    -------
    xr.Dataset
        Dataset with standardized LONGITUDE coordinate attributes.

    """
    if "LONGITUDE" not in ds.coords and "LONGITUDE" not in ds.dims:
        return ds

    # Ensure LONGITUDE is a coordinate
    if "LONGITUDE" in ds.dims and "LONGITUDE" not in ds.coords:
        log_debug("LONGITUDE dimension found without coordinate - creating coordinate")
        if "LONGITUDE" in ds.data_vars:
            ds = ds.set_coords("LONGITUDE")
        else:
            ds = ds.assign_coords(LONGITUDE=range(ds.sizes["LONGITUDE"]))

    # Convert to double precision if not already
    if ds["LONGITUDE"].dtype != "float64":
        log_debug(
            f"Converting LONGITUDE coordinate from {ds['LONGITUDE'].dtype} to float64"
        )
        ds["LONGITUDE"] = ds["LONGITUDE"].astype("float64")

    # Set standard LONGITUDE coordinate attributes
    standard_lon_attrs = {
        "long_name": "Longitude",
        "description": "Longitude east (WGS84)",
        "standard_name": "longitude",
        "units": "degrees_east",
    }

    ds["LONGITUDE"].attrs.update(standard_lon_attrs)
    log_debug("Standardized LONGITUDE coordinate attributes")

    return ds


def standardize_latitude_coordinate(ds: xr.Dataset) -> xr.Dataset:
    """Standardize LATITUDE coordinate to comply with AMOCatlas specifications.

    All datasets with a LATITUDE coordinate should have standardized attributes:
    - data type: double
    - long_name: "Latitude north (WGS84)"
    - standard_name: "latitude"
    - units: "degrees_north"

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to standardize LATITUDE coordinate for.

    Returns
    -------
    xr.Dataset
        Dataset with standardized LATITUDE coordinate attributes.

    """
    if "LATITUDE" not in ds.coords and "LATITUDE" not in ds.dims:
        return ds

    # Ensure LATITUDE is a coordinate
    if "LATITUDE" in ds.dims and "LATITUDE" not in ds.coords:
        log_debug("LATITUDE dimension found without coordinate - creating coordinate")
        if "LATITUDE" in ds.data_vars:
            ds = ds.set_coords("LATITUDE")
        else:
            ds = ds.assign_coords(LATITUDE=range(ds.sizes["LATITUDE"]))

    # Convert to double precision if not already
    if ds["LATITUDE"].dtype != "float64":
        log_debug(
            f"Converting LATITUDE coordinate from {ds['LATITUDE'].dtype} to float64"
        )
        ds["LATITUDE"] = ds["LATITUDE"].astype("float64")

    # Set standard LATITUDE coordinate attributes
    standard_lat_attrs = {
        "long_name": "Latitude",
        "description": "Latitude north (WGS84)",
        "standard_name": "latitude",
        "units": "degrees_north",
    }

    ds["LATITUDE"].attrs.update(standard_lat_attrs)
    log_debug("Standardized LATITUDE coordinate attributes")

    return ds


def standardize_depth_coordinate(ds: xr.Dataset) -> xr.Dataset:
    """Standardize DEPTH coordinate to comply with AMOCatlas specifications.

    All datasets with a DEPTH coordinate should have standardized attributes:
    - data type: double
    - long_name: "Depth below surface of the water"
    - standard_name: "depth"
    - units: "meters"

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to standardize DEPTH coordinate for.

    Returns
    -------
    xr.Dataset
        Dataset with standardized DEPTH coordinate attributes.

    """
    if "DEPTH" not in ds.coords and "DEPTH" not in ds.dims:
        return ds

    # Ensure DEPTH is a coordinate
    if "DEPTH" in ds.dims and "DEPTH" not in ds.coords:
        log_debug("DEPTH dimension found without coordinate - creating coordinate")
        if "DEPTH" in ds.data_vars:
            ds = ds.set_coords("DEPTH")
        else:
            ds = ds.assign_coords(DEPTH=range(ds.sizes["DEPTH"]))

    # Convert to double precision if not already
    if ds["DEPTH"].dtype != "float64":
        log_debug(f"Converting DEPTH coordinate from {ds['DEPTH'].dtype} to float64")
        ds["DEPTH"] = ds["DEPTH"].astype("float64")

    # Set standard DEPTH coordinate attributes
    standard_depth_attrs = {
        "long_name": "Depth",
        "description": " Depth below surface of the water",
        "standard_name": "depth",
        "units": "meters",
    }

    ds["DEPTH"].attrs.update(standard_depth_attrs)
    log_debug("Standardized DEPTH coordinate attributes")

    return ds


def standardize_sigma0_coordinate(ds: xr.Dataset) -> xr.Dataset:
    """Standardize SIGMA0 coordinate to comply with AMOCatlas specifications.

    All datasets with a SIGMA0 coordinate should have standardized attributes:
    - data type: double
    - long_name: "Potential density anomaly to 1000 kg/m3, surface reference"
    - standard_name: "sea_water_sigma_theta"
    - units: "kg m-3"

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to standardize SIGMA0 coordinate for.

    Returns
    -------
    xr.Dataset
        Dataset with standardized SIGMA0 coordinate attributes.

    """
    if "SIGMA0" not in ds.coords and "SIGMA0" not in ds.dims:
        return ds

    # Ensure SIGMA0 is a coordinate
    if "SIGMA0" in ds.dims and "SIGMA0" not in ds.coords:
        log_debug("SIGMA0 dimension found without coordinate - creating coordinate")
        if "SIGMA0" in ds.data_vars:
            ds = ds.set_coords("SIGMA0")
        else:
            ds = ds.assign_coords(SIGMA0=range(ds.sizes["SIGMA0"]))

    # Convert to double precision if not already
    if ds["SIGMA0"].dtype != "float64":
        log_debug(f"Converting SIGMA0 coordinate from {ds['SIGMA0'].dtype} to float64")
        ds["SIGMA0"] = ds["SIGMA0"].astype("float64")

    # Set standard SIGMA0 coordinate attributes
    standard_sigma0_attrs = {
        "long_name": "Sigma0",
        "description": "Potential density anomaly to 1000 kg/m3, surface reference",
        "standard_name": "sea_water_sigma_theta",
        "units": "kg m-3",
    }

    ds["SIGMA0"].attrs.update(standard_sigma0_attrs)
    log_debug("Standardized SIGMA0 coordinate attributes")

    return ds


def standardize_units(ds: xr.Dataset) -> xr.Dataset:
    """Standardize variable units throughout the dataset.

    Uses the comprehensive unit mapping from utilities module.

    Parameters
    ----------
    ds : xr.Dataset
        Dataset to standardize units for.

    Returns
    -------
    xr.Dataset
        Dataset with standardized variable units.

    """
    from .utilities import standardize_dataset_units

    return standardize_dataset_units(ds, log_changes=True)


def standardise_samba(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise SAMBA array dataset to consistent format.

    .. deprecated::
        This function is deprecated. Use :func:`standardise_data` instead.

    Parameters
    ----------
    ds : xr.Dataset
        Raw SAMBA dataset to standardise.
    file_name : str
        Original filename for metadata.

    Returns
    -------
    xr.Dataset
        Standardised dataset with consistent metadata and formatting.

    """
    warnings.warn(
        "standardise_samba() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_data(ds, file_name)


def standardise_rapid(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise RAPID array dataset to consistent format.

    .. deprecated::
        This function is deprecated. Use :func:`standardise_data` instead.

    Parameters
    ----------
    ds : xr.Dataset
        Raw RAPID dataset to standardise.
    file_name : str
        Original filename for metadata.

    Returns
    -------
    xr.Dataset
        Standardised dataset with consistent metadata and formatting.

    """
    warnings.warn(
        "standardise_rapid() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_data(ds, file_name)


def standardise_move(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise MOVE array dataset to consistent format.

    Parameters
    ----------
    ds : xr.Dataset
        Raw MOVE dataset to standardise.
    file_name : str
        Original filename for metadata.

    Returns
    -------
    xr.Dataset
        Standardised dataset with consistent metadata and formatting.

    """
    warnings.warn(
        "standardise_move() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_osnap(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise OSNAP array dataset to consistent format."""
    warnings.warn(
        "standardise_osnap() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_fw2015(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise FW2015 array dataset to consistent format."""
    warnings.warn(
        "standardise_move() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    return standardise_array(ds, file_name)


def standardise_mocha(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise MOCHA array dataset to consistent format."""
    warnings.warn(
        "standardise_mocha() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_41n(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise 41N array dataset to consistent format."""
    warnings.warn(
        "standardise_41n() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_dso(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise DSO array dataset to consistent format."""
    warnings.warn(
        "standardise_dso() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_calafat2025(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise CALAFAT2025 array dataset to consistent format."""
    warnings.warn(
        "standardise_calafat2025() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_zheng2024(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise ZHENG2024 array dataset to consistent format."""
    warnings.warn(
        "standardise_zheng2024() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_47n(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise 47N array dataset to a consistent format.

    Parameters
    ----------
    ds : xr.Dataset
        Raw 47N array dataset to standardise.
    file_name : str
        Original filename associated with the dataset, used for metadata.

    Returns
    -------
    xr.Dataset
        Standardised dataset with consistent metadata and formatting for the 47N array.

    """
    warnings.warn(
        "standardise_47n() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_fbc(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise FBC array dataset to consistent format."""
    warnings.warn(
        "standardise_fbc() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_array(ds, file_name)


def standardise_arcticgateway(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise Arctic Gateway array dataset to consistent format."""
    warnings.warn(
        "standardise_arcticgateway() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    return standardise_array(ds, file_name)


def standardise_data(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise a dataset using YAML-based metadata.

    Parameters
    ----------
    ds : xr.Dataset
        Raw dataset loaded from a reader with amocatlas_datasource metadata.
    file_name : str
        Filename (e.g., 'moc_transports.nc') expected to match ds.attrs["source_file"].

    Returns
    -------
    xr.Dataset
        Standardised dataset with renamed variables and enriched metadata.

    Raises
    ------
    ValueError
        If file_name does not match ds.attrs["source_file"].
    ValueError
        If amocatlas_datasource is not found in dataset metadata.

    """
    # 1) Validate source_file matches
    src = ds.attrs.get("source_file")
    if src and src != file_name:
        raise ValueError(f"file_name {file_name!r} ≠ ds.attrs['source_file'] {src!r}")

    # 2) Get datasource ID from dataset metadata
    datasource_id = ds.attrs.get("processing_datasource")
    if not datasource_id:
        raise ValueError("Dataset missing required 'processing_datasource' metadata")

    log_debug(f"Standardising {file_name} for {datasource_id.upper()}")

    # 3) Collect new attrs from YAML
    meta = utilities.load_array_metadata(datasource_id)
    file_meta = meta["files"].get(file_name, {})

    # 3.5) Remove unwanted variables if specified
    variables_to_remove = file_meta.get("variables_to_remove", [])
    if variables_to_remove:
        # Handle case where YAML parser returns a string instead of list
        if isinstance(variables_to_remove, str):
            variables_to_remove = variables_to_remove.split()
            log_debug(f"Converted string to list: {variables_to_remove}")

        vars_removed = []
        for var_name in variables_to_remove:
            if var_name in ds.variables:
                ds = ds.drop_vars(var_name)
                vars_removed.append(var_name)
                log_debug(f"Removed variable '{var_name}' from dataset")
            else:
                log_debug(f"Variable '{var_name}' not found for removal")

        if vars_removed:
            log_debug(f"Removed {len(vars_removed)} variables: {vars_removed}")

    # Apply per-variable metadata BEFORE renaming (metadata refers to original variable names)
    var_meta = file_meta.get("original_variable_metadata", {})
    for var_name, attrs in var_meta.items():
        if var_name in ds.variables:
            ds[var_name].attrs.update(attrs)
            log_debug(f"Applied metadata to original variable '{var_name}'")

    # Rename variables and track what was actually renamed
    # Prefer dataset's variable_mapping (which may have sanitized names) over YAML
    rename_dict = ds.attrs.get(
        "variable_mapping", file_meta.get("variable_mapping", {})
    )
    applied_mapping = {}

    if rename_dict:
        # Only rename variables that actually exist and need renaming
        valid_renames = {
            old: new
            for old, new in rename_dict.items()
            if old in ds.variables and old != new
        }

        if valid_renames:
            ds = ds.rename(valid_renames)
            applied_mapping.update(valid_renames)
            log_debug("Applied variable renaming: %s", valid_renames)

        # For variables that couldn't be renamed (case mismatch, etc.),
        # try to find them with case-insensitive matching and track pass-through
        failed_renames = {
            old: new
            for old, new in rename_dict.items()
            if old not in ds.variables and old != new
        }

        if failed_renames:
            log_debug("Failed to find exact matches for renaming: %s", failed_renames)

            # Try case-insensitive matching for pass-through tracking
            ds_vars_lower = {var.lower(): var for var in ds.variables}
            for orig_name, std_name in failed_renames.items():
                orig_lower = orig_name.lower()
                if orig_lower in ds_vars_lower:
                    actual_var = ds_vars_lower[orig_lower]
                    # Track as pass-through: actual_name -> actual_name (no rename occurred)
                    applied_mapping[actual_var] = actual_var
                    log_debug(
                        "Pass-through (case mismatch): %s (expected %s -> %s)",
                        actual_var,
                        orig_name,
                        std_name,
                    )

        # Track coordinates that were successfully renamed
        coord_renames = {
            old: new
            for old, new in rename_dict.items()
            if old in ds.coords and old != new
        }
        if coord_renames:
            applied_mapping.update(coord_renames)

    # Always track applied mapping (even if empty) for consistent reporting
    if applied_mapping:
        ds.attrs["applied_variable_mapping"] = applied_mapping
        log_debug(
            "Total applied mapping (renames + pass-throughs): %s", applied_mapping
        )
    else:
        log_debug("No variable_mapping found or applied for %s", file_name)

    # Handle convert_to_coord directive
    convert_to_coord = file_meta.get("convert_to_coord")
    if convert_to_coord:
        # Check if this variable was renamed - look for the mapped name
        target_var = convert_to_coord
        if rename_dict and convert_to_coord in rename_dict:
            target_var = rename_dict[convert_to_coord]
            log_debug(
                f"Using mapped variable name '{target_var}' for convert_to_coord (was '{convert_to_coord}')"
            )

        if target_var in ds.data_vars:
            log_debug(f"Converting variable '{target_var}' to coordinate")
            # Get the variable data and attributes
            var_data = ds[target_var]
            var_attrs = var_data.attrs.copy()

            # Remove the variable from data_vars and add as coordinate
            ds = ds.drop_vars(target_var)
            ds = ds.assign_coords({target_var: var_data})

            # Restore attributes
            ds[target_var].attrs.update(var_attrs)
            log_debug(f"Successfully converted '{target_var}' to coordinate")
        else:
            log_debug(
                f"Variable '{target_var}' not found in dataset for coordinate conversion"
            )

    # Variable metadata was already applied before renaming (lines 1125-1130)

    # Special handling for heat transport unit conversion (W to PW)
    # Convert any remapped variable with units="W" and standard_name containing "northward_ocean_heat_transport"
    for var_name in ds.variables:
        var_attrs = ds[var_name].attrs
        if var_attrs.get(
            "units"
        ) == "W" and "northward_ocean_heat_transport" in var_attrs.get(
            "standard_name", ""
        ):
            log_debug(f"Converting heat transport variable '{var_name}' from W to PW")
            # Convert data from watts to petawatts (divide by 10^15)
            ds[var_name] = ds[var_name] / 1e15
            # Update units attribute
            ds[var_name].attrs["units"] = "PW"

    # If any attributes are blank or value 'n/a', remove them
    for var_name, attrs in list(var_meta.items()):
        if var_name in ds.variables:
            for attr_key, attr_value in attrs.items():
                if attr_value in ("", "n/a"):
                    ds[var_name].attrs.pop(attr_key, None)
                    log_debug(
                        "Removed blank attribute '%s' from variable '%s'",
                        attr_key,
                        var_name,
                    )
    # Remove any empty attributes from the dataset
    for attr_key, attr_value in list(
        ds.attrs.items()
    ):  # Iterate over a copy of the items
        if attr_value in ("", "n/a"):
            ds.attrs.pop(attr_key, None)
            log_debug("Removed blank attribute '%s' from dataset", attr_key)

    # 3) Merge existing attrs + new global attrs + file-specific
    combined = {}
    combined.update(ds.attrs)  # original reader attrs
    combined.update(meta.get("metadata", {}))  # array‑level
    combined.update(
        {
            "summary": meta["metadata"].get("description", ""),
            "weblink": meta["metadata"].get("weblink", ""),
        }
    )
    combined.update(
        {
            k: file_meta[k]
            for k in ("acknowledgment", "data_product", "citation")
            if k in file_meta
        }
    )

    # 4) Clean up collisions & override ds.attrs wholesale
    cleaned = clean_metadata(combined)

    # 4.5) Process overwrite directives from YAML metadata AFTER cleaning
    # This ensures overrides are not reverted by merge conflict resolution
    all_yaml_metadata = {}
    all_yaml_metadata.update(meta.get("metadata", {}))  # array-level
    all_yaml_metadata.update(file_meta)  # file-level

    overwrite_applied = {}
    for key, value in all_yaml_metadata.items():
        if key.endswith("_overwrite"):
            # Extract the base key name (remove _overwrite suffix)
            base_key = key[:-10]  # Remove "_overwrite" (10 characters)

            # Force overwrite the attribute even if it already exists
            cleaned[base_key] = value
            overwrite_applied[base_key] = value
            log_debug(
                f"Applied overwrite: '{base_key}' = '{str(value)[:50]}{'...' if len(str(value)) > 50 else ''}'"
            )

    if overwrite_applied:
        log_debug(
            f"Applied {len(overwrite_applied)} metadata overrides: {list(overwrite_applied.keys())}"
        )

    # 5) Standardize date formats and add processing metadata

    def standardize_date_format(date_string: str) -> str:
        """Standardize date to ISO 8601 format with Z timezone: YYYY-MM-DDTHH:MM:SSZ

        Handles various input formats and converts to UTC with Z suffix.
        """
        if not date_string or date_string.strip() == "":
            return date_string

        date_str = str(date_string).strip()

        # If already in correct format, return as-is
        if date_str.endswith("Z") and "T" in date_str and len(date_str) == 20:
            return date_str

        # Common date formats to try parsing
        formats_to_try = [
            "%Y-%m-%dT%H:%M:%SZ",  # Already correct
            "%Y-%m-%dT%H:%M:%S",  # Missing Z
            "%Y-%m-%d %H:%M:%S",  # Space instead of T
            "%Y-%m-%d",  # Date only
            "%Y-%m-%dT%H:%M:%S.%fZ",  # With microseconds and Z
            "%Y-%m-%dT%H:%M:%S.%f",  # With microseconds, no Z
            "%d-%m-%Y",  # European format
            "%m/%d/%Y",  # US format
            "%Y%m%d",  # Compact format
        ]

        for fmt in formats_to_try:
            try:
                dt = datetime.strptime(date_str, fmt)
                # Return in standard format with Z
                return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                continue

        # If no format worked, return original
        log_debug(f"Could not parse date format: {date_str}")
        return date_string

    def standardize_license_format(license_string: str) -> str:
        """Standardize license to SPDX identifier format where possible.

        Converts common Creative Commons license variations to standard SPDX identifiers.
        """
        if not license_string or license_string.strip() == "":
            return license_string

        license_str = str(license_string).strip()

        # Creative Commons Attribution 4.0 variations
        cc_by_4_patterns = [
            "Creative Commons Attribution 4.0 International (CC BY 4.0)",
            "Creative Commons Attribution 4.0 International",
            "CC BY 4.0",
            "CC-BY 4.0",
            "CCBY4.0",
            "CC BY-4.0",
        ]

        # Check for CC BY 4.0 variations (case insensitive)
        license_lower = license_str.lower()
        if any(pattern.lower() in license_lower for pattern in cc_by_4_patterns):
            if (
                "cc" in license_lower
                and "by" in license_lower
                and "4.0" in license_lower
            ):
                return "CC-BY-4.0"

        # Other common licenses (can be extended)
        license_mappings = {
            "ODC-By": "ODC-BY",  # Open Data Commons Attribution
            "odc-by": "ODC-BY",
            "MIT": "MIT",
            "Apache-2.0": "Apache-2.0",
            "BSD-3-Clause": "BSD-3-Clause",
        }

        # Check exact matches first
        if license_str in license_mappings:
            return license_mappings[license_str]

        # Check case-insensitive matches
        for original, standardized in license_mappings.items():
            if license_str.lower() == original.lower():
                return standardized

        # If no standardization found, return original
        return license_str

    # Standardize date fields in metadata
    date_fields = [
        "date_created",
        "date_modified",
        "date_issued",
        "date_metadata_modified",
    ]
    for field in date_fields:
        if field in cleaned and cleaned[field]:
            cleaned[field] = standardize_date_format(cleaned[field])

    # Standardize license field
    if "license" in cleaned and cleaned["license"]:
        cleaned["license"] = standardize_license_format(cleaned["license"])

    def sanitize_source_path(path_string: str) -> str:
        """Sanitize source paths to remove specific user directory structures.

        Replaces hardcoded paths with generic equivalents for portability.
        Only affects display - other users will see their full paths unchanged.
        """
        if not path_string or path_string.strip() == "":
            return path_string

        path_str = str(path_string).strip()

        # Replace specific user path with generic equivalent
        # This will only match for the specific user, others see full paths
        specific_path = "/Users/eddifying/Cloudfree/github/"
        if specific_path in path_str:
            sanitized = path_str.replace(specific_path, "~/")
            log_debug(f"Sanitized source path: {path_str} → {sanitized}")
            return sanitized

        return path_str

    # Sanitize path fields in metadata
    path_fields = ["source_path", "source_file"]
    for field in path_fields:
        if field in cleaned and cleaned[field]:
            cleaned[field] = sanitize_source_path(cleaned[field])

    # Remove old comment-based processing info if it exists
    if "comment" in cleaned:
        comment = cleaned["comment"]
        if (
            "Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas"
            in comment
        ):
            # Remove this text from comment, keeping other parts
            cleaned_comment = comment.replace(
                "Dataset accessed and processed via http://github.com/AMOCcommunity/amocatlas",
                "",
            ).strip()
            if cleaned_comment:
                cleaned["comment"] = cleaned_comment
            else:
                cleaned.pop("comment", None)

    # Add proper processing metadata
    cleaned["processing_software"] = "http://github.com/AMOCcommunity/amocatlas"
    cleaned["processing_version"] = get_dynamic_version()
    cleaned["date_modified"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Remove internal metadata fields from final dataset
    cleaned.pop("amocatlas_datasource", None)

    # Ensure Conventions includes OceanSITES-1.5
    if "Conventions" in cleaned:
        conventions = cleaned["Conventions"]
        if "OceanSITES-1.5" not in conventions:
            # Append OceanSITES-1.5 to existing conventions
            cleaned["Conventions"] = f"{conventions}, OceanSITES-1.5"
    else:
        # Set default conventions if none exist
        cleaned["Conventions"] = "CF-1.8, ACDD-1.3, OceanSITES-1.5"

    # 6) Normalize and add vocabularies
    normalizations = defaults.PLATFORM_NORMALIZATIONS
    cleaned = normalize_and_add_vocabulary(cleaned, normalizations)

    # 7) Standardize coordinate attributes
    ds = standardize_time_coordinate(ds)
    ds = standardize_longitude_coordinate(ds)
    ds = standardize_latitude_coordinate(ds)
    ds = standardize_depth_coordinate(ds)
    ds = standardize_sigma0_coordinate(ds)

    # 8) Standardize units
    ds = standardize_units(ds)

    # 9) Apply cleaned metadata and reorder according to canonical order
    ds.attrs = cleaned
    ds.attrs = reorder_metadata(ds.attrs)

    # 10) Apply unit standardization again after metadata processing
    # This ensures units are not overwritten by YAML metadata operations
    ds = standardize_units(ds)

    #    ds = utilities.safe_update_attrs(ds, cleaned, overwrite=False)
    return ds


def standardise_array(ds: xr.Dataset, file_name: str) -> xr.Dataset:
    """Standardise a mooring array dataset using YAML-based metadata.

    .. deprecated::
        This function is deprecated. Use :func:`standardise_data` instead.

    Parameters
    ----------
    ds : xr.Dataset
        Raw dataset loaded from a reader with amocatlas_datasource metadata.
    file_name : str
        Filename (e.g., 'moc_transports.nc') expected to match ds.attrs["source_file"].

    Returns
    -------
    xr.Dataset
        Standardised dataset with renamed variables and enriched metadata.

    """
    warnings.warn(
        "standardise_array() is deprecated and will be removed in a future version. "
        "Use standardise_data() instead.",
        DeprecationWarning,
        stacklevel=2,
    )
    return standardise_data(ds, file_name)
