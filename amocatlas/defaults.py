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
    "National Oceanography Centre,UK": "National Oceanography Centre (Southampton)",
    "National Oceanography Centre, UK": "National Oceanography Centre (Southampton)",
    # Add more exact string fixes here as needed
    "Multiple contributing institutions (US, UK, Germany, Netherlands, Canada, France, China)": "Multiple contributing institutions",
    "Georgia Institute of Technology, USA": "Georgia Institute of Technology",
    "National Oceanography Centre at Southampton, UK": "National Oceanography Centre (Southampton)",
    "Woods Hole Oceanographic Institution, USA": "Woods Hole Oceanographic Institution",
    "Scottish Association for Marine Science, UK": "Scottish Association for Marine Science",
    "Royal Netherlands Institute for Sea Research and Utrecht University, Netherlands": "Royal Netherlands Institute for Sea Research",
    "Memorial University, Canada": "Memorial University of Newfoundland",
    "Fisheries and Oceans Canada Northwest Atlantic Fisheries Centre and Institute of Ocean Sciences, Canada": "Fisheries and Oceans Canada, Northwest Atlantic Fisheries Centre, Institute of Ocean Sciences",
    "Scripps Institution of Oceanography, UCSD, USA": "Scripps Institution of Oceanography",
    "University of Miami, USA": "Rosenstiel School of Marine and Atmospheric Science , University of Miami",
    "GEOMAR Helmholtz Centre for Ocean Research Kiel, Germany": "Helmholtz Centre for Ocean Research Kiel (GEOMAR)",
    "Xiamen University, China": "Xiamen University, State Key Laboratory of Marine Environmental Science",
    "University of South Florida, USA": "University of South Florida",
    "Bedford Institute of Oceanography, Canada": "Bedford Institute of Oceanography",
    "Hafrannsóknastofnun / Marine and Freshwater Research Institute (Reykjavik, Iceland)": "Marine and Freshwater Research Institute",
    "University of Hamburg, Institute of Oceanography": "University of Hamburg (IfM)",
    "University of Hamburg": "University of Hamburg (IfM)",
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

# Valid contributor roles from NERC G04 vocabulary
# Reference: https://vocab.nerc.ac.uk/collection/G04/current/
NERC_G04_ROLES = [
    "author",
    "coAuthor",
    "collaborator",
    "contributor",
    "custodian",
    "distributor",
    "editor",
    "funder",
    "mediator",
    "originator",
    "owner",
    "pointOfContact",
    "principalInvestigator",
    "processor",
    "publisher",
    "resourceProvider",
    "rightsHolder",
    "sponsor",
    "stakeholder",
    "user",
]

# Role mappings for contributor consolidation and legacy field mapping
CONTRIBUTOR_ROLE_MAP = {
    # Map legacy creator fields to NERC G04 'originator'
    "creator_name": "originator",
    "creator": "originator",
    "created_by": "originator",
    # Map principal investigator fields
    "principal_investigator": "principalInvestigator",
    "PI": "principalInvestigator",
    # Map publisher fields
    "publisher_name": "publisher",
    "publisher": "publisher",
    # Generic contributor
    "contributor_name": "contributor",
    "contributor": "contributor",
}

# Available AMOC observing arrays and datasets
# Used consistently across report generation, documentation, and other modules
ARRAY_NAMES = [
    "rapid",  # RAPID 26°N array
    "move",  # MOVE 16°N array
    "osnap",  # OSNAP Subpolar North Atlantic
    "samba",  # SAMBA 34.5°S array
    "fw2015",  # Frajka-Williams 2015 altimetry estimates
    "mocha",  # RAPID/MOCHA heat transport at 26.5°N
    "arcticgateway",  # Pan-Arctic Gateway transports
    "dso",  # Denmark Strait Overflow
    "fbc",  # Faroe Bank Channel overflow
    "calafat2025",  # Bayesian Atlantic meridional heat transport
    "zheng2024",  # Observation-based Atlantic meridional freshwater transport
    "wh41n",  # Woods Hole 41°N array
    "noac47n",  # NOAC 47°N array (North Atlantic Ocean Current)
    "nac",  # North Atlantic Current
    "sf2021",  # Sanchez-Franks 2021 satellite reconstruction of AMOC transport at 26°N
    "lebras35n",  # Lebras 2023 AMOC transport at 35°N
    "axmoc22s",  # AXMOC and heat transport from sustained in situ observations at 22.5°S
    "axmoc34s",  # AXMOC, heat and freshwater transport from sustained in situ observations 34.5°S
]

# Mapping from array names to their full descriptions
ARRAY_DESCRIPTIONS = {
    "rapid": "RAPID 26°N array - Longest-running basin-wide monitoring since 2004",
    "move": "MOVE 16°N array - Tropical Atlantic monitoring west of Mid-Atlantic Ridge",
    "osnap": "OSNAP - Subpolar North Atlantic monitoring array",
    "samba": "SAMBA 34.5°S array - South Atlantic monitoring",
    "fw2015": "FW2015 - Altimetry-based transport estimates at 26°N",
    "mocha": "RAPID/MOCHA - Heat transport estimates from 26°N",
    "arcticgateway": "Arctic Gateway - Pan-Arctic gateway transports since 2004",
    "dso": "DSO - Denmark Strait overflow transport monitoring",
    "fbc": "FBC - Faroe Bank Channel overflow transport monitoring",
    "calafat2025": "CALAFAT2025 - Bayesian estimates of Atlantic meridional heat transport",
    "zheng2024": "ZHENG2024 - Observation-based Atlantic meridional freshwater transport",
    "wh41n": "WH41N - Woods Hole 41°N array transport monitoring",
    "noac47n": "NOAC 47°N - North Atlantic Ocean Current monitoring at 47°N",
    "nac": "North Atlantic Current - Transport estimate from satellite altimetry and float observations",
    "sf2021": "SF2021 - Sanchez-Franks 2021 satellite reconstruction of AMOC transport at 26°N",
    "lebras35n": "Le Bras 2023 - AMOC transport estimates at 35°N from satellite altimetry and in situ data",
    "axmoc22s": "AXMOC 22.5°S - AMOC and heat transport from sustained in situ observations at 22.5°S",
    "axmoc34s": "AXMOC 34.5°S - AMOC, heat and freshwater transport from sustained in situ observations at 34.5°S",
}

# Preferred units
PREFERRED_UNITS = {
    "temp": "degree_C",
    "psal": "1",
    "sa": "g kg-1",
    "density": "kg m-3",
    "pressure": "dbar",
    "velocity": "m s-1",
    "moc": "Sverdrup",
    "mht": "PW",
    "transport": "Sverdrup",
    "transport_per_unit_depth": "Sverdrup m-1",
    "latitude": "degree_north",
    "longitude": "degree_east",
    "latitudeS": "degree_south",
    "longitudeW": "degree_west",
    "unitless": "1",
    "length": "m",
    "length_km": "km",
    "time_second": "s",
    "time_day": "day",
    "time_minute": "min",
    "time_hour": "hr",
}
