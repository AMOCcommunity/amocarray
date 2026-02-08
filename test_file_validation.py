#!/usr/bin/env python3
"""Test validation logic for file selection parameters in read API."""

from amocatlas.read import _validate_file_selection_params


def test_default_behavior():
    """Test default behavior (transport_only=True, no other params)."""
    effective_transport_only, effective_file_list = _validate_file_selection_params(
        transport_only=True,
        all_files=False,
        file_list=None,
        available_files=["file1.nc", "file2.nc"],
        transport_files=["file1.nc"],
    )
    assert effective_transport_only == True
    assert effective_file_list is None


def test_custom_file_list():
    """Test that custom file_list overrides transport_only default."""
    effective_transport_only, effective_file_list = _validate_file_selection_params(
        transport_only=True,  # This is the default but should be overridden
        all_files=False,
        file_list=["file1.nc", "file2.nc"],
        available_files=["file1.nc", "file2.nc", "file3.nc"],
        transport_files=["file1.nc"],
    )
    assert effective_transport_only == False
    assert effective_file_list == ["file1.nc", "file2.nc"]


def test_all_files_true():
    """Test that all_files=True overrides transport_only."""
    effective_transport_only, effective_file_list = _validate_file_selection_params(
        transport_only=True,  # Should be overridden
        all_files=True,
        file_list=None,
        available_files=["file1.nc", "file2.nc"],
        transport_files=["file1.nc"],
    )
    assert effective_transport_only == False
    assert effective_file_list is None


def test_conflicting_all_files_and_file_list_valid():
    """Test all_files=True with file_list that matches all files (should work)."""
    # This should work if file_list matches available_files exactly
    effective_transport_only, effective_file_list = _validate_file_selection_params(
        transport_only=False,
        all_files=True,
        file_list=["file1.nc", "file2.nc"],  # Matches available_files
        available_files=["file1.nc", "file2.nc"],
        transport_files=["file1.nc"],
    )
    assert effective_transport_only == False
    assert effective_file_list is None  # all_files takes precedence


def test_conflicting_all_files_and_file_list_invalid():
    """Test all_files=True with file_list that doesn't match (should fail)."""
    print("    Starting invalid combination test...")
    try:
        result = _validate_file_selection_params(
            transport_only=False,
            all_files=True,
            file_list=["file1.nc"],  # Doesn't match all available files
            available_files=["file1.nc", "file2.nc"],
            transport_files=["file1.nc"],
        )
        # If we get here, the test failed
        print(f"    ERROR: Got result instead of exception: {result}")
        raise AssertionError("Expected ValueError was not raised")
    except ValueError as e:
        # This is expected - check the error message
        print(f"    Got expected ValueError: {e}")
        assert "all_files=True conflicts with file_list" in str(e)
        print("    Assertion passed, test completed successfully")


def test_string_file_list():
    """Test that string file_list is handled correctly."""
    effective_transport_only, effective_file_list = _validate_file_selection_params(
        transport_only=True,
        all_files=False,
        file_list="single_file.nc",  # String instead of list
        available_files=["single_file.nc", "other_file.nc"],
        transport_files=["single_file.nc"],
    )
    assert effective_transport_only == False
    assert effective_file_list == "single_file.nc"


def test_empty_available_files():
    """Test behavior with empty available files list."""
    effective_transport_only, effective_file_list = _validate_file_selection_params(
        transport_only=True,
        all_files=False,
        file_list=None,
        available_files=[],
        transport_files=None,
    )
    assert effective_transport_only == True
    assert effective_file_list is None


if __name__ == "__main__":
    # Run basic tests
    test_default_behavior()
    test_custom_file_list()
    test_all_files_true()
    test_conflicting_all_files_and_file_list_valid()
    test_string_file_list()
    test_empty_available_files()

    print("✅ All validation logic tests passed!")

    # Test the error case manually
    print("\n--- Testing error case manually ---")
    try:
        _validate_file_selection_params(
            transport_only=False,
            all_files=True,
            file_list=["file1.nc"],  # Doesn't match all available files
            available_files=["file1.nc", "file2.nc"],
            transport_files=["file1.nc"],
        )
        print("❌ Error test should have failed!")
    except ValueError as e:
        print(f"✅ Error case correctly caught: {e}")

    # Now test the wrapper function
    print("\n--- Testing wrapper function ---")
    try:
        test_conflicting_all_files_and_file_list_invalid()
        print(
            "✅ Error validation test passed (correctly caught and validated the error)"
        )
    except AssertionError as e:
        print(f"❌ Test assertion failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected exception in test: {type(e).__name__}: {e}")

    print("\n🎉 All file validation tests completed successfully!")
