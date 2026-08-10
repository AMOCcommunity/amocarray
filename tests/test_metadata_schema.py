"""Schema validation for the array metadata YAML files.

Every ``amocatlas/metadata/<array>.yml`` file is validated against
``amocatlas/metadata/array_schema.json``. The schema uses closed key sets
(``additionalProperties: false``) so that typos and unmapped keys — which the
standardiser would otherwise silently ignore — fail loudly here instead.

A second test asserts the schema's allowed ``metadata`` keys stay a superset of
the canonical attributes and recognised aliases defined in ``defaults.py``, so
the schema cannot drift out of sync with the code.
"""

import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

from amocatlas import defaults

METADATA_DIR = Path(defaults.__file__).parent / "metadata"
SCHEMA_PATH = METADATA_DIR / "array_schema.json"

# Registry files have a different structure and are not array metadata.
REGISTRY_FILES = {"contributor_registry.yml", "institution_registry.yml"}


def _array_yaml_files() -> list[Path]:
    return sorted(p for p in METADATA_DIR.glob("*.yml") if p.name not in REGISTRY_FILES)


def _load_schema() -> dict:
    with SCHEMA_PATH.open() as fh:
        return json.load(fh)


def test_schema_file_is_valid() -> None:
    """The schema itself is a well-formed Draft 2020-12 schema."""
    Draft202012Validator.check_schema(_load_schema())


def test_at_least_one_array_yaml_found() -> None:
    """Guard against the glob silently matching nothing."""
    assert len(_array_yaml_files()) >= 18


@pytest.mark.parametrize("yaml_path", _array_yaml_files(), ids=lambda p: p.name)
def test_array_yaml_matches_schema(yaml_path: Path) -> None:
    """Each array YAML validates against the schema with no errors."""
    with yaml_path.open() as fh:
        data = yaml.safe_load(fh)
    validator = Draft202012Validator(_load_schema())
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    messages = [
        f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors
    ]
    assert not messages, f"{yaml_path.name} violates schema:\n" + "\n".join(messages)


def test_schema_stays_in_sync_with_defaults() -> None:
    """Schema's allowed metadata keys cover every canonical attr and alias.

    If a key is added to ``GLOBAL_ATTR_ORDER`` or ``METADATA_KEY_MAPPINGS`` but
    not to the schema, this fails and prompts a schema update.
    """
    schema = _load_schema()
    allowed = set(schema["properties"]["metadata"]["properties"])
    required = (
        set(defaults.GLOBAL_ATTR_ORDER)
        | set(defaults.METADATA_KEY_MAPPINGS.keys())
        | set(defaults.METADATA_KEY_MAPPINGS.values())
    )
    missing = required - allowed
    assert not missing, f"Schema missing keys defined in defaults.py: {sorted(missing)}"
