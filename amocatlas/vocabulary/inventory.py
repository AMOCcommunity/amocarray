"""Scan the per-array metadata YAMLs and inventory every standardised variable.

The metadata YAMLs under ``amocatlas/metadata/`` are the ground truth for what
AMOCatlas actually serves: each ``files.<file>.variable_mapping`` maps a provider
variable name to a standardised short name, and ``original_variable_metadata`` carries
the verified ``standard_name``/``units``/``long_name`` for that provider variable.

This module gathers those into a per-short-name inventory so the vocabulary can be
populated from what is served rather than from recall, and so conflicts (one short name
served with two different standard_names or units) surface explicitly.

It reads only; it does not write or fabricate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, List

METADATA_DIR = Path(__file__).resolve().parent.parent / "metadata"

# Registry/schema files under metadata/ that are not per-array YAMLs.
_NON_ARRAY = {
    "contributor_registry.yml",
    "institution_registry.yml",
    "array_schema.json",
}


@dataclass
class Occurrence:
    """One appearance of a standardised short name in a source file."""

    array: str
    source_file: str
    original_name: str
    standard_name: str | None
    units: str | None
    long_name: str | None
    description: str | None


@dataclass
class ShortName:
    """All occurrences of one standardised short name across arrays."""

    name: str
    occurrences: List[Occurrence] = field(default_factory=list)

    @property
    def standard_names(self) -> set:
        """Distinct standard_names this short name is served with."""
        return {o.standard_name for o in self.occurrences}

    @property
    def units(self) -> set:
        """Distinct units this short name is served with."""
        return {o.units for o in self.occurrences}

    @property
    def arrays(self) -> set:
        """Arrays that serve this short name."""
        return {o.array for o in self.occurrences}

    @property
    def has_conflict(self) -> bool:
        """True if this name is served with more than one standard_name or unit."""
        sn = {s for s in self.standard_names if s}
        un = {u for u in self.units if u}
        return len(sn) > 1 or len(un) > 1


def _iter_array_yaml(metadata_dir: Path) -> "Iterator[Path]":
    for path in sorted(metadata_dir.glob("*.yml")):
        if path.name in _NON_ARRAY:
            continue
        yield path


def build_inventory(metadata_dir: Path = METADATA_DIR) -> Dict[str, ShortName]:
    """Return {short_name: ShortName} across all per-array metadata YAMLs."""
    import yaml

    result: Dict[str, ShortName] = {}

    for path in _iter_array_yaml(metadata_dir):
        array = path.stem
        with open(path, "r", encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        files = doc.get("files") or {}
        for source_file, spec in files.items():
            if not isinstance(spec, dict):
                continue
            mapping = spec.get("variable_mapping") or {}
            ovm = spec.get("original_variable_metadata") or {}
            for original_name, short in mapping.items():
                if not isinstance(short, str):
                    continue
                meta = ovm.get(original_name) or {}
                occ = Occurrence(
                    array=array,
                    source_file=source_file,
                    original_name=original_name,
                    standard_name=meta.get("standard_name"),
                    units=meta.get("units"),
                    long_name=meta.get("long_name"),
                    description=meta.get("description"),
                )
                result.setdefault(short, ShortName(name=short)).occurrences.append(occ)

    return dict(sorted(result.items()))


def summarize(inventory: Dict[str, ShortName]) -> str:
    """Human-readable summary: names, their standard_names/units, and conflicts."""
    lines = [f"{len(inventory)} standardised short names across the arrays.", ""]
    conflicts = [n for n in inventory.values() if n.has_conflict]
    lines.append(f"{len(conflicts)} served with conflicting standard_name or units:")
    for sn in conflicts:
        lines.append(f"  {sn.name}:")
        lines.append(
            f"    standard_names: {sorted(s or '-' for s in sn.standard_names)}"
        )
        lines.append(f"    units:          {sorted(u or '-' for u in sn.units)}")
        lines.append(f"    arrays:         {sorted(sn.arrays)}")
    return "\n".join(lines)


if __name__ == "__main__":
    inv = build_inventory()
    print(summarize(inv))
