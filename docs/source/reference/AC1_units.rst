Units
========================

This document summarizes unit definitions for AMOCatlas Format v0.1 (A0.1), based on `udunits2-base.xml` with AMOC-specific extensions.

- Check out `udunits <https://docs.unidata.ucar.edu/udunits/current/>`_.
- SI base units (XML) are `here <https://docs.unidata.ucar.edu/udunits/current/udunits2-base.xml>`_.
- Derived units (XML) are `here <https://docs.unidata.ucar.edu/udunits/current/udunits2-derived.xml>`_.


AMOCatlas Preferred Units
------------------------

The following table summarizes the preferred units for common AMOC variables:


.. list-table:: AMOCatlas Preferred Units
   :header-rows: 1
   :widths: 45 20 35

   * - Variable Type
     - AC1.0 Unit
     - Rationale
   * - Ocean volume transport
     - Sverdrup
     - Avoids Sv/sievert confusion
   * - Heat transport
     - PW
     - Appropriate scale for oceanic heat transport
   * - Temperature
     - degree_C
     - CF-compliant
   * - Salinity
     - PSU, g kg-1
     - Uppercase standard
   * - Density, potential density
     - kg m-3
     - Standard density unit
   * - Velocity
     - m s-1
     - Standard velocity unit, positive north or east
   * - Transport per unit depth
     - Sverdrup/m
     - Consistent with transport units
   * - Pressure
     - dbar
     - Standard oceanographic pressure unit
   * - Latitude
     - degree_north
     - CF-compliant, positive north
   * - Longitude
     - degree_east
     - CF-compliant, positive east
   * - Time
     - datetime64[ns]
     - Standard time representation in xarray and pandas
   * - Depth
     - m
     - Depth below sea surface, positive downwards



Mapping of Custom Conversions
-----------------------------

.. list-table:: AMOCatlas Unit Conversions
   :header-rows: 1
   :widths: 25 25 15 35

   * - Original Unit
     - Canonical Unit
     - Factor
     - Notes
   * - ``cm/s``, ``cm s-1``
     - ``m s-1``
     - 0.01
     - Velocity conversions
   * - ``S/m``
     - ``mS cm-1``
     - 0.1
     - Conductivity conversions
   * - ``Pa``, ``kPa``
     - ``dbar``
     - 1/10000, 1/10
     - Pressure conversions
   * - ``Celsius``, ``°C``
     - ``degree_C``
     - 1
     - Temperature unit normalization
   * - ``deg N``, ``deg E``
     - ``degrees_north``, ``degrees_east``
     - 1
     - Geographic coordinates (CF-compliant)
   * - ``psu``, ``PSU``
     - 1
     - 1
     - Practical salinity unit (unitless)
   * - ``W``, ``TW``, ``MW``
     - ``PW``
     - 1e-15, 1e-3, 1e-9
     - Heat transport scaling to petawatts
   * - ``meters``, ``m``
     - ``m``
     - 1 
     - 
   * - ``kg/m3`` 
     - ``kg m-3``
     - 1
     - Density conversions
   * - ``1e6 m3/s``
     - ``Sverdrup``
     - 1/1e6
     - Ocean volume transport (no abbreviation)
   * - ``W``, ``J``
     - ``watt``, ``joule``
     - base units
     - Energy and power base units

**Note:** Full "Sverdrup" spelling used to avoid confusion with "Sv" (sievert).


SI Unit Prefixes
------------------

Standard prefixes supported by UDUNITS-2 for scaling base and derived units.

.. tabularcolumns:: |p{3cm}|p{2cm}|L|

.. list-table:: SI Unit Prefixes
   :header-rows: 1
   :widths: 40 25 35

   * - Prefix
     - Symbol
     - Factor
   * - yotta
     - Y
     - 1e24
   * - zetta
     - Z
     - 1e21
   * - exa
     - E
     - 1e18
   * - peta
     - P
     - 1e15
   * - tera
     - T
     - 1e12
   * - giga
     - G
     - 1e9
   * - mega
     - M
     - 1e6
   * - kilo
     - k
     - 1e3
   * - hecto
     - h
     - 1e2
   * - deca
     - da
     - 1e1
   * - deci
     - d
     - 1e-1
   * - centi
     - c
     - 1e-2
   * - milli
     - m
     - 1e-3
   * - micro
     - µ (u)
     - 1e-6
   * - nano
     - n
     - 1e-9
   * - pico
     - p
     - 1e-12
   * - femto
     - f
     - 1e-15
   * - atto
     - a
     - 1e-18
   * - zepto
     - z
     - 1e-21
   * - yocto
     - y
     - 1e-24

Notes:

- Prefixes can be applied to compatible base/derived units (e.g., kW, cm, µS/cm).
- `µ` is often typed as `u` in ASCII-only environments.
