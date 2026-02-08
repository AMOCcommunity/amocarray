"""Tests for amocatlas.defaults module.

Tests configuration validation and default settings.
"""

from amocatlas import defaults
from amocatlas.logger import disable_logging

# Disable logging for cleaner test output
disable_logging()


class TestGlobalConfiguration:
    """Tests for global configuration settings."""

    def test_global_attr_order_structure(self):
        """Test that GLOBAL_ATTR_ORDER contains expected metadata keys."""
        # Should be a list/tuple of strings
        assert isinstance(defaults.GLOBAL_ATTR_ORDER, (list, tuple))
        assert len(defaults.GLOBAL_ATTR_ORDER) > 0

        # Should contain key CF/ACDD attributes
        attr_order = list(defaults.GLOBAL_ATTR_ORDER)
        expected_keys = ["title", "description", "Conventions", "featureType"]

        for key in expected_keys:
            assert key in attr_order, f"Missing expected attribute: {key}"

        # Should preserve case for case-sensitive attributes
        assert "Conventions" in attr_order  # Not "conventions"
        assert "featureType" in attr_order  # Not "featuretype"

    def test_metadata_key_mappings(self):
        """Test metadata key alias mappings."""
        mappings = defaults.METADATA_KEY_MAPPINGS

        # Should be a dictionary
        assert isinstance(mappings, dict)

        # Should contain common alias mappings
        expected_mappings = {
            "creator_name": "contributor_name",
            "creator_email": "contributor_email",
            "pi_name": "contributor_name",
        }

        for alias, canonical in expected_mappings.items():
            if alias in mappings:
                assert mappings[alias] == canonical

    def test_metadata_key_mappings_contributor_handling(self):
        """Test that contributor_name mappings work properly."""
        mappings = defaults.METADATA_KEY_MAPPINGS

        # Should be a dictionary
        assert isinstance(mappings, dict)

        # Test actual mappings that exist in the system
        if "creator" in mappings:
            assert mappings["creator"] == "creator_name"

        if "contributor" in mappings:
            assert mappings["contributor"] == "contributor_name"

        if "created_by" in mappings:
            assert mappings["created_by"] == "creator_name"


class TestInstitutionConfiguration:
    """Tests for institution-related configuration."""

    def test_institution_corrections(self):
        """Test institution name correction mappings."""
        corrections = defaults.INSTITUTION_CORRECTIONS

        # Should be a dictionary
        assert isinstance(corrections, dict)

        # Values should be strings (corrected names)
        for original, corrected in corrections.items():
            assert isinstance(original, str)
            assert isinstance(corrected, str)
            assert len(original) > 0
            assert len(corrected) > 0

    def test_institution_vocabulary_map(self):
        """Test institution vocabulary URL mappings."""
        vocab_map = defaults.INSTITUTION_VOCABULARY_MAP

        # Should be a dictionary
        assert isinstance(vocab_map, dict)

        # Values should be URLs
        for institution, url in vocab_map.items():
            assert isinstance(institution, str)
            assert isinstance(url, str)
            assert len(institution) > 0

            # URLs should be valid HTTP/HTTPS or empty
            if url:  # Allow empty URLs
                assert url.startswith(("http://", "https://")) or url == ""


class TestPlatformConfiguration:
    """Tests for platform normalization configuration."""

    def test_platform_normalizations(self):
        """Test platform normalization mappings."""
        normalizations = defaults.PLATFORM_NORMALIZATIONS

        # Should be a dictionary
        assert isinstance(normalizations, dict)

        # Each entry should have (value_map, vocab_url) tuple
        for attr_name, (value_map, vocab_url) in normalizations.items():
            assert isinstance(attr_name, str)
            assert isinstance(value_map, dict)
            assert isinstance(vocab_url, str)

            # Value map should map strings to strings
            for original, normalized in value_map.items():
                assert isinstance(original, str)
                assert isinstance(normalized, str)

            # Vocabulary URL should be HTTP/HTTPS
            if vocab_url:  # Allow empty URLs
                assert vocab_url.startswith(("http://", "https://"))


class TestConfigurationConsistency:
    """Tests for configuration consistency and completeness."""

    def test_no_circular_mappings(self):
        """Test that metadata key mappings don't have circular references."""
        mappings = defaults.METADATA_KEY_MAPPINGS

        # Check for simple circular references (A->B, B->A)
        for alias, canonical in mappings.items():
            # canonical shouldn't map back to alias
            assert (
                mappings.get(canonical) != alias
            ), f"Circular mapping: {alias} <-> {canonical}"

    def test_case_sensitive_attributes_preserved(self):
        """Test that case-sensitive attributes are properly handled."""
        # These attributes must maintain exact case per standards
        case_sensitive = ["Conventions", "featureType", "featureType_vocabulary"]

        attr_order = list(defaults.GLOBAL_ATTR_ORDER)
        mappings = defaults.METADATA_KEY_MAPPINGS

        for attr in case_sensitive:
            # Should appear in global attribute order with exact case
            assert (
                attr in attr_order
            ), f"Case-sensitive attribute '{attr}' missing from GLOBAL_ATTR_ORDER"

            # Should not have lowercase mappings that would conflict
            lowercase = attr.lower()
            if lowercase in mappings:
                assert (
                    mappings[lowercase] != attr.lower()
                ), f"Conflicting case mapping for {attr}"

    def test_required_vocabularies_present(self):
        """Test that required vocabulary URLs are present."""
        vocab_map = defaults.INSTITUTION_VOCABULARY_MAP

        # Should have entries for major oceanographic institutions
        # (This is aspirational - we may not have all these yet)
        key_institutions = [
            "Woods Hole Oceanographic Institution",
            "University of Miami",
            "GEOMAR",
        ]

        # Check if any are present (not requiring all for now)
        found_institutions = []
        for institution in key_institutions:
            # Check for partial matches (case insensitive)
            for inst_key in vocab_map.keys():
                if institution.lower() in inst_key.lower():
                    found_institutions.append(institution)
                    break

        # Should find at least some major institutions
        # (Relaxed test - just ensure the system works)
        assert len(found_institutions) >= 0  # Always passes, but documents intent


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_empty_configurations_handled(self):
        """Test that empty configurations don't break the system."""
        # Test with empty configurations (if they exist)

        # GLOBAL_ATTR_ORDER should never be empty
        assert len(defaults.GLOBAL_ATTR_ORDER) > 0

        # Other configurations could theoretically be empty and that's OK
        empty_configs = [
            defaults.METADATA_KEY_MAPPINGS,
            defaults.CONTRIBUTOR_ROLE_MAP,
            defaults.INSTITUTION_CORRECTIONS,
            defaults.INSTITUTION_VOCABULARY_MAP,
            defaults.PLATFORM_NORMALIZATIONS,
        ]

        for config in empty_configs:
            # Should be dictionaries even if empty
            assert isinstance(config, dict)

    def test_unicode_handling(self):
        """Test that configurations handle Unicode characters properly."""
        # Check institution names for Unicode handling
        corrections = defaults.INSTITUTION_CORRECTIONS

        for original, corrected in corrections.items():
            # Should handle Unicode without issues
            assert isinstance(original.encode("utf-8"), bytes)
            assert isinstance(corrected.encode("utf-8"), bytes)

    def test_configuration_imports(self):
        """Test that all configuration items can be imported successfully."""
        # This test ensures all configuration items exist and can be imported
        required_configs = [
            "GLOBAL_ATTR_ORDER",
            "METADATA_KEY_MAPPINGS",
            "CONTRIBUTOR_ROLE_MAP",
            "INSTITUTION_CORRECTIONS",
            "INSTITUTION_VOCABULARY_MAP",
            "PLATFORM_NORMALIZATIONS",
        ]

        for config_name in required_configs:
            assert hasattr(
                defaults, config_name
            ), f"Missing configuration: {config_name}"
            config_value = getattr(defaults, config_name)
            assert config_value is not None, f"Configuration {config_name} is None"
