AMOCatlas Standards Overview
====================================

This document provides an overview of the AMOCatlas variable standards and documentation structure.

Variable Naming Framework
-------------------------

Variables are in uppercase with underscores for readability, using CF-1.8 standard names where possible.  Key patterns include:

Transport Variables (`TRANS_` prefix):
   - TRANS_EKMAN: Ekman transport component
   - TRANS_FC: Florida Current transport
   - TRANS_{depth1}_{depth2}: Layer-specific transports
   - TRANS_{component}: Component-specific transports

Overturning Variables (`MOC_`  with coordinate specification):
   - MOC_Z: Depth coordinate overturning
   - MOC_SIGMA0: σ₀ density coordinate overturning  
   - MOC_SIGMA2: σ₂ density coordinate overturning

Uncertainty Variables (`_ERR`` suffix):
   - {VARIABLE}_ERR: Uncertainty estimate for any variable
   - Same units as parent variable
   - Examples: MOC_SIGMA0_ERR, MHT_ERR, TRANS_EKMAN_ERR

Heat/Freshwater Transport:
   - MHT: Meridional heat transport (PW)
   - MFT: Meridional freshwater transport (Sverdrup)
   - Regional qualifiers: _EAST, _WEST, _GYRE, _OT

Standards Compliance
-------------------

**Format Identification**:
   - Conventions: "CF-1.8, ACDD-1.3, OceanSITES-1.5"
   - format_version: "AC1.0"
   - standard_name_vocabulary: CF Standard Name Table v84

**Metadata Requirements**:

Every variable includes:
   - standard_name (CF-1.8 vocabulary)
   - long_name (human-readable)
   - units (UDUNITS-2 compliant)
   - description (extended detail)

Unit Standardization
-------------------

**Key Units**:
   - Transport: Sverdrup (1×10⁶ m³/s)
   - Heat transport: PW (1×10¹⁵ W) 
   - Temperature: degree_C
   - Salinity: 1 (practical salinity) or g m-3 (absolute salinity)
   - Pressure: dbar
   - Coordinates: degree_north, degree_east

**Rationale**:
   - The use of "Sverdrup" deviates from CF conventions (m3 s-1) but reflects appropriate scales for the AMOC
   - Using the full "Sverdrup" instead of "Sv" avoids ambiguities with "sievert"
   - Using PW for ocean heat transport makes numbers more readable than W

