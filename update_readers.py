#!/usr/bin/env python3
"""Script to systematically update all data source readers with:
1. YAML metadata loading via ReaderUtils.load_array_metadata_with_fallback()
2. Full track_added_attrs functionality via ReaderUtils.attach_metadata_with_tracking()

This applies the pattern established in RAPID and MOVE to all other readers.
"""

import re
from pathlib import Path

# List of readers to update (excluding RAPID which is already done, and MOVE/SAMBA which we just updated)
READERS_TO_UPDATE = [
    "osnap55n.py",
    "mocha26n.py",
    "arcticgateway.py",
    "dso.py",
    "fbc.py",
    "fw2015.py",
    "calafat2025.py",
    "zheng2024.py",
    "wh41n.py",
    "noac47n.py",
]


def update_reader_file(file_path):
    """Update a single reader file with the new ReaderUtils pattern."""
    print(f"Updating {file_path.name}...")

    with open(file_path, "r") as f:
        content = f.read()

    # Extract datasource ID and metadata constants
    datasource_match = re.search(r'DATASOURCE_ID = ["\']([^"\']+)["\']', content)
    if not datasource_match:
        print(f"  ERROR: Could not find DATASOURCE_ID in {file_path.name}")
        return False

    datasource_id = datasource_match.group(1)

    # Find metadata constants
    metadata_constant = f'{datasource_id.upper().replace("2025", "").replace("2024", "").replace("26N", "").replace("16N", "").replace("34S", "").replace("55N", "").replace("47N", "").replace("41N", "")}_METADATA'
    file_metadata_constant = f'{datasource_id.upper().replace("2025", "").replace("2024", "").replace("26N", "").replace("16N", "").replace("34S", "").replace("55N", "").replace("47N", "").replace("41N", "")}_FILE_METADATA'

    # Handle special cases
    if "arcticgateway" in file_path.name:
        metadata_constant = "ARCTIC_METADATA"
        file_metadata_constant = "ARCTIC_FILE_METADATA"
    elif "calafat2025" in file_path.name:
        metadata_constant = "CALAFAT2025_METADATA"
        file_metadata_constant = "CALAFAT2025_FILE_METADATA"
    elif "zheng2024" in file_path.name:
        metadata_constant = "ZHENG2024_METADATA"
        file_metadata_constant = "ZHENG2024_FILE_METADATA"

    # 1. Add YAML metadata loading after log.info statement
    log_pattern = r"(log[._]info\([^)]+\)\s*\n)"
    yaml_loading_code = f"""\\1
    # Load YAML metadata with fallback
    global_metadata, yaml_file_metadata = ReaderUtils.load_array_metadata_with_fallback(
        DATASOURCE_ID, {metadata_constant}
    )

"""

    content = re.sub(log_pattern, yaml_loading_code, content, count=1)

    # 2. Add added_attrs_per_dataset initialization
    datasets_pattern = r"(datasets = \[\]\s*\n)"
    tracking_init = (
        "\\1    added_attrs_per_dataset = [] if track_added_attrs else None\n"
    )
    content = re.sub(datasets_pattern, tracking_init, content, count=1)

    # 3. Replace old metadata attachment with new ReaderUtils pattern
    old_attach_pattern = (
        r"(\s+)# Use ReaderUtils for consistent metadata attachment\s*\n"
        r"\s+file_metadata = " + file_metadata_constant + r"\.get\(file, \{\}\)\s*\n"
        r"\s+ds = ReaderUtils\.attach_standard_metadata\(\s*\n"
        r"\s+ds,\s*\n"
        r"\s+file,\s*\n"
        r"\s+file_path,\s*\n"
        r"\s+" + metadata_constant + r",\s*\n"
        r"\s+file_metadata,\s*\n"
        r"\s+datasource_id=DATASOURCE_ID,?\s*\n"
        r"\s+\)"
    )

    new_attach_code = f"""\\1# Attach metadata with optional tracking
\\1if track_added_attrs:
\\1    ds, attr_changes = ReaderUtils.attach_metadata_with_tracking(
\\1        ds, file, file_path, global_metadata, yaml_file_metadata, 
\\1        {file_metadata_constant}, DATASOURCE_ID, track_added_attrs=True
\\1    )
\\1    added_attrs_per_dataset.append(attr_changes)
\\1else:
\\1    ds = ReaderUtils.attach_metadata_with_tracking(
\\1        ds, file, file_path, global_metadata, yaml_file_metadata,
\\1        {file_metadata_constant}, DATASOURCE_ID, track_added_attrs=False
\\1    )"""

    content = re.sub(
        old_attach_pattern, new_attach_code, content, flags=re.MULTILINE | re.DOTALL
    )

    # 4. Replace TODO track_added_attrs implementation with proper return
    todo_pattern = (
        r"(\s+)# Handle track_added_attrs parameter\s*\n"
        r"\s+if track_added_attrs:\s*\n"
        r"\s+# TODO: Implement actual attribute tracking\s*\n"
        r"\s+# For now, return empty tracking info for compatibility\s*\n"
        r"\s+added_attrs_per_dataset = \[[^\]]+\]\s*\n"
        r"\s+return datasets, added_attrs_per_dataset\s*\n"
        r"\s+else:\s*\n"
        r"\s+return datasets"
    )

    new_return_code = """\\1# Handle track_added_attrs parameter
\\1if track_added_attrs:
\\1    return datasets, added_attrs_per_dataset
\\1else:
\\1    return datasets"""

    content = re.sub(todo_pattern, new_return_code, content, flags=re.MULTILINE)

    # Write back the updated content
    with open(file_path, "w") as f:
        f.write(content)

    print(f"  ✅ Updated {file_path.name}")
    return True


def main():
    """Update all specified readers."""
    print(
        "Updating data source readers with YAML metadata loading and attribute tracking...\n"
    )

    data_sources_dir = Path("amocatlas/data_sources")

    success_count = 0
    for reader_file in READERS_TO_UPDATE:
        file_path = data_sources_dir / reader_file
        if file_path.exists():
            if update_reader_file(file_path):
                success_count += 1
        else:
            print(f"  ❌ File not found: {reader_file}")

    print(f"\n✅ Successfully updated {success_count}/{len(READERS_TO_UPDATE)} readers")
    print("\nNext steps:")
    print("1. Test the updated readers")
    print("2. Generate reports to verify YAML metadata loading")
    print("3. Add TIME coordinate standardization")


if __name__ == "__main__":
    main()
