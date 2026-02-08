About 
===============

**What is this?**

AMOCatlas is a Python package for loading data from Atlantic Meridional Overturning Circulation (AMOC) observing arrays. It gives you a simple way to access data from different programmes around the Atlantic.

**Why AMOC?**

The Atlantic Meridional Overturning Circulation moves warm water north and cold water south in the Atlantic Ocean. It's important for climate - think of it as a giant conveyor belt that helps regulate temperatures in Europe and beyond.

Scientists monitor this circulation at several locations using moorings and other instruments. AMOCatlas makes it easier to work with data from these monitoring arrays.

**What data sources are included?**

* **RAPID (26°N)** - The longest-running basin-wide array, monitoring since 2004
* **MOVE (16°N)** - Tropical Atlantic monitoring, west of the Mid-Atlantic Ridge
* **OSNAP (Subpolar)** - Covers the subpolar North Atlantic
* **SAMBA (34.5°S)** - South Atlantic monitoring
* **41°N** - Uses Argo float data and altimetry
* **47°N** - North Atlantic Ocean Current monitoring
* **DSO** - Denmark Strait overflow
* **FBC** - Faroe Bank Channel overflow transport monitoring
* **Arctic Gateway** - Pan-Arctic gateway transports
* **RAPID/MOCHA** - Heat transport estimates from 26°N
* **FW2015** - Altimetry-based transport estimates at 26°N
* **CALAFAT2025** - Bayesian estimates of Atlantic meridional heat transport
* **ZHENG2024** - Observation-based Atlantic meridional freshwater transport

**What can you do with it?**

* Load data from any array of the above arrays (or measurement methods) with just a few lines of code
* Compare data across different locations
* Make plots with consistent styling
* Access both raw datasets (with original variable names) and standardised datasets (for ease of use between different sources).
* Get logs of what data was downloaded and processed

The package handles downloading, caching, and organizing the data so you can focus on the science.  Note that if the web-based locations of the original datasets change, that links may break.  Please then raise an issue (see below) or try a fix yourself (see developer guide).

Installation
============

**Quick Install**

To install the latest released version from PyPI:

.. code-block:: bash

    python -m pip install amocatlas

This allows you to import the package into a Python file or notebook with:

.. code-block:: python

    import amocatlas

**Install for Contributing**

To install a local, development version for contributing, clone the repository and run:

.. code-block:: bash

    git clone https://github.com/AMOCcommunity/amocatlas.git
    cd amocatlas
    pip install -r requirements-dev.txt
    pip install -e .

This installs ``amocatlas`` locally. The ``-e`` ensures that any edits you make in the files will be picked up by scripts that import functions from ``amocatlas``. The ``requirements-dev.txt`` includes additional Python packages needed for development, including building documentation, running tests, and code linting.

You can run the example Jupyter notebook by launching JupyterLab with ``jupyter-lab`` and navigating to the ``notebooks`` directory, or in VS Code or other Python GUI.

**Testing**

All new functions should include tests. You can run tests locally and generate a coverage report with:

.. code-block:: bash

    pytest --cov=amocatlas --cov-report term-missing tests/

This shows what lines of a module (e.g., ``amocatlas/read.py``) are not covered by existing tests (located in ``tests/``). Try to ensure that all lines of your contribution are covered in the tests.

See also the `Developers Guide <developer_guide.html>`_ for coding conventions, automatic GitHub Actions triggered on pull requests, and example Git workflows.

Getting Started
===============

The quickest way to try it out:

.. code-block:: python

    from amocatlas import read

    # Load standardized data ready for analysis
    ds = read.rapid()
    print(ds)

Check out the demo notebook for more examples.

**Need help?**

* Full documentation: https://amoccommunity.github.io/amocatlas
* Issues and questions: https://github.com/AMOCcommunity/amocatlas/issues
* Contributing: See our developer guide

.. note::
    This work has been carried out within the framework of the `EPOC project <http://epoc-eu.org>`_ funded by the European Union's Horizon Europe programme (grant agreement No 101059547), under call HORIZON-CL6-2021-CLIMATE01. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.
   