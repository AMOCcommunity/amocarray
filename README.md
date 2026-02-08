# AMOCatlas


[![PyPI version](https://img.shields.io/pypi/v/AMOCatlas.svg)](https://pypi.org/project/AMOCatlas/)
[![Python](https://img.shields.io/pypi/pyversions/AMOCatlas.svg)](https://pypi.org/project/AMOCatlas/)
[![License](https://img.shields.io/github/license/AMOCcommunity/amocatlas.svg)](LICENSE)

**Clean, modular loading of AMOC observing array datasets, with optional structured logging and metadata enrichment.**

AMOCatlas provides a unified system to access and process data from major Atlantic Meridional Overturning Circulation (AMOC) observing arrays. The Atlantic Meridional Overturning Circulation is a critical component of Earth's climate system, transporting heat northward in the Atlantic Ocean. This project enables researchers to easily access, analyze, and visualize data from key monitoring stations.

This is a work in progress, all contributions welcome!

## Table of Contents
- [Features](#features)
- [Supported Arrays](#supported-arrays)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Development](#development)
- [Funding & Support](#funding--support)
- [Acknowledgements](#acknowledgements)
- [Contributing](#contributing)

## Features

- 🌊 **Unified Data Access**: Single interface for multiple AMOC observing arrays
- 📊 **Automatic Data Download**: Intelligent caching system prevents redundant downloads
- 📝 **Structured Logging**: Per-dataset logging for reproducible workflows
- 🔍 **Metadata Enrichment**: Enhanced datasets with processing timestamps and source information
- 📈 **Visualization Tools**: Built-in plotting functions with consistent styling
- 🧪 **Sample Datasets**: Quick access to example data for testing and development

## Available Data Sources

| Data Source | Location | Description | Read Command |
|-------------|----------|-------------|--------------|
| **RAPID** | 26°N | Continuous monitoring since 2004 | `read.rapid()` |
| **MOCHA** | 26°N | Heat transport since 2004 | `read.mocha()` |
| **MOVE** | 16°N | Meridional heat transport | `read.move()` |
| **OSNAP** | Subpolar North Atlantic | Overturning circulation | `read.osnap()` |
| **SAMBA** | 34.5°S | South Atlantic MOC | `read.samba()` |
| **41°N Array** | 41°N | North Atlantic section | `read.wh41n()` |
| **NOAC 47°N** | 47°N | North Atlantic Ocean Current monitoring | `read.noac47n()` |
| **DSO** | Denmark Strait | Overflow monitoring | `read.dso()` |
| **FBC** | Faroe Bank Channel | Overflow transport monitoring | `read.fbc()` |
| **Arctic Gateway** | Arctic Ocean | Pan-Arctic gateway transports | `read.arcticgateway()` |
| **FW2015** | 26°N | Frajka-Williams 2015 satellite-cable dataset | `read.fw2015()` |
| **CALAFAT2025** | Atlantic | Bayesian estimates of Atlantic meridional heat transport | `read.calafat2025()` |
| **ZHENG2024** | Atlantic | Observation-based Atlantic meridional freshwater transport | `read.zheng2024()` |

## Installation

### From PyPI (Recommended)
```bash
pip install AMOCatlas
```

**Requirements**: Python ≥3.9, with numpy, pandas, xarray, and matplotlib.

### For Development
```bash
git clone https://github.com/AMOCcommunity/amocatlas.git
cd amocatlas
pip install -r requirements-dev.txt
pip install -e .
```

This installs amocatlas locally. The `-e` ensures that any edits you make in the files will be picked up by scripts that import functions from amocatlas.

## Quick Start

### Load Sample Data
```python
from amocatlas import read

# Load RAPID sample dataset (new API - recommended)
ds = read.rapid()
print(ds)

# Or use the legacy API
from amocatlas import readers
ds = readers.load_sample_dataset("rapid")
```

### Load Full Datasets
```python
from amocatlas import read

# Load complete dataset (downloads and caches data) - new API
ds = read.osnap()                          # Single standardized dataset
all_files = read.osnap(all_files=True)     # Get all files for array

# Or use the legacy API
from amocatlas import readers
datasets = readers.load_dataset("osnap")  # Returns list of raw datasets
```

A `*.log` file will be written to `logs/` by default.

Data will be cached in `~/.amocatlas_data/` unless you specify a custom location.

### API Features (v0.2.0+)

AMOCatlas provides **standardized, analysis-ready data by default** with the new `read` API:

**Key Benefits:**
- 🧹 **Clean Data**: Consistent variable names, metadata, and units
- 🚀 **Easy to Use**: Single function calls instead of complex workflows  
- 🔄 **Flexible**: Get raw data when needed with `raw=True`
- 📊 **Smart Defaults**: Automatically handles array-specific parameters

```python
from amocatlas import read

# Standard workflow - recommended for most users
rapid_data = read.rapid()              # Single standardized dataset
osnap_data = read.osnap()              # Automatically uses latest version
arctic_data = read.arcticgateway()     # Consistent across all arrays

# Advanced usage
all_rapid = read.rapid(all_files=True) # Get all files for an array
raw_data = read.rapid(raw=True)        # Original format for special cases
```

**Legacy API (still supported):**
```python
from amocatlas import readers
datasets = readers.load_dataset("rapid")  # Returns raw data as before
```

## Documentation

Documentation is available at [https://amoccommunity.github.io/amocatlas](https://amoccommunity.github.io/amocatlas/).

Check out the demo notebook `notebooks/demo.ipynb` for example functionality.

## Project Structure

```
amocatlas/
│
├── read.py                  # 🆕 Modern API namespace (read.rapid(), read.osnap(), etc.)
├── readers.py               # Legacy orchestrator for loading datasets
├── reader_utils.py          # Shared utilities for all data source readers
│
├── data_sources/            # 🆕 Organized data source readers
│   ├── rapid26n.py          # RAPID array (26°N)
│   ├── move16n.py           # MOVE array (16°N)
│   ├── osnap55n.py          # OSNAP array (Subpolar North Atlantic)
│   ├── samba34s.py          # SAMBA array (34.5°S)
│   ├── mocha26n.py          # MOCHA dataset (26°N)
│   ├── wh41n.py             # 41°N array
│   ├── dso.py               # DSO overflow
│   ├── fbc.py               # Faroe Bank Channel
│   ├── fw2015.py            # Frajka-Williams 2015 dataset
│   ├── arcticgateway.py     # Arctic Gateway transports
│   ├── calafat2025.py       # Calafat 2025 heat transport
│   ├── zheng2024.py         # Zheng 2024 freshwater transport
│   └── noac47n.py           # NOAC 47°N monitoring
│
├── metadata/                # 🆕 YAML metadata files for standardization
├── utilities.py             # Core utilities (downloads, parsing, validation)
├── logger.py                # Structured logging system
├── standardise.py           # Data standardization functions
├── plotters.py              # Visualization and plotting functions
├── tools.py                 # Analysis and calculation functions
├── writers.py               # Data export functionality
│
└── tests/                   # Comprehensive unit tests
```

## Development

### Running Tests
All new functions should include tests. You can run tests locally and generate a coverage report with:
```bash
pytest --cov=amocatlas --cov-report term-missing tests/
```

Try to ensure that all the lines of your contribution are covered in the tests.

### Generating Dataset Reports
AMOCatlas includes automated report generation for comprehensive dataset documentation:

```bash
# Generate reports for all supported arrays
python generate_report

# Generate report for a specific dataset
python generate_report --data_source rapid26n

# Generate reports with custom output directory
python generate_report --output_dir custom_reports/
```

Reports are generated as structured RST files in `docs/source/reports/` with:
- Dataset visualization plots
- Variable mapping tables (original → standardized names)
- Comprehensive metadata documentation
- Temporal coverage analysis
- Statistical summaries

### Code Quality
```bash
black amocatlas/ tests/          # Format code
ruff check amocatlas/ tests/     # Lint code
pre-commit run --all-files       # Run all hooks
```

### Working with Notebooks
You can run the example jupyter notebook by launching jupyterlab with `jupyter-lab` and navigating to the `notebooks` directory, or in VS Code or another python GUI.

### Documentation
To build the documentation locally you need to install a few extra requirements:

- Install `make` for your computer, e.g. on ubuntu with `sudo apt install make`
- Install the additional python requirements. Activate the environment you use for working with amocatlas, navigate to the top directory of this repo, then run `pip install -r requirements-dev.txt`

Once you have the extras installed, you can build the docs locally by navigating to the `docs/` directory and running `make clean html`. This command will create a directory called `build/` which contains the html files of the documentation. Open the file `docs/build/html/index.html` in your browser, and you will see the docs with your changes applied.

## Funding & Support

<div align="center">
  <img src="docs/source/_static/epoc-logo.jpg" alt="EPOC Logo" width="300"/>
</div>

This project is supported by the Horizon Europe project **EPOC - Explaining and Predicting the Ocean Conveyor** (Grant Agreement No. 101081012).

*Funded by the European Union. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.*


## Current Roadmap

- [ ] Improve test coverage for data sources with <40% coverage
- [ ] Add more comprehensive visualization function tests  
- [ ] Expand plotting capabilities with additional array-specific visualizations
- [ ] Performance optimization for large dataset handling
- [ ] Create summary table of variable names, standard_names, long_names and units across all datasets
- [ ] Create summary table of default units and formatting conventions used for standardization
- [ ] Document deviations from OceanSITES-1.5 standard and rationale for changes
- [ ] Enrich metadata with ORCID identifiers for contributors
- [ ] Enrich metadata with https://edmo.seadatanet.org identifiers for contributing institutions
- [ ] Create sample 3D plots for Arctic Gateway and Calafat2025 datasets

## Acknowledgements

The observing arrays and datasets accessed through AMOCatlas are supported by:

- **RAPID data**: The RAPID-MOC monitoring project is funded by the Natural Environment Research Council (UK). Data is freely available from [www.rapid.ac.uk](https://www.rapid.ac.uk/)

- **MOVE data**: The MOVE project is funded by the NOAA Climate Program Office under award NA15OAR4320071. Initial funding came from the German Bundesministerium für Bildung und Forschung. Data collection is carried out by Uwe Send and Matthias Lankhorst at Scripps Institution of Oceanography

- **OSNAP data**: OSNAP data were collected and made freely available by the OSNAP (Overturning in the Subpolar North Atlantic Program) project and all the national programs that contribute to it ([www.o-snap.org](https://www.o-snap.org)). Multiple contributing institutions from US, UK, Germany, Netherlands, Canada, France, and China

- **SAMBA data**: SAMBA data were collected and made freely available by the SAMOC international project and contributing national programs

- **MOCHA data**: Data from the RAPID-MOCHA program are funded by the U.S. National Science Foundation and U.K. Natural Environment Research Council

- **41°N data**: These data were collected and made freely available by the International Argo Program and the national programs that contribute to it. The Argo Program is part of the Global Ocean Observing System

- **DSO data**: Generated by Institution of Oceanography Hamburg and Marine and Freshwater Research Institute (Reykjavik, Iceland). Supported through funding from NACLIM (EU-FP7, grant 308299), RACE II, RACE-Synthese (German BMBF), Nordic WOCE, VEINS, MOEN, ASOF-W, NAClim, THOR, AtlantOS, and Blue Action

- **FW2015 data**: Based on Frajka-Williams, E. (2015), "Estimating the Atlantic overturning at 26°N using satellite altimetry and cable measurements"

Dataset access and processing via [AMOCatlas](https://github.com/AMOCcommunity/amocatlas).

## Contributing

All contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## PyGMT add-on

AMOCatlas includes support for creating publication-quality figures using PyGMT. The demo notebook `notebooks/amoc_paperfigs.ipynb` demonstrates how to generate figures similar to those in Frajka-Williams et al. (2019, 2023) papers, including filtered time series, component breakdowns, and multi-array comparisons.

**Note**: PyGMT can be challenging to install due to its dependency on GMT. See the [PyGMT installation guide](https://www.pygmt.org/latest/install.html) for platform-specific instructions. PyGMT is an optional dependency - all other AMOCatlas functionality works without it.

Example figures generated by the notebook:

**Multi-array AMOC comparison:**
<img src="docs/source/_static/paperfigs/amoc_multi_array.png" alt="Atlantic Meridional Overturning Circulation time series from four major observing arrays: OSNAP at subpolar latitudes (green), RAPID at 26°N (red), MOVE at 16°N (magenta), and SAMBA at 34.5°S (blue anomaly). Data spans 2000-2025 showing AMOC transport in Sverdrups and variability across different latitudes." width="600"/>

**Multi-array AMOC comparison (filtered):**
<img src="docs/source/_static/paperfigs/amoc_multi_array_filtered.png" alt="Low-pass filtered Atlantic Meridional Overturning Circulation time series using Tukey window filtering to highlight long-term trends. Shows OSNAP, RAPID, MOVE, and SAMBA MOC transport data with reduced high-frequency variability, revealing decadal-scale changes in ocean circulation strength from 2000-2025." width="600"/>

**Multi-array AMOC overlaid:**
<img src="docs/source/_static/paperfigs/amoc_multi_array_overlaid.png" alt="Overlaid Atlantic Meridional Overturning Circulation time series from multiple observing arrays plotted on the same coordinate system. OSNAP (green), RAPID 26°N (red), and MOVE 16°N (magenta) show MOC transport in Sverdrups, while SAMBA 34.5°S (blue) displays anomaly values, enabling direct comparison of AMOC variability across Atlantic latitudes." width="600"/>

**Historical AMOC (Bryden 2005):**
<img src="docs/source/_static/paperfigs/bryden2005_amoc.png" alt="Historical Atlantic Meridional Overturning Circulation estimates from Bryden et al. 2005 showing AMOC decline from 1957 to 2004. Red line and diamond markers indicate MOC transport measurements at 26°N, demonstrating significant weakening of Atlantic overturning circulation over five decades from 23 to 15 Sverdrups." width="400"/>

---

*For questions or support, please open an [issue](https://github.com/AMOCcommunity/amocatlas/issues) or check our [documentation](https://amoccommunity.github.io/amocatlas/).*