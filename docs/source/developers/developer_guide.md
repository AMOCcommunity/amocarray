# Developer Guide for AMOCatlas

Welcome to the AMOCatlas Developer Guide! This comprehensive guide will help you contribute effectively to the project, whether you're fixing bugs, adding new data readers, or improving documentation.

**Quick Navigation:**
- [Quickstart](#quickstart) - Get contributing in 5 minutes
- [Development Environment](#development-environment) - Setup and tools
- [Adding New Features](#adding-new-features) - Core contribution patterns
- [Code Standards](#code-standards) - Style and quality guidelines
- [Git Workflow](#git-workflow) - Fork, branch, and PR process
- [Testing](#testing) - Running tests locally and in CI
- [Specialized Guides](#specialized-guides) - Links to detailed references

**Related Documentation:**
- {doc}`git_beginners_guide` - Step-by-step Git workflow for beginners
- {doc}`housekeeping` - Maintenance tasks
- {doc}`actions` - CI/CD and release process

---

## Quickstart

Get started contributing in 5 minutes:

1. **Fork and clone** the repository:
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/amocatlas.git
   cd amocatlas
   ```

2. **Set up development environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-dev.txt
   pip install -e .
   ```

3. **Create a feature branch**:
   ```bash
   git checkout -b yourname-patch-1
   ```

4. **Make your changes** and test them:
   ```bash
   pytest  # Run tests
   pre-commit run --all-files  # Check formatting and linting
   ```

5. **Push and create a pull request**:
   ```bash
   git add .
   git commit -m "feat: your descriptive commit message"
   git push origin yourname-patch-1
   # Then create PR on GitHub
   ```

---

## Project Overview

AMOCatlas is a Python package for accessing and analyzing data from Atlantic Meridional Overturning Circulation (AMOC) observing arrays. The project aims to provide:

- **Unified data access** across multiple AMOC arrays (RAPID, OSNAP, MOVE, SAMBA, etc.)
- **Consistent data formats** and standardized metadata
- **Visualization tools** including publication-quality PyGMT figures
- **Analysis functions** for filtering, processing, and comparing datasets

### Core Architecture

```
amocatlas/
├── readers.py           # Main interface - load_dataset(), load_sample_dataset()
├── read_*.py           # Individual array readers (rapid, osnap, move, etc.)
├── utilities.py        # Shared functions (downloads, file handling)
├── tools.py            # Analysis functions (filtering, unit conversion)
├── plotters.py         # Visualization (matplotlib + PyGMT)
├── standardise.py      # Data format standardization
├── writers.py          # Data export functionality
└── logger.py           # Structured logging system
```

**Data Flow**: User calls `readers.load_dataset("rapid")` → `readers.py` routes to `read_rapid.py` → downloads data → standardizes format → returns xarray Dataset(s)

### Package-Level Imports

We import modules in `__init__.py` instead of at the top of each individual module:

```python
# In amocatlas/__init__.py
from . import (
    readers,
    plotters,
    compliance_checker,
    convert,
    # etc.
)
```

This means:
- Tests can do `from amocatlas import compliance_checker` 
- Without this, tests would need `from amocatlas.compliance_checker import ...`
- Modules like `plotters.HAS_PYGMT` are accessible because `plotters` is imported at package level

---

## Development Environment

### Prerequisites

- Python 3.9 or higher
- Git for version control
- Optional: PyGMT for publication figures (see installation notes below)

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AMOCcommunity/amocatlas.git
   cd amocatlas
   ```

2. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate && micromamba deactivate  # Safeguard if using micromamba
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements-dev.txt    # Includes runtime + development tools
   pip install -e .                       # Install amocatlas in editable mode
   ```

4. **Test your setup**:
   ```bash
   pytest                                 # Run tests
   python -c "import amocatlas; print('Success!')"
   ```

### Development Tools

- **Black**: Code formatting (88 character line length)
- **Ruff**: Linting and import sorting
- **pytest**: Testing framework with coverage reporting
- **pre-commit**: Automated code quality checks (run manually)
- **Sphinx**: Documentation generation

### PyGMT Installation Notes

PyGMT is an optional dependency for publication-quality figures but can be challenging to install:

```bash
# Try conda/mamba first (recommended):
conda install pygmt -c conda-forge

# Or pip (may require GMT to be installed separately):
pip install pygmt
```

See the [PyGMT installation guide](https://www.pygmt.org/latest/install.html) for platform-specific instructions.

---

## Adding New Features

### Adding a New Data Reader

This is the most common contribution type. Here's the step-by-step process:

1. **Create the reader module** `amocatlas/read_newarray.py`:
   ```python
   """Reader for NEWARRAY data."""
   
   import xarray as xr
   from amocatlas.utilities import download_file
   from amocatlas.logger import log_info
   
   def read_newarray(source: str = None, **kwargs) -> list[xr.Dataset]:
       """Read NEWARRAY data and return standardized datasets.
       
       Parameters
       ----------
       source : str, optional
           Data source URL or path.
       **kwargs
           Additional parameters passed to data loading.
           
       Returns
       -------
       list[xr.Dataset]
           List of standardized xarray datasets.
       """
       log_info("Loading NEWARRAY data...")
       # Implementation here
       return [dataset]
   ```

2. **Add to the main readers interface** in `amocatlas/readers.py`:
   ```python
   # Add to AVAILABLE_ARRAYS
   AVAILABLE_ARRAYS = {
       # ... existing arrays
       "newarray": "amocatlas.read_newarray",
   }
   ```

3. **Create tests** in `tests/test_read_newarray.py`:
   ```python
   import pytest
   from amocatlas.read_newarray import read_newarray
   
   def test_read_newarray():
       """Test basic functionality of NEWARRAY reader."""
       datasets = read_newarray()
       assert isinstance(datasets, list)
       assert len(datasets) > 0
   ```

4. **Document the original format** in `docs/source/format_orig_newarray.rst`:
   ```rst
   NEWARRAY Original Format
   ========================
   
   Description of the native NEWARRAY data format, including:
   - File structure and naming conventions
   - Variable names and units in original format
   - Metadata structure
   - Any format-specific considerations
   ```

5. **Add sample data** (if needed) and update other documentation.

### Adding Visualization Functions

Add to `amocatlas/plotters.py`. Choose between matplotlib (default) or PyGMT (publication quality):

```python
def plot_new_visualization(data, **kwargs):
    """Create a new type of visualization.
    
    Parameters
    ----------
    data : pandas.DataFrame or xarray.Dataset
        Input data to plot.
    **kwargs
        Plotting options.
        
    Returns
    -------
    matplotlib.figure.Figure or pygmt.Figure
        Generated plot.
    """
    # Implementation
    return fig
```

For PyGMT functions, include the availability check:
```python
def plot_new_pygmt_viz(data, **kwargs):
    """Create publication-quality plot using PyGMT."""
    _check_pygmt()  # This function handles missing PyGMT gracefully
    # Implementation
```

---

## Code Standards

### Python Style

- **Type hints**: Use for all function parameters and return values
- **Docstrings**: NumPy-style docstrings for all public functions
- **Naming**: snake_case for functions and variables, ALL_CAPS for xarray variables
- **Line length**: 88 characters (Black default)
- **Import order**: Standard library → Third party → Local imports (handled by Ruff)

### Example Function:
```python
def convert_units_var(
    var_values: xr.DataArray,
    current_unit: str,
    new_unit: str,
    unit_conversion: dict = None,
) -> xr.DataArray:
    """Convert variable values from one unit to another.

    Parameters
    ----------
    var_values : xr.DataArray
        The numerical values to convert.
    current_unit : str
        Unit of the original values.
    new_unit : str
        Desired unit for the output values.
    unit_conversion : dict, optional
        Dictionary containing conversion factors between units.

    Returns
    -------
    xr.DataArray
        Converted values in the desired unit.
    """
    # Implementation
    return converted_values
```

### Data Standards

- **xarray variables**: ALL_CAPS (e.g., `TRANSPORT`, `TIME`, `DEPTH`)
- **Attributes**: lowercase_with_underscores following OceanGliders OG1 format
- **Units**: Always include units in variable attributes, never in variable names
- **Missing values**: Handle NaN values consistently across functions

### Quality Checks

Run these before committing:
```bash
black amocatlas/ tests/           # Format code
ruff check amocatlas/ tests/      # Lint code  
pytest --cov=amocatlas           # Run tests with coverage
pre-commit run --all-files       # Run all quality checks
```

---

## Git Workflow

### Basic Workflow

1. **Keep your fork synced**:
   ```bash
   # Add upstream remote (one time only)
   git remote add upstream https://github.com/AMOCcommunity/amocatlas.git
   
   # Sync your fork
   git checkout main
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```

2. **Create feature branches**:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b yourname-patch-1  # Or descriptive name like: fix-osnap-metadata
   ```

3. **Make commits with clear messages**:
   ```bash
   git add .
   git commit -m "feat: add support for NEWARRAY dataset"
   # or
   git commit -m "fix: handle missing timestamps in RAPID data"
   ```

### Commit Message Format

Use conventional commits for consistency:

```
[type]: brief description of change

Types:
- feat: new feature
- fix: bug fix  
- docs: documentation changes
- style: formatting changes (no logic change)
- refactor: code restructuring (no behavior change)
- test: adding or updating tests
- chore: maintenance tasks
```

### Pull Request Process

1. **Push your branch**:
   ```bash
   git push origin yourname-patch-1
   ```

2. **Create PR on GitHub** targeting `AMOCcommunity/amocatlas:main`

3. **Address feedback** and update your branch as needed

4. **Merge** once approved (you can merge your own PR after approval)

---

## Testing

### Running Tests Locally

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=amocatlas --cov-report term-missing

# Run specific test file
pytest tests/test_readers.py

# Run specific test
pytest tests/test_readers.py::test_load_sample_dataset_rapid
```

### Writing Tests

Place tests in `tests/` directory following the naming convention `test_*.py`:

```python
import pytest
import numpy as np
from amocatlas import readers

def test_load_sample_dataset():
    """Test that sample datasets load correctly."""
    ds = readers.load_sample_dataset("rapid")
    assert ds is not None
    assert "TRANSPORT" in ds.variables

def test_data_processing():
    """Test data processing functions."""
    # Use sample data for testing
    data = np.array([1, 2, 3, 4, 5])
    result = your_function(data)
    expected = np.array([2, 4, 6, 8, 10])
    np.testing.assert_array_equal(result, expected)
```

### GitHub Actions CI

Tests run automatically on:
- Pull requests
- Pushes to main branch

The CI tests on multiple platforms (Windows, macOS, Linux) and Python versions. Check the "Actions" tab on GitHub to see test results.

### Pre-commit Checks

Before submitting PRs, ensure these pass:
```bash
pre-commit run --all-files
```

This runs:
- Black code formatting
- Ruff linting and import sorting  
- Basic pytest tests (on modified files)

---

## PyGMT Development

*Note: PyGMT development is advanced and not expected for most contributors.*

PyGMT functions in `amocatlas/plotters.py` follow these patterns:

- All PyGMT functions include `_check_pygmt()` for graceful fallback
- Functions return `pygmt.Figure` objects
- Include AMOCatlas timestamp: `_add_amocatlas_timestamp(fig)`
- Handle optional dependency gracefully with informative error messages

For detailed PyGMT development, see the existing PyGMT functions in `plotters.py` and refer to [PyGMT documentation](https://www.pygmt.org/).

---

## Troubleshooting

### Common Issues

**Pre-commit not running?**
```bash
pre-commit run --all-files  # Run manually
```

**Tests failing locally but passing in CI?**
- Check your virtual environment is activated
- Ensure you have the latest `requirements-dev.txt` installed

**Import errors after installing in editable mode?**
```bash
pip install -e . --force-reinstall
```

**PyGMT installation issues?**
- Try conda/mamba: `conda install pygmt -c conda-forge`
- Check [PyGMT installation guide](https://www.pygmt.org/latest/install.html)
- PyGMT is optional - all other functionality works without it

**VSCode not recognizing virtual environment?**
- Ensure Python interpreter is set to `./venv/bin/python`
- Reload VSCode window after activating environment

---

## Specialized Guides

For detailed information on specific topics, see these dedicated guides:

- {doc}`git_beginners_guide` - Step-by-step Git workflow with screenshots for beginners
- {doc}`housekeeping` - Maintenance and dependency management
- {doc}`actions` - CI/CD workflows and release process

---

## Resources

- [AMOCatlas Documentation](https://amoccommunity.github.io/amocatlas/)
- [GitHub Repository](https://github.com/AMOCcommunity/amocatlas)
- [Issue Tracker](https://github.com/AMOCcommunity/amocatlas/issues)
- [AMOC Community Project](https://www.amoccommunity.org/)

---

*This developer guide incorporates best practices from the Python scientific computing community and is designed to grow with the project.*