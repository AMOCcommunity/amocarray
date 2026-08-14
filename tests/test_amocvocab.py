"""Tests for the amocvocab vocabulary and its validator.

The fast checks (schema, name==key, referential integrity) run everywhere. The CF-name
and units-convertibility checks need the CF standard-name table; they run only when a
table is available locally (``AMOCVOCAB_CF_TABLE`` or a cached copy). CI runs the full
validator in a dedicated job that fetches the table (see .github/workflows/amocvocab.yml).
"""

import pytest

from amocatlas.vocabulary import inventory, validate_amocvocab as V

VOCAB = V.DEFAULT_VOCAB
SCHEMA = V.DEFAULT_SCHEMA


@pytest.fixture(scope="module")
def vocab():
    return V.load_yaml(VOCAB)


@pytest.fixture(scope="module")
def schema():
    return V.load_schema(SCHEMA)


def test_schema_is_valid_draft2020(schema):
    from jsonschema import Draft202012Validator

    Draft202012Validator.check_schema(schema)


def test_vocab_matches_schema(vocab, schema):
    errors = V.schema_errors(vocab, schema)
    assert errors == [], "amocvocab.yml violates its schema:\n" + "\n".join(errors)


def test_name_equals_key(vocab):
    assert V.name_key_errors(vocab) == []


def test_referential_integrity(vocab):
    assert V.referential_errors(vocab) == []


def test_every_standard_name_is_null_or_string(vocab):
    # cf_status exact <-> standard_name string; else null. (Schema enforces; assert too.)
    for key, e in vocab["quantities"].items():
        if e["cf_status"] == "exact":
            assert isinstance(e["standard_name"], str) and e["standard_name"]
        else:
            assert e["standard_name"] is None, key


def test_validator_rejects_bad_vocab(schema):
    # Regression: a validator that never fails is useless. Feed known-bad entries.
    bad = {
        "version": "0.1",
        "cf_standard_name_table": "v94",
        "quantities": {
            "MHT": {
                "name": "WRONG",  # name != key
                "quantity": "MHT",
                "kind": "heat_transport",
                "long_name": "x",
                "definition": "x",
                "cf_status": "exact",
                "standard_name": "not_a_real_cf_name_xyz",
                "units": "petawatt",
                "sign_convention": "Positive northward.",
                "since": "0.1",
                "status": "current",
            }
        },
    }
    assert V.name_key_errors(bad) == [
        "name-key: quantity 'MHT' has name 'WRONG' (must equal key)"
    ]


def test_inventory_builds():
    inv = inventory.build_inventory()
    assert len(inv) > 50
    assert "MOC" in inv and "MHT" in inv


def _cf_table():
    try:
        return V.resolve_cf_table(None)
    except FileNotFoundError:
        return None


@pytest.mark.skipif(_cf_table() is None, reason="CF standard-name table not available")
def test_full_validation_passes():
    problems = V.validate(VOCAB, SCHEMA, _cf_table())
    assert problems == [], "amocvocab.yml failed full validation:\n" + "\n".join(
        problems
    )
