import pathlib
import sys
import numpy as np
import pandas as pd
import xarray as xr
from datetime import datetime

script_dir = pathlib.Path(__file__).parent.absolute()
parent_dir = script_dir.parents[0]
sys.path.append(str(parent_dir))

from amocatlas import logger, tools

logger.disable_logging()


def test_convert_units_var():
    """Test basic unit conversion."""
    var_values = 100
    current_units = "cm/s"
    new_units = "m/s"
    converted_values = tools.convert_units_var(var_values, current_units, new_units)
    assert converted_values == 1.0


def test_generate_reverse_conversions():
    """Test generating reverse unit conversions."""
    forward = {"m": {"cm": 100, "km": 0.001}}
    result = tools.generate_reverse_conversions(forward)

    # Check forward conversions are preserved
    assert result["m"]["cm"] == 100
    assert result["m"]["km"] == 0.001

    # Check reverse conversions are created
    assert result["cm"]["m"] == 0.01
    assert result["km"]["m"] == 1000


def test_generate_reverse_conversions_zero_factor():
    """Test handling of zero conversion factors."""
    forward = {"m": {"invalid": 0}}
    result = tools.generate_reverse_conversions(forward)

    # Forward conversion should be preserved
    assert result["m"]["invalid"] == 0
    # Reverse conversion should not exist due to zero factor
    assert "m" not in result.get("invalid", {})


def test_reformat_units_var():
    """Test unit reformatting for variables."""
    ds = xr.Dataset({
        "velocity": xr.DataArray([1, 2, 3], attrs={"units": "m/s"})
    })

    # Use the default format mapping
    result = tools.reformat_units_var(ds, "velocity")
    assert result == "m s-1"  # Based on tools.unit_str_format

    # Test with custom format
    custom_format = {"m/s": "meters per second"}
    result = tools.reformat_units_var(ds, "velocity", custom_format)
    assert result == "meters per second"

    # Test with units not in format dict
    ds2 = xr.Dataset({
        "temp": xr.DataArray([1, 2, 3], attrs={"units": "unknown_unit"})
    })
    result = tools.reformat_units_var(ds2, "temp")
    assert result == "unknown_unit"  # Should return original


def test_find_best_dtype():
    """Test finding optimal data type for variables."""
    # Test small integer data
    int_data = xr.DataArray([1, 2, 3, 4, 5])
    dtype = tools.find_best_dtype("test_var", int_data)
    assert dtype == np.int16  # Small values fit in int16

    # Test float data
    float_data = xr.DataArray([1.1, 2.2, 3.3])
    dtype = tools.find_best_dtype("test_var", float_data)
    assert dtype == np.float32

    # Test large integer data requiring larger type
    large_int_data = xr.DataArray([2**31, 2**31 + 1])
    dtype = tools.find_best_dtype("test_var", large_int_data)
    assert dtype == np.int64


def test_set_fill_value():
    """Test setting appropriate fill values for data types."""
    # Function calculates based on bit width: 2^(bits-1) - 1
    assert tools.set_fill_value(np.int32) == 2**31 - 1  # 2147483647
    assert tools.set_fill_value(np.int16) == 2**15 - 1  # 32767
    assert tools.set_fill_value(np.int64) == 2**63 - 1  # Very large number


def test_set_best_dtype():
    """Test optimizing data types for entire dataset."""
    ds = xr.Dataset({
        "int_var": xr.DataArray([1, 2, 3], attrs={"units": "m"}),
        "float_var": xr.DataArray([1.1, 2.2, 3.3], attrs={"units": "m/s"}),
        "TIME": xr.DataArray(pd.date_range("2020-01-01", periods=3))
    })

    result = tools.set_best_dtype(ds)

    # Check that data types were optimized (small values use int16)
    assert result["int_var"].dtype == np.int16
    assert result["float_var"].dtype == np.float32
    # TIME should remain unchanged (datetime)
    assert "datetime" in str(result["TIME"].dtype)


def test_to_decimal_year():
    """Test conversion of dates to decimal years."""
    dates = pd.Series([
        datetime(2020, 1, 1),
        datetime(2020, 7, 1),  # Mid-year
        datetime(2021, 1, 1)
    ])

    result = tools.to_decimal_year(dates)

    assert result.iloc[0] == 2020.0
    assert 2020.4 < result.iloc[1] < 2020.6  # Approximately mid-year
    assert result.iloc[2] == 2021.0


def test_extract_time_and_time_num():
    """Test extracting time information from dataset."""
    time_values = pd.date_range("2020-01-01", periods=5, freq="D")
    ds = xr.Dataset({
        "data": xr.DataArray([1, 2, 3, 4, 5], dims=["TIME"]),
        "TIME": time_values
    })

    result = tools.extract_time_and_time_num(ds)

    assert "time" in result.columns
    assert "time_num" in result.columns
    assert len(result) == 5
    assert result["time_num"].iloc[0] == 2020.0


def test_bin_average_5day():
    """Test 5-day binning and averaging."""
    # Create test data with daily values for 15 days
    dates = pd.date_range("2020-01-01", periods=15, freq="D")
    df = pd.DataFrame({
        "time": dates,
        "moc": range(15)  # Default column name expected by function
    })

    result = tools.bin_average_5day(df)

    # Should have 3 bins (15 days / 5 days per bin)
    assert len(result) == 3
    assert "moc" in result.columns
    # Check that values are averaged correctly
    assert result["moc"].iloc[0] == 2.0  # Average of 0,1,2,3,4

    # Test with custom column name
    df_custom = pd.DataFrame({
        "time": dates,
        "value": range(15)
    })
    result_custom = tools.bin_average_5day(df_custom, value_column="value")
    assert "value" in result_custom.columns


def test_bin_average_monthly():
    """Test monthly binning and averaging."""
    # Create test data spanning 2 months
    dates = pd.date_range("2020-01-01", periods=60, freq="D")
    df = pd.DataFrame({
        "time": dates,
        "value": range(60)
    })

    result = tools.bin_average_monthly(df)

    # Should have 2 bins (January and February)
    assert len(result) == 2
    assert "value" in result.columns


def test_check_and_bin():
    """Test automatic binning based on data resolution."""
    # Test daily dataset (median diff < 15 days, should use monthly binning)
    daily_dates = pd.date_range("2020-01-01", periods=100, freq="D")
    daily_df = pd.DataFrame({
        "time": daily_dates,
        "moc": range(100)
    })

    daily_result = tools.check_and_bin(daily_df)
    # Should be monthly bins (fewer than original)
    assert len(daily_result) < len(daily_df)

    # Test monthly dataset (median diff > 15 days, should remain unchanged)
    monthly_dates = pd.date_range("2020-01-01", periods=12, freq="M")
    monthly_df = pd.DataFrame({
        "time": monthly_dates,
        "moc": range(12)
    })

    monthly_result = tools.check_and_bin(monthly_df)
    # Should be unchanged
    assert len(monthly_result) == len(monthly_df)
    pd.testing.assert_frame_equal(monthly_result, monthly_df)


def test_apply_tukey_filter():
    """Test Tukey filter application."""
    # Create test DataFrame with more variation to ensure filtering has effect
    np.random.seed(42)  # For reproducible test
    dates = pd.date_range("2020-01-01", periods=200, freq="D")
    # Create signal with trend and noise
    signal = np.sin(np.arange(200) * 0.05) + 0.5 * np.random.normal(0, 1, 200)
    df = pd.DataFrame({
        "time": dates,
        "data": signal
    })

    result = tools.apply_tukey_filter(df, column="data", alpha=0.5, window_months=2)

    # Result should be same length as input
    assert len(result) == len(df)
    # Should have same columns
    assert "data" in result.columns
    # Function returns the DataFrame, check if it's processed
    assert isinstance(result, pd.DataFrame)

    # Test with add_back_mean option
    result_with_mean = tools.apply_tukey_filter(
        df, column="data", alpha=0.5, add_back_mean=True
    )
    assert isinstance(result_with_mean, pd.DataFrame)


def test_handle_samba_gaps():
    """Test SAMBA data gap handling."""
    # Create test data with a gap
    dates = pd.date_range("2020-01-01", periods=10, freq="D")
    df = pd.DataFrame({
        "time": dates,
        "value": [1, 2, np.nan, np.nan, np.nan, 6, 7, 8, 9, 10]
    })

    result = tools.handle_samba_gaps(df)

    # Should return a DataFrame
    assert isinstance(result, pd.DataFrame)
    # Should have same columns
    assert list(result.columns) == list(df.columns)
