#!/usr/bin/env python3
"""Debug script to trace timing warnings in report generation."""

from amocatlas.report import ReportUtils
from amocatlas import read
import pandas as pd

def debug_time_analysis(dataset_name):
    """Debug time analysis for a specific dataset."""
    print(f"\n=== Debugging {dataset_name.upper()} ===")
    
    # Load all files for the dataset
    if dataset_name == 'wh41n':
        datasets = read.wh41n(all_files=True)
    elif dataset_name == 'move':
        datasets = read.move(all_files=True)
    else:
        print(f"Dataset {dataset_name} not implemented in debug script")
        return
    
    for i, ds in enumerate(datasets):
        print(f"\nDataset {i}: {ds.attrs.get('source_file', 'unknown')}")
        
        # Check what time coordinates exist
        time_coords = [coord for coord in ds.coords if 'time' in coord.lower()]
        print(f"Time coordinates found: {time_coords}")
        
        if not time_coords:
            print("No time coordinates - skipping")
            continue
            
        # Analyze each time coordinate
        for time_coord in time_coords:
            print(f"\nAnalyzing time coordinate: {time_coord}")
            time_var = ds[time_coord]
            
            print(f"  Time dtype: {time_var.dtype}")
            print(f"  Time shape: {time_var.shape}")
            
            # Get the actual values
            time_values = time_var.values
            print(f"  First few values: {time_values[:3]}")
            print(f"  Last few values: {time_values[-3:]}")
            
            # Test the ReportUtils time analysis
            try:
                time_info = ReportUtils._analyze_time_coordinate(ds, time_coord)
                print(f"  Analysis result:")
                print(f"    Start date: {time_info.get('start_date')}")
                print(f"    End date: {time_info.get('end_date')}")  
                print(f"    Time span days: {time_info.get('time_span_days')}")
                print(f"    Time span years: {time_info.get('time_span_years')}")
                print(f"    Warnings: {time_info.get('warnings', [])}")
            except Exception as e:
                print(f"  Error in time analysis: {e}")
                import traceback
                traceback.print_exc()

if __name__ == "__main__":
    debug_time_analysis('wh41n')
    debug_time_analysis('move')