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
    with SCHEMA_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


class _UniqueKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate mapping keys.

    ``yaml.safe_load`` silently keeps the last of a duplicated key, so a rename onto
    an existing key drops a value with no error. This loader raises instead.
    """


def _no_duplicate_keys(loader: _UniqueKeyLoader, node: yaml.MappingNode) -> dict:
    seen = set()
    for key_node, _value_node in node.value:
        key = loader.construct_object(key_node, deep=True)
        if key in seen:
            raise ValueError(f"Duplicate key {key!r}")
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=True)


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicate_keys
)


def test_schema_file_is_valid() -> None:
    """The schema itself is a well-formed Draft 2020-12 schema."""
    Draft202012Validator.check_schema(_load_schema())


def test_at_least_one_array_yaml_found() -> None:
    """Guard against the glob silently matching nothing."""
    assert len(_array_yaml_files()) >= 18


@pytest.mark.parametrize("yaml_path", _array_yaml_files(), ids=lambda p: p.name)
def test_array_yaml_matches_schema(yaml_path: Path) -> None:
    """Each array YAML validates against the schema with no errors."""
    with yaml_path.open(encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    validator = Draft202012Validator(_load_schema())
    errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
    messages = [
        f"{'/'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in errors
    ]
    assert not messages, f"{yaml_path.name} violates schema:\n" + "\n".join(messages)


@pytest.mark.parametrize("yaml_path", _array_yaml_files(), ids=lambda p: p.name)
def test_array_yaml_has_no_duplicate_keys(yaml_path: Path) -> None:
    """No array YAML has a duplicate mapping key (which safe_load would hide)."""
    with yaml_path.open(encoding="utf-8") as fh:
        yaml.load(fh, Loader=_UniqueKeyLoader)


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
