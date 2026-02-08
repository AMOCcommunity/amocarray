"""Registry lookup utilities for contributor and institution standardization.

This module provides functions to match contributor names and institution names
against the standardized registry using fuzzy matching on name variants.
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple
import yaml

from amocatlas.logger import log_debug, log_warning


def load_contributor_registry(registry_file: Optional[Path] = None) -> Dict:
    """Load the contributor registry from YAML file.

    Parameters
    ----------
    registry_file : Path, optional
        Path to the registry file. If None, uses the default location.

    Returns
    -------
    Dict
        Dictionary containing contributors data

    Raises
    ------
    FileNotFoundError
        If registry file cannot be found or loaded

    """
    if registry_file is None:
        # Default location in metadata directory
        registry_file = Path(__file__).parent / "metadata" / "contributor_registry.yml"

    try:
        with open(registry_file, "r", encoding="utf-8") as f:
            registry = yaml.safe_load(f)
        log_debug(
            f"Loaded contributor registry with {len(registry.get('contributors', {}))} contributors"
        )
        return registry
    except Exception as e:
        log_warning(f"Could not load contributor registry from {registry_file}: {e}")
        return {"contributors": {}}


def load_institution_registry(registry_file: Optional[Path] = None) -> Dict:
    """Load the institution registry from YAML file.

    Parameters
    ----------
    registry_file : Path, optional
        Path to the registry file. If None, uses the default location.

    Returns
    -------
    Dict
        Dictionary containing institutions data

    Raises
    ------
    FileNotFoundError
        If registry file cannot be found or loaded

    """
    if registry_file is None:
        # Default location in metadata directory
        registry_file = Path(__file__).parent / "metadata" / "institution_registry.yml"

    try:
        with open(registry_file, "r", encoding="utf-8") as f:
            registry = yaml.safe_load(f)
        log_debug(
            f"Loaded institution registry with {len(registry.get('institutions', {}))} institutions"
        )
        return registry
    except Exception as e:
        log_warning(f"Could not load institution registry from {registry_file}: {e}")
        return {"institutions": {}}


def find_contributor_orcid(
    name: str, registry: Optional[Dict] = None
) -> Optional[Tuple[str, Dict]]:
    """Find ORCID and standardized info for a contributor name using fuzzy matching.

    Parameters
    ----------
    name : str
        Raw contributor name to match
    registry : Dict, optional
        Pre-loaded registry. If None, loads from default location.

    Returns
    -------
    Optional[Tuple[str, Dict]]
        Tuple of (ORCID, contributor_info) if match found, None otherwise

    Examples
    --------
    >>> orcid, info = find_contributor_orcid("B. Moat")
    >>> print(orcid)  # "0000-0002-3644-8181"
    >>> print(info['standard_name'])  # "Ben I. Moat"

    """
    if registry is None:
        registry = load_contributor_registry()

    contributors = registry.get("contributors", {})
    name_cleaned = name.strip()

    # Try exact match first on name variants
    for orcid, contributor_info in contributors.items():
        name_variants = contributor_info.get("name_variants", [])
        if name_cleaned in name_variants:
            log_debug(f"Found exact match for '{name_cleaned}' -> ORCID {orcid}")
            return orcid, contributor_info

    # Try case-insensitive match
    name_lower = name_cleaned.lower()
    for orcid, contributor_info in contributors.items():
        name_variants = contributor_info.get("name_variants", [])
        if any(variant.lower() == name_lower for variant in name_variants):
            log_debug(
                f"Found case-insensitive match for '{name_cleaned}' -> ORCID {orcid}"
            )
            return orcid, contributor_info

    # No match found
    log_debug(f"No ORCID match found for contributor '{name_cleaned}'")
    return None


def find_institution_edmo(
    name: str, registry: Optional[Dict] = None
) -> Optional[Tuple[str, Dict]]:
    """Find EDMO code and standardized info for an institution name using fuzzy matching.

    Parameters
    ----------
    name : str
        Raw institution name to match
    registry : Dict, optional
        Pre-loaded registry. If None, loads from default location.

    Returns
    -------
    Optional[Tuple[str, Dict]]
        Tuple of (EDMO_code, institution_info) if match found, None otherwise

    Examples
    --------
    >>> edmo, info = find_institution_edmo("NOC Southampton")
    >>> print(edmo)  # "1910"
    >>> print(info['standard_name'])  # "National Oceanography Centre"

    """
    if registry is None:
        registry = load_institution_registry()

    institutions = registry.get("institutions", {})
    name_cleaned = name.strip()

    # Try exact match first on name variants
    for edmo_code, institution_info in institutions.items():
        name_variants = institution_info.get("name_variants", [])
        if name_cleaned in name_variants:
            log_debug(f"Found exact match for '{name_cleaned}' -> EDMO {edmo_code}")
            return edmo_code, institution_info

    # Try case-insensitive match
    name_lower = name_cleaned.lower()
    for edmo_code, institution_info in institutions.items():
        name_variants = institution_info.get("name_variants", [])
        if any(variant.lower() == name_lower for variant in name_variants):
            log_debug(
                f"Found case-insensitive match for '{name_cleaned}' -> EDMO {edmo_code}"
            )
            return edmo_code, institution_info

    # No match found
    log_debug(f"No EDMO match found for institution '{name_cleaned}'")
    return None


def standardize_contributor_info(
    raw_names: List[str], registry: Optional[Dict] = None
) -> Dict[str, List[str]]:
    """Standardize a list of contributor names using the registry.

    Parameters
    ----------
    raw_names : List[str]
        List of raw contributor names from dataset
    registry : Dict, optional
        Pre-loaded registry. If None, loads from default location.

    Returns
    -------
    Dict[str, List[str]]
        Dictionary with standardized contributor information:
        - 'names': standardized names
        - 'orcids': corresponding ORCIDs (empty string if not found)

    Examples
    --------
    >>> result = standardize_contributor_info(["B. Moat", "Unknown Person"])
    >>> print(result['names'])  # ["Ben I. Moat", "Unknown Person"]
    >>> print(result['orcids'])  # ["0000-0002-3644-8181", ""]

    """
    if registry is None:
        registry = load_contributor_registry()

    standardized_names = []
    orcids = []

    for raw_name in raw_names:
        match_result = find_contributor_orcid(raw_name, registry)

        if match_result:
            orcid, contributor_info = match_result
            standard_name = contributor_info.get("standard_name", raw_name)

            standardized_names.append(standard_name)
            orcids.append(orcid)
        else:
            # Keep original name if no match found
            standardized_names.append(raw_name)
            orcids.append("")

    return {"names": standardized_names, "orcids": orcids}


def standardize_institution_info(
    raw_names: List[str], registry: Optional[Dict] = None
) -> Dict[str, List[str]]:
    """Standardize a list of institution names using the registry.

    Parameters
    ----------
    raw_names : List[str]
        List of raw institution names from dataset
    registry : Dict, optional
        Pre-loaded registry. If None, loads from default location.

    Returns
    -------
    Dict[str, List[str]]
        Dictionary with standardized institution information:
        - 'names': standardized names
        - 'edmo_codes': corresponding EDMO codes (empty string if not found)
        - 'countries': countries from registry

    Examples
    --------
    >>> result = standardize_institution_info(["NOC Southampton", "Unknown University"])
    >>> print(result['names'])  # ["National Oceanography Centre", "Unknown University"]
    >>> print(result['edmo_codes'])  # ["1910", ""]

    """
    if registry is None:
        registry = load_institution_registry()

    standardized_names = []
    edmo_codes = []
    countries = []

    for raw_name in raw_names:
        match_result = find_institution_edmo(raw_name, registry)

        if match_result:
            edmo_code, institution_info = match_result
            standard_name = institution_info.get("standard_name", raw_name)
            country = institution_info.get("country", "")

            standardized_names.append(standard_name)
            edmo_codes.append(edmo_code)
            countries.append(country)
        else:
            # Keep original name if no match found
            standardized_names.append(raw_name)
            edmo_codes.append("")
            countries.append("")

    return {
        "names": standardized_names,
        "edmo_codes": edmo_codes,
        "countries": countries,
    }
