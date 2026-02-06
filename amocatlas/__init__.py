"""AMOCatlas: Atlantic Meridional Overturning Circulation Data Access.

AMOCatlas provides unified access to data from major AMOC observing arrays
including RAPID, OSNAP, MOVE, SAMBA, and others. The package standardizes
data formats, provides analysis tools, and enables consistent visualization
across different monitoring systems.

Key Features:
- Unified data loading interface for multiple AMOC arrays
- Automatic data download and caching
- Standardized metadata and data formats
- Visualization tools including PyGMT publication figures
- Analysis functions for filtering and processing time series

Basic Usage:
    >>> from amocatlas import read
    >>> data = read.rapid()                    # Single transport dataset  
    >>> osnap = read.osnap(version="2025")     # Latest OSNAP data
    >>> all_data = read.rapid(all_files=True)  # All RAPID files as list
    
    # Legacy API (still supported):
    >>> from amocatlas import readers  
    >>> datasets = readers.load_dataset("rapid")
    >>> sample_data = readers.load_sample_dataset("osnap")
"""

# Import core modules to make them available at package level
from . import (
    readers,
    read,  # New intuitive API namespace
    plotters,
    standardise,
    utilities,
    tools,
    logger,
    writers,
    convert,
    compliance_checker,
    reader_utils,
    data_sources,  # New data sources package
)

# Version information
# from ._version import __version__

__all__ = [
    "readers",
    "read",
    "plotters", 
    "standardise",
    "utilities",
    "tools",
    "logger",
    "writers",
    "convert",
    "compliance_checker",
    "reader_utils",
    "data_sources",
    "__version__",
]
