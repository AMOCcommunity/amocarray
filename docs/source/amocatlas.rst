:mod:`amocatlas API`
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   read
   readers
   data_sources
   plotters
   writers
   tools
   standardise
   utilities

Load and process transport estimates from major AMOC observing arrays.

New Intuitive API (v0.2.0+)
============================

The recommended API that returns standardized, analysis-ready data by default.

.. automodule:: amocatlas.read
   :members:
   :undoc-members:

readers (Legacy API)
====================

Legacy API that returns raw data. Still supported for backwards compatibility.

.. automodule:: amocatlas.readers
   :members:
   :undoc-members:

data_sources
============

Individual data source readers organized by array/dataset.

.. automodule:: amocatlas.data_sources
   :members:
   :undoc-members:

standardise
===========
Functions to apply naming conventions, units, and metadata standards to datasets.

.. automodule:: amocatlas.standardise
   :members:
   :undoc-members:

plotters
========
Tools for visualising AMOC time series and transport data.

.. automodule:: amocatlas.plotters
   :members:
   :undoc-members:

writers
=======
.. automodule:: amocatlas.writers
   :members:
   :undoc-members:

tools
=====
Helper functions for data manipulation, unit conversion, and clean-up.

.. automodule:: amocatlas.tools
   :members:
   :undoc-members:

utilities
=========
Shared utilities for downloading, reading, and parsing data files.

.. automodule:: amocatlas.utilities
   :members:
   :undoc-members:
