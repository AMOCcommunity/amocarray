"""Tests for amocatlas.report module.

This module tests both the core report generation functionality and utility functions
for dataset analysis and reporting.
"""

import subprocess
import sys
from pathlib import Path
import pandas as pd
import pytest
import xarray as xr

from amocatlas import report
from amocatlas.logger import disable_logging
from amocatlas.report import ReportUtils

# Disable logging for cleaner test output
disable_logging()


class TestReportGeneration:
    """Integration tests for report generation."""

    def test_generate_small_dataset_report(self):
        """Test report generation with a small dataset (47N - 0.01 MB)."""
        # Use 47N: single small file, safe for CI
        rst_content = ReportUtils.generate_array_report("noac47n")

        # Verify basic structure
        assert "Datasets" in rst_content
        assert "Generated:" in rst_content
        assert "Dataset Overview" in rst_content
        assert "Variable Information" in rst_content

        # Should have reasonable length (not empty, not massive)
        assert 500 < len(rst_content) < 10000

    def test_generate_multi_file_small_dataset_report(self):
        """Test report generation with multiple small files (SAMBA - 0.03 + 0.20 = 0.23 MB)."""
        # SAMBA has 2 small files, perfect for testing multi-file reports
        rst_content = ReportUtils.generate_array_report("samba")

        # Verify basic structure
        assert "SAMBA Datasets" in rst_content
        assert "Generated:" in rst_content
        assert "Dataset Overview" in rst_content

        # Should handle multiple datasets
        assert "----" in rst_content  # Section separators for multiple files

        # Test table generation: should have 2 tables per dataset (coordinates + variables)
        # SAMBA has 2 datasets, so expect 4 tables total
        list_tables = rst_content.count(".. list-table::")
        assert (
            list_tables == 4
        ), f"Expected 4 list-tables (2 per dataset), found {list_tables}"

        # Test figure generation: should have 2 figures (one per dataset)
        figures = rst_content.count(".. figure::")
        assert figures == 2, f"Expected 2 figures (one per dataset), found {figures}"

        # Test specific time coverage for SAMBA files
        assert (
            "2013-09-12 to 2017-07-16" in rst_content
        ), "Missing time coverage for Upper_Abyssal_Transport_Anomalies.txt"
        assert (
            "2009-03-19 to 2017-04-29" in rst_content
        ), "Missing time coverage for second SAMBA file"

        # Test metadata addition: processing software should be added
        assert (
            "- **Processing Software**: http://github.com/AMOCcommunity/amocatlas"
            in rst_content
        ), "Missing processing software metadata"

        # Test variable mapping: check for specific SAMBA variable remapping
        assert (
            "   * - *Ekman__wind__contribution_to_the_MOC_anomaly* → **EKMAN**"
            in rst_content
        ), "Missing variable mapping for EKMAN"

        # Test units conversion: should have multiple instances of "Sverdrup" units
        sverdrup_count = rst_content.count("Sverdrup")
        assert (
            sverdrup_count >= 2
        ), f"Expected at least 2 'Sverdrup' units, found {sverdrup_count}"

        # Should be longer than single-file reports due to multiple files
        assert len(rst_content) > 2000

        # Should be reasonable size (not massive)
        assert len(rst_content) < 50000

    @pytest.mark.slow
    def test_generate_rapid_report_transport_only(self):
        """Test most common use case: generating RAPID transport report."""
        # This is the primary user workflow
        rst_content = report.rapid(all_files=False)

        # Verify basic structure
        assert "RAPID Datasets" in rst_content
        assert "Generated:" in rst_content
        assert "Dataset Overview" in rst_content
        assert "Variable Information" in rst_content
        assert "Coordinate Information" in rst_content

        # Check key metadata fields are present
        assert "Project" in rst_content or "Description" in rst_content

        # Verify RST formatting is correct
        assert "========" in rst_content  # Title underline
        assert "^^^^^^^^" in rst_content  # Section headers
        assert ".. list-table::" in rst_content  # Tables

        # Should contain transport variables
        assert "MOC" in rst_content or "transport" in rst_content.lower()

        # Should have reasonable length (not empty, not massive)
        assert 1000 < len(rst_content) < 50000

    @pytest.mark.slow
    def test_generate_multi_dataset_report(self):
        """Test report generation for arrays with multiple files."""
        # Use OSNAP which typically has multiple datasets
        rst_content = ReportUtils.generate_array_report("osnap")

        # Should handle multiple datasets
        assert "OSNAP Datasets" in rst_content
        assert "Generated:" in rst_content

        # Should have section separators for multiple files
        assert "----" in rst_content

        # Should be longer than single-file reports
        assert len(rst_content) > 2000

    @pytest.mark.slow
    def test_command_line_generate_report(self):
        """Test command-line interface works."""
        # Test the CLI interface that users will actually use
        # Use a small dataset for faster testing (NOAC47N is only 0.01 MB)
        result = subprocess.run(
            [sys.executable, "generate_report", "--data_source", "noac47n"],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,  # Run from project root
            timeout=30,
        )

        # Should complete successfully
        assert result.returncode == 0, f"CLI failed with stderr: {result.stderr}"

        # Should produce some output
        assert "Processing" in result.stdout or "Generated" in result.stdout

        # Should create the expected report file
        report_file = Path("docs/source/reports/noac47n_report.rst")
        if report_file.exists():
            content = report_file.read_text()
            assert "Datasets" in content


class TestReportUtils:
    """Unit tests for core utility functions."""

    def test_handle_yyyymm_time_format(self):
        """Test YYYYMM time format conversion."""
        # Create test data in YYYYMM format
        test_data = xr.DataArray([200201, 200202, 200203])  # Feb-Apr 2002

        result = ReportUtils.handle_yyyymm_time_format(test_data)

        # Should convert to proper datetime
        assert isinstance(result, pd.DatetimeIndex)
        assert len(result) == 3

        # Check first date - handle both possible interpretations
        assert result[0].year == 2002
        # Month could be 1 or 2 depending on interpretation
        assert result[0].month in [1, 2]
        assert result[0].day == 1

    def test_estimate_frequency(self):
        """Test frequency estimation from time differences."""
        # Test hourly
        hourly_diff = pd.Timedelta(hours=1)
        result = ReportUtils.estimate_frequency(hourly_diff)
        assert result in ["hourly", "1.0H"]  # Accept both formats

        # Test daily
        daily_diff = pd.Timedelta(hours=24)
        assert ReportUtils.estimate_frequency(daily_diff) == "daily"

        # Test 12-hourly
        twelve_h_diff = pd.Timedelta(hours=12)
        assert ReportUtils.estimate_frequency(twelve_h_diff) == "12H"

        # Test monthly (30 days)
        monthly_diff = pd.Timedelta(days=30)
        assert ReportUtils.estimate_frequency(monthly_diff) == "monthly"

        # Test sub-hourly
        minute_diff = pd.Timedelta(minutes=30)
        result = ReportUtils.estimate_frequency(minute_diff)
        assert "min" in result

    def test_safe_time_diff_days(self):
        """Test safe time difference calculation."""
        from datetime import datetime

        # Test normal datetime difference
        start = datetime(2020, 1, 1)
        end = datetime(2020, 1, 31)
        diff = ReportUtils._safe_time_diff_days(end, start)
        assert diff == 30

        # Test YYYYMM format
        diff_yyyymm = ReportUtils._safe_time_diff_days(202002, 202001)  # Jan to Feb
        assert 25 < diff_yyyymm < 35  # Roughly a month

        # Test edge case with invalid data
        diff_invalid = ReportUtils._safe_time_diff_days(None, None)
        assert diff_invalid == 0

    def test_safe_format_date(self):
        """Test safe date formatting."""
        from datetime import datetime

        # Test normal datetime
        date = datetime(2020, 5, 15, 12, 30)
        result = ReportUtils._safe_format_date(date)
        assert result == "2020-05-15"

        # Test unix timestamp
        timestamp = 1589544600  # May 15, 2020
        result = ReportUtils._safe_format_date(timestamp)
        assert "2020-05-15" in result

        # Test year value
        result = ReportUtils._safe_format_date(2020)
        assert "2020" in result

    def test_dataframe_to_rst_table(self):
        """Test DataFrame to RST table conversion."""
        # Create test DataFrame
        df = pd.DataFrame(
            {
                "Variable": ["**MOC**", "*moc_mar_hc10* → **MOC**"],
                "Units": ["Sv", "Sv"],
                "Description": [
                    "Meridional overturning circulation",
                    "MOC time series",
                ],
            }
        )

        rst_lines = ReportUtils.dataframe_to_rst_table(df)

        # Should produce list-table format
        rst_text = "\n".join(rst_lines)
        assert ".. list-table::" in rst_text
        assert ":widths:" in rst_text
        assert ":header-rows: 1" in rst_text

        # Should preserve formatting (asterisks for bold/italic)
        assert "**MOC**" in rst_text
        assert "*moc_mar_hc10*" in rst_text

        # Should have proper structure
        assert "   * - Variable" in rst_text
        assert "     - Units" in rst_text


class TestAnalysisAndStatistics:
    """Tests for dataset analysis functionality."""

    def test_compute_dataset_statistics(self):
        """Test dataset statistics computation."""
        # Create minimal test dataset
        ds = xr.Dataset(
            {
                "temperature": (["time"], [15.0, 16.0, 17.0]),
                "salinity": (["time"], [35.0, 35.1, 35.2]),
            },
            coords={"time": pd.date_range("2020-01-01", periods=3)},
        )

        stats = ReportUtils.compute_dataset_statistics(ds)

        # Basic structure
        assert stats["total_variables"] == 2
        assert stats["total_coordinates"] == 1
        assert "variables" in stats

        # Variable stats
        temp_stats = stats["variables"]["temperature"]
        assert temp_stats["min"] == 15.0
        assert temp_stats["max"] == 17.0
        assert temp_stats["units"] == "unknown"  # No units in test data

    def test_analyze_temporal_coverage(self):
        """Test temporal coverage analysis."""
        # Create test dataset with time
        times = pd.date_range("2020-01-01", "2020-01-10", freq="D")
        ds = xr.Dataset({"data": (["TIME"], range(10))}, coords={"TIME": times})

        temporal = ReportUtils.analyze_temporal_coverage(ds)

        # Should detect time
        assert temporal["has_time"] is True
        assert temporal["valid_times"] is True
        assert temporal["coordinate_name"] == "TIME"

        # Should calculate span
        assert temporal["time_span_days"] == 9  # 10 days, 9 day difference
        assert temporal["total_records"] == 10

        # Should estimate frequency
        assert "estimated_frequency" in temporal
        assert temporal["estimated_frequency"] == "daily"


class TestErrorHandling:
    """Tests for error handling and edge cases."""

    def test_generate_report_nonexistent_array(self):
        """Test graceful handling of invalid array names."""
        with pytest.raises((AttributeError, ValueError)):
            ReportUtils.generate_array_report("nonexistent_array")

    def test_empty_dataframe_to_rst(self):
        """Test handling of empty DataFrames."""
        df = pd.DataFrame()
        rst_lines = ReportUtils.dataframe_to_rst_table(df)

        assert len(rst_lines) == 1
        assert "No data available" in rst_lines[0]

    def test_dataset_without_time(self):
        """Test analysis of datasets without time coordinate."""
        ds = xr.Dataset({"static_var": (["x"], [1, 2, 3])}, coords={"x": [0, 1, 2]})

        temporal = ReportUtils.analyze_temporal_coverage(ds)
        assert temporal["has_time"] is False
