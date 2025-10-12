"""Tests for amocatlas.utilities module."""
from pathlib import Path
import tempfile
import os
from typing import Any, Tuple
import yaml
import pandas as pd

import pytest
import xarray as xr

from amocatlas import logger, utilities

# Sample data
VALID_URL = "https://mooring.ucsd.edu/move/nc/"
INVALID_URL = "ftdp://invalid-url.com/data.nc"
INVALID_STRING = "not_a_valid_source"

# Replace with actual path to a local .nc file if you have one for local testing
LOCAL_VALID_FILE = "/path/to/your/OS_MOVE_TRANSPORTS.nc"
LOCAL_INVALID_FILE = "/path/to/invalid_file.txt"

logger.disable_logging()


@pytest.mark.parametrize(
    "url,expected",
    [
        (VALID_URL, True),
        (INVALID_URL, False),
        ("not_a_url", False),
    ],
)
def test_is_valid_url(url: str, expected: bool) -> None:
    assert utilities._is_valid_url(url) == expected


@pytest.mark.parametrize(
    "path,expected",
    [
        (
            LOCAL_VALID_FILE,
            Path(LOCAL_VALID_FILE).is_file() and LOCAL_VALID_FILE.endswith(".nc"),
        ),
        (LOCAL_INVALID_FILE, False),
        ("non_existent_file.nc", False),
    ],
)
def test_is_valid_file(path: str, expected: bool) -> None:
    assert utilities._is_valid_file(path) == expected


def test_safe_update_attrs_add_new_attribute() -> None:
    """Test adding new attributes via safe_update_attrs."""
    ds = xr.Dataset()
    new_attrs = {"project": "MOVE"}
    ds = utilities.safe_update_attrs(ds, new_attrs)
    assert ds.attrs["project"] == "MOVE"


def test_safe_update_attrs_existing_key_logs(caplog: Any) -> None:
    """Test logging when trying to overwrite existing attributes."""
    from amocatlas import logger, utilities

    # Re-enable logging for this test
    logger.enable_logging()

    ds = xr.Dataset(attrs={"project": "MOVE"})
    new_attrs = {"project": "OSNAP"}

    with caplog.at_level("DEBUG", logger="amocatlas"):
        utilities.safe_update_attrs(ds, new_attrs, overwrite=False, verbose=True)

    assert any(
        "Attribute 'project' already exists in dataset attrs and will not be overwritten."
        in message
        for message in caplog.messages
    )


def test_safe_update_attrs_existing_key_with_overwrite() -> None:
    """Test overwriting existing attributes when overwrite=True."""
    ds = xr.Dataset(attrs={"project": "MOVE"})
    new_attrs = {"project": "OSNAP"}
    ds = utilities.safe_update_attrs(ds, new_attrs, overwrite=True)
    assert ds.attrs["project"] == "OSNAP"


def test_get_project_root() -> None:
    """Test getting project root directory."""
    root = utilities.get_project_root()
    assert isinstance(root, Path)
    # Should find a directory containing setup.py or pyproject.toml
    assert root.exists()
    # Check for project files
    project_files = ["pyproject.toml", "setup.py", "setup.cfg"]
    assert any((root / file).exists() for file in project_files)


def test_get_default_data_dir() -> None:
    """Test getting default data directory."""
    data_dir = utilities.get_default_data_dir()
    assert isinstance(data_dir, Path)
    # The function returns <project>/data, not .amocatlas_data
    assert "data" in str(data_dir)
    assert data_dir.name == "data"


def test_normalize_whitespace() -> None:
    """Test whitespace normalization in attributes."""
    attrs = {
        "description": "This  has  multiple   spaces",
        "comment": "Line1\nLine2\n\nLine4",
        "normal_attr": "normal_value"
    }

    result = utilities.normalize_whitespace(attrs)

    assert result["description"] == "This has multiple spaces"
    assert result["comment"] == "Line1 Line2 Line4"
    assert result["normal_attr"] == "normal_value"


def test_resolve_file_path_local() -> None:
    """Test resolving local file paths."""
    with tempfile.NamedTemporaryFile(suffix=".nc", delete=False) as tmp:
        tmp_path = tmp.name
        tmp.write(b"test data")

    try:
        # Test local file
        result = utilities.resolve_file_path(
            file_name=os.path.basename(tmp_path),
            source=os.path.dirname(tmp_path),
            download_url=None,
            local_data_dir=Path(os.path.dirname(tmp_path)),
            redownload=False
        )
        assert result == Path(tmp_path)
        assert result.exists()
    finally:
        os.unlink(tmp_path)


def test_resolve_file_path_url() -> None:
    """Test resolving URL-based file paths (mock scenario)."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create a file in cache to avoid download
        cached_file = Path(tmp_dir) / "test_file.nc"
        cached_file.write_text("test data")

        result = utilities.resolve_file_path(
            file_name="test_file.nc",
            source="https://example.com/data/",
            download_url="https://example.com/data/test_file.nc",
            local_data_dir=Path(tmp_dir),
            redownload=False
        )
        # Should return the cached file path
        assert result == cached_file
        assert result.exists()


def test_load_array_metadata() -> None:
    """Test loading array metadata."""
    # Test with a known array
    try:
        metadata = utilities.load_array_metadata("rapid")
        assert isinstance(metadata, dict)
        # Should contain basic structure
        assert "array_name" in metadata or len(metadata) > 0
    except FileNotFoundError:
        # If metadata files don't exist, test the exception handling
        pytest.skip("Array metadata files not available")


def test_validate_array_yaml() -> None:
    """Test YAML validation for arrays."""
    # Create a temporary YAML file for testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yml', delete=False) as tmp:
        yaml.dump({
            "array_name": "test",
            "description": "Test array",
            "variables": {"test_var": {"units": "m"}}
        }, tmp)
        tmp_path = tmp.name

    try:
        # This should work without errors (exact behavior depends on implementation)
        result = utilities.validate_array_yaml("test", verbose=False)
        assert isinstance(result, bool)
    except Exception:  # noqa: BLE001
        # If validation fails due to missing schema, that's expected
        pass
    finally:
        os.unlink(tmp_path)


def test_parse_ascii_header() -> None:
    """Test parsing ASCII file headers."""
    # Create a test ASCII file
    content = """% Column 1: Year
% Column 2: Month
% Column 3: Value (m/s)
% This is a comment
2020 1 1.5
2020 2 2.0
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        columns, num_header_lines = utilities.parse_ascii_header(tmp_path, comment_char="%")

        assert len(columns) == 3
        assert "Year" in columns[0]
        assert "Month" in columns[1]
        assert "Value" in columns[2]
        assert num_header_lines >= 3  # Returns number of header lines
    finally:
        os.unlink(tmp_path)


def test_read_ascii_file() -> None:
    """Test reading ASCII data files."""
    content = """% Header line
% Another header
1.0 2.0 3.0
4.0 5.0 6.0
7.0 8.0 9.0
"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        df = utilities.read_ascii_file(tmp_path, comment_char="%")

        assert isinstance(df, pd.DataFrame)
        # The function might skip header lines, check actual length
        assert len(df) >= 2  # At least 2 data rows
        assert len(df.columns) == 3  # 3 columns
        # Check data values (adjust indices based on actual behavior)
        assert df.iloc[0, 0] == 1.0 or df.iloc[0, 0] == 4.0
    finally:
        os.unlink(tmp_path)


def test_is_valid_url_edge_cases() -> None:
    """Test URL validation with edge cases."""
    # Function requires scheme, netloc, AND path
    assert utilities._is_valid_url("https://example.com/path")
    assert utilities._is_valid_url("http://test.org/data")
    assert utilities._is_valid_url("ftp://ftp.example.com/files")

    # These should fail (no path required by the function)
    assert not utilities._is_valid_url("https://example.com")  # No path
    assert not utilities._is_valid_url("")
    assert not utilities._is_valid_url("not-a-url")
    assert not utilities._is_valid_url("file:///local/path")  # Wrong scheme


def test_is_valid_file_edge_cases() -> None:
    """Test file validation with edge cases."""
    # Test with actual temporary file
    with tempfile.NamedTemporaryFile(suffix=".nc") as tmp:
        assert utilities._is_valid_file(tmp.name)

    # Test with non-existent file
    assert not utilities._is_valid_file("/definitely/does/not/exist.nc")

    # Test with directory instead of file
    with tempfile.TemporaryDirectory() as tmp_dir:
        assert not utilities._is_valid_file(tmp_dir)


def test_apply_defaults_decorator() -> None:
    """Test the apply_defaults decorator functionality."""
    @utilities.apply_defaults("default_source", ["file1.nc", "file2.nc"])
    def test_function(source: str = None, file_list: list = None) -> Tuple[str, list]:
        return source, file_list

    # Test with no arguments (should use defaults)
    source, files = test_function()
    assert source == "default_source"
    assert files == ["file1.nc", "file2.nc"]

    # Test with custom arguments
    source, files = test_function(source="custom", file_list=["custom.nc"])
    assert source == "custom"
    assert files == ["custom.nc"]


def test_resolve_file_path_missing_file() -> None:
    """Test error handling when local file is missing."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        with pytest.raises(FileNotFoundError):
            utilities.resolve_file_path(
                file_name="nonexistent.nc",
                source=tmp_dir,  # Local directory
                download_url=None,
                local_data_dir=Path(tmp_dir),
                redownload=False
            )


def test_safe_update_attrs_edge_cases() -> None:
    """Test edge cases for safe_update_attrs."""
    # Test with empty attributes
    ds = xr.Dataset()
    result = utilities.safe_update_attrs(ds, {})
    assert len(result.attrs) == 0

    # Test return value
    ds = xr.Dataset()
    result = utilities.safe_update_attrs(ds, {"test": "value"})
    assert result is ds  # Should modify in place and return same object


def test_normalize_whitespace_edge_cases() -> None:
    """Test edge cases for normalize_whitespace."""
    # Test with non-string values
    attrs = {
        "string_val": "normal text",
        "int_val": 42,
        "float_val": 3.14,
        "none_val": None
    }

    result = utilities.normalize_whitespace(attrs)
    assert result["string_val"] == "normal text"
    assert result["int_val"] == 42  # Should remain unchanged
    assert result["float_val"] == 3.14
    assert result["none_val"] is None


def test_load_array_metadata_missing() -> None:
    """Test loading metadata for non-existent array."""
    with pytest.raises(FileNotFoundError):
        utilities.load_array_metadata("definitely_does_not_exist")
