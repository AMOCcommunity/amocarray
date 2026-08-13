# Changelog

All notable changes to AMOCatlas will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.4.0] - 2026-08-13

### Added
- New reader for the AXMOC 22.5°S and 34.5°S arrays (#142)
- Schema validation for array metadata YAML files (`array_schema.json`), enforced in CI (#171)
- Download provenance: each downloaded file now gets a `<name>.provenance.json` sidecar recording the source URL, download time, byte size, SHA-256, and server ETag/Last-Modified, plus a `read_provenance()` accessor (#175)
- Comprehensive test cases for the FBC (Faroe Bank Channel) and NOAC 47°N readers, and this CHANGELOG

### Changed
- Downloads are now atomic (streamed to a `.part` file and renamed on completion) and use a connect/read timeout, so an interrupted or stalled download can no longer leave a truncated file in the cache (#175)
- Contributor handling: single-contributor datasets are handled correctly and a genuine ORCID is never overwritten by a registry placeholder (#172)
- License metadata normalised toward SPDX identifiers: `fw2015` `CC-BY 4.0` → `CC-BY-4.0`, `mocha26n` `ODC-By` → `ODC-By-1.0`, and `fbc` `CC0-1.0` → `CC-BY-4.0` following the providers' updated Zenodo record
- Documentation deploy runs offline (notebooks are copied, not executed) and `gh-pages` is force-orphaned each deploy to stop history bloat (#174)
- Repository history rewritten to remove large data files committed in the past (fresh-clone size reduced from ~162 MB to ~24 MB)
- Dependency and CI maintenance: bumped xarray, pandas, matplotlib, jinja2, sphinx and other dev/CI dependencies, and added Dependabot (#144–#168)

### Fixed
- TIME coordinate converter now honours the declared epoch and units (e.g. `days since 1950-01-01` decodes to 1950, not 1970); unrecognised units warn instead of silently assuming 1970; and the output `units` attribute is a valid UDUNITS string rather than the numpy dtype name `datetime64[ns]` (#175)
- Internal working structures (`files`, `variable_mapping`, `original_variable_metadata`) are stripped from output attributes so standardised datasets serialise to netCDF without error (#175)
- Metadata conflict resolution corrected, and the metadata drift surfaced by the new schema validation fixed (#171)
- Small metadata updates across several arrays (#143)
- Fixed `__version__` import in `__init__.py` for proper package version access

## [0.3.1] - 2026-06-07

### Added
- New reader for Le Bras AMOC at 35°N (#139)
- New Sanchez-Franks 2021 Reader (#137) 
- New NAC reader (#134)
- Report generation functionality (#140)

### Updated
- Updated FBC transport with new location and extended timeseries (#133)
- Updated metadata for Zheng2024 (#136)
- Updated Zheng2024 plot to 2D (#135)

### Fixed
- Fixed convert lowercase URL into uppercase when case sensitive (#132)
- Fixed standardized sigma coords on RAPID to be <1000 (#126)

## [0.3.0] - 2026-02-10

### Added
- Registry for ORCID/EDMO with contributor alignment and dedupe (#106)
- Report generation of standardised datasets (#105)

### Fixed
- Addressed linting issues (#108)

## [0.2.0] - 2026-02-04

### Added
- New intuitive API (`amocatlas.read` namespace)
- Automatic data standardization
- Enhanced metadata management system
- Comprehensive documentation and reports

### Changed
- Legacy API (`load_dataset`, `load_sample_dataset`) marked as deprecated
- Improved package architecture with modular data sources

## [0.1.1] - 2025-09-26

### Fixed
- Bug fixes and minor improvements

## [0.1.0] - 2025-09-26

### Added
- Initial stable release
- Basic data loading functionality for major AMOC arrays
- Core plotting and analysis tools

## [0.0.4] - 2025-07-06

### Added
- Early development version
- Basic reader implementations

---

### Legend

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes

### Release Process

1. Create a new version section above "Unreleased"
2. Move items from "Unreleased" to the new version section
3. Add release date in YYYY-MM-DD format
4. Create git tag with format `v{version}` (e.g., `v0.3.1`)
5. GitHub Actions will automatically publish to PyPI

### Contributing

When adding changes, please:
1. Add new entries under the "Unreleased" section
2. Use the appropriate category (Added, Changed, Fixed, etc.)
3. Include PR numbers in parentheses when applicable
4. Keep descriptions clear and user-focused