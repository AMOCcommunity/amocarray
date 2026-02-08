#!/usr/bin/env python3
"""Generate comprehensive dataset reports for AMOCatlas arrays.

This script generates detailed Sphinx RST reports for each observing array,
including variable mapping, metadata analysis, and processing change tracking.
"""

import argparse
import pathlib
import sys
from datetime import datetime, timezone

# Add the project root to the path so we can import amocatlas
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from amocatlas import read
from amocatlas.report import StandardizedDatasetReport, _generate_rst_report


def generate_array_report(array_name: str, output_dir: pathlib.Path) -> pathlib.Path:
    """Generate comprehensive report for a single array.

    Parameters
    ----------
    array_name : str
        Name of the array (e.g., 'rapid', 'osnap', 'move', 'samba')
    output_dir : pathlib.Path
        Directory to write the report

    Returns
    -------
    pathlib.Path
        Path to the generated report file

    """
    print(f"Generating report for {array_name.upper()} array...")

    # Get the read function for this array
    if not hasattr(read, array_name.lower()):
        available_arrays = [
            attr
            for attr in dir(read)
            if not attr.startswith("_") and hasattr(getattr(read, attr), "__call__")
        ]
        raise ValueError(
            f"Unsupported array '{array_name}'. Available arrays: {', '.join(available_arrays)}"
        )

    read_func = getattr(read, array_name.lower())

    try:
        # Load all files for this array with attribute tracking
        datasets, attr_changes_list = read_func(
            all_files=True,
            transport_only=False,
            track_added_attrs=True,
            raw=False,  # Get standardized versions
        )

        print(f"Loaded {len(datasets)} {array_name.upper()} datasets")

        # Build comprehensive RST content
        lines = []
        lines.extend(
            [
                f"{array_name.upper()} Dataset Report",
                "=" * (len(array_name) + 15),
                "",
                f"*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}*",
                "",
                f"This report covers all available {array_name.upper()} datasets with comprehensive analysis.",
                "",
            ]
        )

        # Process each file
        for i, (dataset, attr_changes) in enumerate(zip(datasets, attr_changes_list)):
            source_file = dataset.attrs.get("source_file", f"file_{i}")
            print(f"  Processing {source_file}...")

            try:
                # Create detailed report for this dataset
                report_data = StandardizedDatasetReport(
                    f"{array_name.upper()} {source_file}", dataset, attr_changes
                )

                # Generate the full RST content for this dataset
                # We'll use the existing _generate_rst_report but modify the title
                dataset_rst = _generate_rst_report(report_data)

                # Extract everything after the first title line for inclusion
                rst_lines = dataset_rst.split("\n")

                # Find the first section (after the main title) and include from there
                start_idx = 0
                for j, line in enumerate(rst_lines):
                    if line.startswith("Generated:"):
                        start_idx = j - 2  # Include the filename header
                        break

                # Add the filename as a section header
                lines.extend(
                    [
                        source_file,
                        "-" * len(source_file),
                        "",
                    ]
                )

                # Add the rest of the report content (skip the main title)
                if start_idx > 0:
                    for line in rst_lines[
                        start_idx + 2 :
                    ]:  # Skip filename and underline
                        lines.append(line)
                else:
                    # Fallback: add basic info
                    lines.extend(
                        [
                            "Dataset Overview",
                            "^^^^^^^^^^^^^^^^",
                            "",
                            f"- **Source File**: {source_file}",
                            f'- **Data Product**: {dataset.attrs.get("data_product", "Unknown")}',
                            "",
                            "Note: Full analysis not available for this dataset.",
                            "",
                        ]
                    )

            except Exception as e:
                print(f"    Error processing {source_file}: {e}")
                # Add basic fallback info
                lines.extend(
                    [
                        source_file,
                        "-" * len(source_file),
                        "",
                        "Dataset Overview",
                        "^^^^^^^^^^^^^^^^",
                        "",
                        f"- **Source File**: {source_file}",
                        f'- **Data Product**: {dataset.attrs.get("data_product", "Unknown")}',
                        f"- **Variables**: {list(dataset.data_vars.keys())}",
                        f"- **Coordinates**: {list(dataset.coords.keys())}",
                        "",
                        f"Note: Report generation failed: {e}",
                        "",
                    ]
                )

        # Write the report
        rst_content = "\n".join(lines)
        output_file = output_dir / f"{array_name.lower()}_report.rst"
        output_file.write_text(rst_content)

        print(f"Report written to: {output_file}")
        return output_file

    except Exception as e:
        print(f"Failed to generate report for {array_name}: {e}")
        raise


def main():
    """Main script entry point."""
    parser = argparse.ArgumentParser(description="Generate AMOCatlas dataset reports")
    parser.add_argument(
        "arrays",
        nargs="*",
        default=["rapid"],
        help="Array names to generate reports for (default: rapid)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        type=pathlib.Path,
        default=pathlib.Path("docs/source/reports"),
        help="Output directory for reports",
    )
    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Generate reports for all available arrays",
    )

    args = parser.parse_args()

    # Create output directory if it doesn't exist
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Determine which arrays to process
    if args.all:
        # List of all available arrays
        available_arrays = [
            "rapid",
            "osnap",
            "move",
            "samba",
            "fw2015",
            "mocha",
            "wh41n",
            "dso",
        ]
        arrays_to_process = available_arrays
    else:
        arrays_to_process = args.arrays

    print(f"Generating reports for arrays: {', '.join(arrays_to_process)}")

    # Generate reports
    generated_files = []
    for array_name in arrays_to_process:
        try:
            output_file = generate_array_report(array_name, args.output_dir)
            generated_files.append(output_file)
        except Exception as e:
            print(f"Failed to generate report for {array_name}: {e}")

    print(f"\nGenerated {len(generated_files)} reports:")
    for file_path in generated_files:
        print(f"  {file_path}")

    print("\nTo rebuild documentation: cd docs && make html")


if __name__ == "__main__":
    main()
