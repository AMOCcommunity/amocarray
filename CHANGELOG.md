# Changelog

All notable changes to AMOCatlas will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Fixed `__version__` import in `__init__.py` for proper package version access
- Enhanced test coverage for `fbc.py` and `noac47n.py` modules

### Added
- Comprehensive test cases for FBC (Faroe Bank Channel) data reader
- Comprehensive test cases for NOAC 47°N array data reader
- CHANGELOG.md file for tracking project changes

## [0.3.0] - YYYY-MM-DD

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

## [0.2.0] - YYYY-MM-DD

### Added
- New intuitive API (`amocatlas.read` namespace)
- Automatic data standardization
- Enhanced metadata management system
- Comprehensive documentation and reports

### Changed
- Legacy API (`load_dataset`, `load_sample_dataset`) marked as deprecated
- Improved package architecture with modular data sources

## [0.1.1] - YYYY-MM-DD

### Fixed
- Bug fixes and minor improvements

## [0.1.0] - YYYY-MM-DD

### Added
- Initial stable release
- Basic data loading functionality for major AMOC arrays
- Core plotting and analysis tools

## [0.0.4] - YYYY-MM-DD

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