#!/usr/bin/env python3
"""Generate RAPID array report for Sphinx documentation.

Usage:
    python generate_rapid_report.py
"""

import sys
from pathlib import Path

# Add the current directory to Python path so we can import amocatlas
sys.path.insert(0, str(Path(__file__).parent))

import amocatlas.report as report


def main():
    """Generate RAPID report and save to docs directory."""
    print("Generating RAPID array report...")

    # Generate the report content
    try:
        content = report.rapid()
        print(f"Generated report with {len(content)} characters")
    except Exception as e:
        print(f"Error generating report: {e}")
        return 1

    # Create output directory if it doesn't exist
    output_dir = Path("docs/source/reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Write the report
    output_file = output_dir / "rapid_all_files_report.rst"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Report saved to: {output_file}")
        print(f"File size: {output_file.stat().st_size} bytes")
    except Exception as e:
        print(f"Error writing report: {e}")
        return 1

    print("\nTo rebuild documentation, run:")
    print("cd docs && make clean html")

    return 0


if __name__ == "__main__":
    exit(main())
