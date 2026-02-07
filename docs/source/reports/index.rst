Dataset Reports
===============

AMOCatlas provides comprehensive automated reports for all supported datasets.
These reports include variable mappings, statistical summaries, temporal coverage
analysis, and data quality assessments.

.. toctree::
   :maxdepth: 1
   :caption: Individual Dataset Reports

   rapid_report
   osnap_report
   move_report
   samba_report
   mocha_report
   arcticgateway_report
   dso_report
   fbc_report
   fw2015_report
   calafat2025_report
   zheng2024_report
   wh41n_report
   noac47n_report

Report Features
---------------

Each dataset report includes:

📊 **Dataset Overview**
   - Project information and institutional details
   - Temporal coverage and record length
   - Data collection frequency

🔄 **Variable Mapping Table**
   - Original variable names from source files
   - Standardized variable names (for AC1 conversion)
   - Units, descriptions, and statistical summaries
   - Data quality indicators

📈 **Statistical Analysis**
   - Min/max values for each variable
   - Missing data percentages
   - Dataset size and structure

Automated Generation
--------------------

Reports are automatically generated from the actual datasets using::

    from amocatlas import report
    
    # Generate report for any dataset
    rst_report = report.generate_dataset_report("rapid", transport_only=True)
    
    # Analyze dataset for programmatic access
    analysis = report.analyze_dataset("rapid", transport_only=True)
    print(f"Dataset has {analysis.statistics['total_variables']} variables")

This ensures the documentation always reflects the current state of the data and
helps identify any missing or incorrect metadata before implementing AC1 conversion.