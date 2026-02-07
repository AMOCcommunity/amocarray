"""Default configurations and mappings for AMOCatlas standardization.

This module contains default values, mappings, and configurations used throughout
the AMOCatlas standardization process.
"""

# Canonical order of global attributes for dataset metadata
# Extracted from OG1.0 spec "## Global attributes"
GLOBAL_ATTR_ORDER = [
    # Dataset identification
    "title",
    "summary",
    "description",
    "program",
    "project",
    "source",
    "id",
    "naming_authority",
    # Legal and licensing
    "license",
    "acknowledgment",
    "citation",
    "doi",
    "uri",
    "references",
    "weblink",
    "distribution_statement",
    # Platform and methodology
    "platform",
    "platform_type",
    "platform_vocabulary",
    "platform_code",
    "wmo_platform_code",
    "processing_level",
    "data_product",
    # Site and network
    "site",
    "site_code",
    "site_vocabulary",
    "array",
    "network",
    "program_vocabulary",
    "internal_mission_identifier",
    # Geospatial and temporal coverage
    "start_date",
    "time_coverage_start",
    "time_coverage_end",
    "geospatial_lat_min",
    "geospatial_lat_max",
    "geospatial_lon_min",
    "geospatial_lon_max",
    "geospatial_vertical_min",
    "geospatial_vertical_max",
    "sea_name",
    # Contributors and attribution
    "creator_name",
    "creator_email",
    "creator_url",
    "creator_institution",
    "contributor_name",
    "contributor_role",
    "contributor_role_vocabulary",
    "contributor_url",
    "contributor_email",
    "contributor_id",
    "contributor_institution",
    "contributing_institutions",
    "contributing_institutions_vocabulary",
    "contributing_institutions_role",
    "contributing_institutions_role_vocabulary",
    "institution",
    "publisher_name",
    "publisher_email",
    "publisher_url",
    "publisher_institution",
    "publisher_type",
    # Technical metadata
    "Conventions",  # preserve exact case
    "CF_version",
    "ACDD_version",
    "standard_name_vocabulary",
    "ncei_template_version",
    "featureType",  # preserve exact case
    "featureType_vocabulary",
    "cdm_data_type",
    "data_type",
    # Data provenance
    "source_file",
    "source_path",
    "source_url",
    "date_created",
    "date_modified",
    "history",
    "processing_date",
    "processing_software",
    "processing_version",
    "processing_datasource",
    "product_version",
    "format_version",
    "variable_mapping",
    "original_variable_metadata",
    "applied_variable_mapping",
    # Keywords and quality control
    "keywords",
    "keywords_vocabulary",
    "rtqc_method",
    "rtqc_method_doi",
    # Links
    "data_url",
    "weblink",
    # Other
    "uuid",
    "update_interval",  # OceanSITES-1.5: use VOID if not regular
    "comment",
]

# Mapping of metadata key aliases to canonical ACDD-compliant names
# Used during metadata cleaning to normalize key names
METADATA_KEY_MAPPINGS = {
    "web_link": "weblink",
    "website": "weblink",
    "note": "comment",
    "acknowledgement": "acknowledgment",  # OceanSITES -> ACDD
    "data_policy": "distribution_statement",  # OSNAP -> ACDD
    "DOI": "doi",
    "reference": "references",
    "creator": "creator_name",
    "platform_type": "platform",
    "contributor": "contributor_name",
    "Institution": "institution",
    "Project": "project",
    "created_by": "creator_name",
    "principle_investigator": "principal_investigator",
    "principle_investigator_email": "principal_investigator_email",
    "creation_date": "date_created",
}

# Institution name corrections for known inconsistencies
INSTITUTION_CORRECTIONS = {
    "National Oceanography Centre,UK": "National Oceanography Centre (Southampton) (UK)",
    "National Oceanography Centre, UK": "National Oceanography Centre (Southampton) (UK)",
    # Add more exact string fixes here as needed
}

# Platform vocabulary normalization
PLATFORM_NORMALIZATIONS = {
    "platform": (
        {"Mooring array": "mooring"},
        "https://vocab.nerc.ac.uk/collection/L06/",
    ),
    "featureType": (
        {"timeSeries": "timeSeries"},
        "https://cfconventions.org/cf-conventions/v1.6.0/cf-conventions.html#_features_and_feature_types",
    ),
}

# Institution vocabulary mapping (for contributing_institutions_vocabulary)
INSTITUTION_VOCABULARY_MAP = {
    "national oceanography centre (southampton) (uk)": "https://edmo.seadatanet.org/report/17",
    "helmholtz centre for ocean research kiel (geomar)": "https://edmo.seadatanet.org/report/2947",
    "university of hamburg institute of oceanography (ifm)": "https://edmo.seadatanet.org/report/1156",
    "scripps institution of oceanography": "https://edmo.seadatanet.org/report/1390",
    "national aeronautics and space administration, jet propulsion laboratory (nasa jpl)": "https://edmo.seadatanet.org/report/1224",
    # Add more lower-cased, normalized keys here
}

# Role mappings for contributor consolidation
CONTRIBUTOR_ROLE_MAP = {
    "creator_name": "creator",
    "creator": "creator",
    "principal_investigator": "PI",
    "publisher_name": "publisher",
    "publisher": "publisher",
    "contributor_name": "",
    "contributor": "",
}
