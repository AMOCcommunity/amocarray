"""Tests for amocatlas.registry module.

Tests the registry lookup utilities for contributor and institution
standardization including fuzzy matching and ORCID/EDMO lookup.
"""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch, mock_open
import yaml

from amocatlas import registry
from amocatlas.logger import disable_logging

# Disable logging for cleaner test output
disable_logging()


@pytest.fixture
def sample_contributor_registry():
    """Sample contributor registry data for testing."""
    return {
        "contributors": {
            "0000-0001-1234-5678": {
                "name": "John Smith",
                "standard_name": "John Smith",
                "email": "john.smith@example.com",
                "name_variants": ["J. Smith", "Smith, John", "John Smith"],
            },
            "0000-0002-9876-5432": {
                "name": "Jane Doe",
                "standard_name": "Jane Doe",
                "email": "jane.doe@example.org",
                "name_variants": ["J. Doe", "Doe, Jane"],
            },
        }
    }


@pytest.fixture
def sample_institution_registry():
    """Sample institution registry data for testing."""
    return {
        "institutions": {
            "123": {
                "name": "University of Example",
                "standard_name": "University of Example",
                "edmo_id": "123",
                "name_variants": ["UoE", "Example University", "University of Example"],
            },
            "456": {
                "name": "Research Institute",
                "standard_name": "Research Institute",
                "edmo_id": "456",
                "name_variants": ["RI", "Res. Inst."],
            },
        }
    }


class TestLoadRegistries:
    """Test registry loading functions."""

    def test_load_contributor_registry_success(self, sample_contributor_registry):
        """Test successful loading of contributor registry."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(sample_contributor_registry, f)
            f.flush()

            registry_path = Path(f.name)
            result = registry.load_contributor_registry(registry_path)

            assert result == sample_contributor_registry
            assert "contributors" in result
            assert "0000-0001-1234-5678" in result["contributors"]

        # Cleanup
        registry_path.unlink()

    def test_load_contributor_registry_default_path(self):
        """Test loading with default path."""
        # Mock the default path and file reading
        mock_data = {"contributors": {"test": "data"}}

        with patch("builtins.open", mock_open(read_data=yaml.dump(mock_data))):
            with patch("amocatlas.registry.Path") as mock_path:
                mock_path.return_value.parent.__truediv__.return_value.__truediv__.return_value = Path(
                    "/fake/path"
                )

                result = registry.load_contributor_registry()
                assert result == mock_data

    def test_load_contributor_registry_file_not_found(self):
        """Test handling of missing registry file."""
        non_existent_path = Path("/non/existent/file.yml")

        # Function should return empty registry on file not found
        result = registry.load_contributor_registry(non_existent_path)
        assert result == {"contributors": {}}

    def test_load_institution_registry_success(self, sample_institution_registry):
        """Test successful loading of institution registry."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
            yaml.dump(sample_institution_registry, f)
            f.flush()

            registry_path = Path(f.name)
            result = registry.load_institution_registry(registry_path)

            assert result == sample_institution_registry
            assert "institutions" in result
            assert "123" in result["institutions"]

        # Cleanup
        registry_path.unlink()


class TestContributorLookup:
    """Test contributor lookup and matching functions."""

    def test_find_contributor_orcid_variant_match(self, sample_contributor_registry):
        """Test finding contributor ORCID with name variant match."""
        result = registry.find_contributor_orcid(
            "J. Smith", sample_contributor_registry
        )
        assert result is not None
        orcid, info = result
        assert orcid == "0000-0001-1234-5678"
        assert info["name"] == "John Smith"
        assert info["email"] == "john.smith@example.com"

    def test_find_contributor_orcid_case_insensitive(self, sample_contributor_registry):
        """Test finding contributor ORCID with case insensitive match."""
        result = registry.find_contributor_orcid(
            "john smith", sample_contributor_registry
        )
        assert result is not None
        orcid, info = result
        assert orcid == "0000-0001-1234-5678"
        assert info["name"] == "John Smith"

    def test_find_contributor_orcid_no_match(self, sample_contributor_registry):
        """Test finding contributor ORCID when no match found."""
        result = registry.find_contributor_orcid(
            "Unknown Person", sample_contributor_registry
        )
        assert result is None

    def test_find_contributor_orcid_empty_registry(self):
        """Test finding contributor ORCID with empty registry."""
        empty_registry = {"contributors": {}}
        result = registry.find_contributor_orcid("John Smith", empty_registry)
        assert result is None


class TestInstitutionLookup:
    """Test institution lookup and matching functions."""

    def test_find_institution_edmo_variant_match(self, sample_institution_registry):
        """Test finding institution EDMO with name variant match."""
        result = registry.find_institution_edmo("UoE", sample_institution_registry)
        assert result is not None
        edmo, info = result
        assert edmo == "123"
        assert info["name"] == "University of Example"

    def test_find_institution_edmo_case_insensitive(self, sample_institution_registry):
        """Test finding institution EDMO with case insensitive match."""
        result = registry.find_institution_edmo(
            "university of example", sample_institution_registry
        )
        assert result is not None
        edmo, info = result
        assert edmo == "123"
        assert info["name"] == "University of Example"

    def test_find_institution_edmo_no_match(self, sample_institution_registry):
        """Test finding institution EDMO when no match found."""
        result = registry.find_institution_edmo(
            "Unknown University", sample_institution_registry
        )
        assert result is None

    def test_find_institution_edmo_empty_registry(self):
        """Test finding institution EDMO with empty registry."""
        empty_registry = {"institutions": {}}
        result = registry.find_institution_edmo("University", empty_registry)
        assert result is None


class TestStandardization:
    """Test standardization functions."""

    def test_standardize_contributor_info_with_match(self, sample_contributor_registry):
        """Test contributor standardization when match is found."""
        input_names = ["J. Smith", "Unknown Person"]

        with patch("amocatlas.registry.load_contributor_registry") as mock_load:
            mock_load.return_value = sample_contributor_registry

            result = registry.standardize_contributor_info(input_names)

            assert result["names"] == ["John Smith", "Unknown Person"]
            assert result["orcids"] == ["0000-0001-1234-5678", ""]

    def test_standardize_contributor_info_no_match(self, sample_contributor_registry):
        """Test contributor standardization when no match is found."""
        input_names = ["Unknown Person", "Another Unknown"]

        with patch("amocatlas.registry.load_contributor_registry") as mock_load:
            mock_load.return_value = sample_contributor_registry

            result = registry.standardize_contributor_info(input_names)

            assert result["names"] == ["Unknown Person", "Another Unknown"]
            assert result["orcids"] == ["", ""]

    def test_standardize_institution_info_with_match(self, sample_institution_registry):
        """Test institution standardization when match is found."""
        input_names = ["UoE", "Unknown University"]

        with patch("amocatlas.registry.load_institution_registry") as mock_load:
            mock_load.return_value = sample_institution_registry

            result = registry.standardize_institution_info(input_names)

            assert result["names"] == ["University of Example", "Unknown University"]
            assert result["edmo_codes"] == ["123", ""]
            assert result["countries"] == ["", ""]

    def test_standardize_institution_info_no_match(self, sample_institution_registry):
        """Test institution standardization when no match is found."""
        input_names = ["Unknown University", "Another Unknown"]

        with patch("amocatlas.registry.load_institution_registry") as mock_load:
            mock_load.return_value = sample_institution_registry

            result = registry.standardize_institution_info(input_names)

            assert result["names"] == ["Unknown University", "Another Unknown"]
            assert result["edmo_codes"] == ["", ""]
            assert result["countries"] == ["", ""]


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_find_contributor_orcid_malformed_registry(self):
        """Test handling of malformed contributor registry."""
        malformed_registry = {"contributors": None}

        with pytest.raises((AttributeError, TypeError)):
            registry.find_contributor_orcid("John Smith", malformed_registry)

    def test_find_institution_edmo_malformed_registry(self):
        """Test handling of malformed institution registry."""
        malformed_registry = {"institutions": None}

        with pytest.raises((AttributeError, TypeError)):
            registry.find_institution_edmo("University", malformed_registry)

    def test_standardize_contributor_with_empty_list(self):
        """Test contributor standardization with empty list."""
        empty_list = []

        with patch("amocatlas.registry.load_contributor_registry") as mock_load:
            mock_load.return_value = {"contributors": {}}
            result = registry.standardize_contributor_info(empty_list)
            assert result == {"names": [], "orcids": []}

    def test_standardize_institution_with_empty_list(self):
        """Test institution standardization with empty list."""
        empty_list = []

        with patch("amocatlas.registry.load_institution_registry") as mock_load:
            mock_load.return_value = {"institutions": {}}
            result = registry.standardize_institution_info(empty_list)
            assert result == {"names": [], "edmo_codes": [], "countries": []}
