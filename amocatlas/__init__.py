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
    >>> from amocatlas import readers
    >>> datasets = readers.load_dataset("rapid")
    >>> sample_data = readers.load_sample_dataset("osnap")
"""
