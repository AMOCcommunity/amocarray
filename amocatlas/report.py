"""AMOCatlas Dataset Report Generator.

This module provides automated reporting capabilities for AMOCatlas datasets,
generating comprehensive, human-readable documentation with dataset statistics,
variable mappings, and quality assessments.

Features:
- Dataset analysis and statistical summaries
- Variable mapping tables (original → standardized names)
- Temporal coverage analysis
- Sphinx-compatible RST output
- Quality assessment and metadata validation

Usage:
    >>> from amocatlas import report
    >>> report_data = report.analyze_dataset("rapid26n", transport_only=True)
    >>> rst_output = report.generate_dataset_report("rapid26n")
"""

import pandas as pd
import xarray as xr
from typing import Dict, Any, Optional, List, Union
from pathlib import Path
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for automated plotting

from amocatlas import read, utilities, plotters
from amocatlas.logger import log_info, log_debug


class ReportUtils:
    """Shared utilities for AMOCatlas report generation."""
    
    @staticmethod
    def estimate_frequency(median_diff) -> str:
        """Estimate sampling frequency from median time difference."""
        try:
            # Handle pandas Timedelta
            if hasattr(median_diff, 'total_seconds'):
                hours = median_diff.total_seconds() / 3600
            else:
                # Handle numeric difference (assume days)
                hours = float(median_diff) * 24
        except Exception:
            return "unknown"
        
        if hours < 1:
            try:
                if hasattr(median_diff, 'total_seconds'):
                    return f"{int(median_diff.total_seconds()//60)}min"
                else:
                    return "<1H"
            except:
                return "<1H"
        elif hours < 12:
            return f"{hours:.1f}H"
        elif 10 <= hours <= 14:
            return "12H"
        elif 20 <= hours <= 28:
            return "daily"
        elif 28 <= hours <= 35:
            return "monthly"
        elif 720 <= hours <= 760:  # ~30-31 days 
            return "monthly"
        else:
            return f"{hours:.1f}H"
    
    @staticmethod
    def compute_dataset_statistics(dataset: xr.Dataset) -> Dict[str, Any]:
        """Compute comprehensive dataset statistics."""
        stats = {
            "total_variables": len(dataset.data_vars),
            "total_coordinates": len(dataset.coords),
            "total_attributes": len(dataset.attrs),
            "file_size_mb": dataset.nbytes / (1024 * 1024),
            "variables": {}
        }
        
        # Compute statistics for each data variable
        for var_name, var in dataset.data_vars.items():
            var_stats = {
                "dtype": str(var.dtype),
                "shape": var.shape,
                "dimensions": list(var.dims),
                "has_time": "time" in var.dims or "TIME" in var.dims,
                "units": var.attrs.get("units", "unknown"),
                "long_name": var.attrs.get("long_name", var_name),
                "missing_data_pct": 0.0
            }
            
            # Compute min/max/mean for numeric variables
            if np.issubdtype(var.dtype, np.number):
                # Handle potential NaN values
                valid_data = var.where(np.isfinite(var), drop=True)
                if valid_data.size > 0:
                    var_stats.update({
                        "min": float(valid_data.min().values),
                        "max": float(valid_data.max().values),
                        "mean": float(valid_data.mean().values),
                        "std": float(valid_data.std().values),
                    })
                    # Calculate missing data percentage
                    total_size = var.size
                    valid_size = valid_data.size
                    var_stats["missing_data_pct"] = ((total_size - valid_size) / total_size) * 100
            
            stats["variables"][var_name] = var_stats
        
        return stats
    
    @staticmethod
    def _safe_time_diff_days(time_max, time_min):
        """Safely calculate time difference in days, handling different data types."""
        try:
            # Try standard datetime difference
            diff = time_max - time_min
            if hasattr(diff, 'days'):
                return diff.days
            else:
                # Handle numeric time - check if it looks like seconds since 1970
                try:
                    numeric_diff = float(diff)
                    # Check if the values look like unix timestamps (> 1e9)
                    if max(abs(time_max), abs(time_min)) > 1e9:
                        # Assume difference is in seconds, convert to days
                        return numeric_diff / 86400.0  # seconds to days
                    else:
                        # Assume years 
                        return numeric_diff * 365.25
                except (ValueError, TypeError):
                    return 0
        except Exception:
            # Fallback for any other cases
            return 0
    
    @staticmethod
    def _safe_format_date(date_obj):
        """Safely format date, handling different data types."""
        try:
            if hasattr(date_obj, 'strftime'):
                return date_obj.strftime('%Y-%m-%d')
            else:
                # Check if this looks like seconds since 1970 (unix timestamp)
                try:
                    numeric_val = float(date_obj)
                    if numeric_val > 1e9:  # Likely seconds since 1970
                        import pandas as pd
                        return pd.to_datetime(numeric_val, unit='s').strftime('%Y-%m-%d')
                    else:
                        # Assume it's a year
                        return f"{numeric_val:.1f}"
                except (ValueError, TypeError):
                    return str(date_obj)
        except Exception:
            return str(date_obj)
    
    @staticmethod
    def analyze_temporal_coverage(dataset: xr.Dataset) -> Dict[str, Any]:
        """Analyze temporal coverage of the dataset."""
        # Find time coordinate
        time_coords = []
        for coord_name in dataset.coords:
            if coord_name.lower() in ['time', 'date'] or 'time' in coord_name.lower():
                time_coords.append(coord_name)
        
        if not time_coords:
            return {"has_time": False}
        
        time_coord = time_coords[0]  # Use first time coordinate found
        time_data = dataset[time_coord]
        
        # Convert to pandas datetime if needed
        if hasattr(time_data, 'to_pandas'):
            time_series = time_data.to_pandas()
        else:
            time_values = time_data.values
            # Handle different time formats
            if hasattr(time_values, '__iter__') and len(time_values) > 0:
                # Check the dtype first
                if str(time_data.dtype).startswith('datetime64'):
                    # Already datetime64, just convert to pandas
                    time_series = pd.to_datetime(time_values)
                else:
                    # Numeric values - check if they look like seconds since 1970
                    try:
                        sample_val = float(time_values[0])
                        if sample_val > 1e9:  # Likely seconds since 1970
                            time_series = pd.to_datetime(time_values, unit='s')
                        else:
                            time_series = pd.to_datetime(time_values)
                    except (ValueError, TypeError):
                        time_series = pd.to_datetime(time_values)
            else:
                time_series = pd.to_datetime(time_values)
        
        # Remove invalid times
        valid_times = time_series.dropna()
        
        if len(valid_times) == 0:
            return {"has_time": True, "valid_times": False}
        
        # Calculate temporal statistics
        start_date = valid_times.min()
        end_date = valid_times.max()
        
        time_info = {
            "has_time": True,
            "valid_times": True,
            "coordinate_name": time_coord,
            "start_date": start_date,
            "end_date": end_date,
            "total_records": len(valid_times),
            "time_span_days": ReportUtils._safe_time_diff_days(end_date, start_date),
            "time_span_years": ReportUtils._safe_time_diff_days(end_date, start_date) / 365.25,
        }
        
        # Estimate sampling frequency
        if len(valid_times) > 1:
            time_diffs = valid_times.diff().dropna()
            median_diff = time_diffs.median()
            time_info["median_sampling_interval"] = median_diff
            time_info["estimated_frequency"] = ReportUtils.estimate_frequency(median_diff)
            
            # Add warnings for problematic values
            warnings = []
            
            # Check for extremely long record length (>50 years)
            if time_info["time_span_years"] > 50:
                warnings.append(f"WARNING: Record length of {time_info['time_span_years']:.1f} years seems unusually long")
            
            # Check for extremely high sampling frequency values (>100 hours)
            freq_str = time_info["estimated_frequency"]
            if freq_str.endswith("H") and not freq_str.endswith("min"):
                try:
                    freq_hours = float(freq_str.replace("H", ""))
                    if freq_hours > 100:
                        warnings.append(f"WARNING: Sampling frequency of {freq_hours}H seems unusually high - possible time parsing issue")
                except ValueError:
                    pass
            
            if warnings:
                time_info["warnings"] = warnings
                for warning in warnings:
                    print(f"  {warning}")
        
        return time_info
    
    @staticmethod
    def create_coordinate_info_table(dataset: xr.Dataset) -> pd.DataFrame:
        """Create coordinate information table from dataset coordinates."""
        coord_data = []
        
        for coord_name in dataset.coords:
            coord_var = dataset[coord_name]
            
            # Basic coordinate info
            coord_info = {
                "Coordinate": coord_name,
                "Standardized Name": coord_name,  # No mapping for raw data
                "Description": coord_var.attrs.get("long_name", coord_var.attrs.get("description", "No description available")),
                "Units": coord_var.attrs.get("units", str(coord_var.dtype)),
                "Size": str(coord_var.shape),
                "Min Value": "",  # Will fill below
                "Max Value": "",  # Will fill below
            }
            
            # Try to get min/max values
            try:
                # Special handling for TIME coordinates
                if coord_name == "TIME":
                    
                    # Handle different TIME coordinate formats
                    if coord_var.dtype.kind == 'M':  # datetime64 type
                        # Convert datetime64 directly to readable dates
                        min_date = pd.to_datetime(coord_var.min().values).strftime('%Y-%m-%d')
                        max_date = pd.to_datetime(coord_var.max().values).strftime('%Y-%m-%d')
                        coord_info["Min Value"] = min_date
                        coord_info["Max Value"] = max_date
                    elif coord_var.attrs.get("units", "").startswith("seconds since 1970"):
                        # Handle seconds since 1970 (standardized format)
                        min_timestamp = float(coord_var.min())
                        max_timestamp = float(coord_var.max())
                        
                        min_date = pd.to_datetime(min_timestamp, unit='s').strftime('%Y-%m-%d')
                        max_date = pd.to_datetime(max_timestamp, unit='s').strftime('%Y-%m-%d')
                        
                        coord_info["Min Value"] = min_date
                        coord_info["Max Value"] = max_date
                    else:
                        # Fallback to numeric handling
                        coord_info["Min Value"] = f"{float(coord_var.min()):.2f}"
                        coord_info["Max Value"] = f"{float(coord_var.max()):.2f}"
                elif coord_var.dtype.kind in ['f', 'i']:  # Numeric data
                    coord_info["Min Value"] = f"{float(coord_var.min()):.2f}"
                    coord_info["Max Value"] = f"{float(coord_var.max()):.2f}"
                elif coord_var.dtype.kind == 'M':  # Datetime
                    coord_info["Min Value"] = str(coord_var.min().values)[:10]  # Just date part
                    coord_info["Max Value"] = str(coord_var.max().values)[:10]  # Just date part
                else:
                    coord_info["Min Value"] = str(coord_var.values[0])
                    coord_info["Max Value"] = str(coord_var.values[-1])
            except Exception:
                coord_info["Min Value"] = "N/A"
                coord_info["Max Value"] = "N/A"
            
            coord_data.append(coord_info)
        
        return pd.DataFrame(coord_data)
    
    @staticmethod
    def create_variable_mapping_table(dataset: xr.Dataset, statistics: Dict[str, Any], metadata: Dict[str, Any]) -> pd.DataFrame:
        """Create variable mapping table from dataset metadata and statistics."""
        # Use only what's in the dataset metadata - no separate YAML loading
        files_metadata = metadata.get("files", {})
        
        if not files_metadata:
            return pd.DataFrame()
        
        # Find the transport file or use the first file
        transport_files = ["moc_transports.nc", "transport.nc", "transports.nc"]
        file_key = None
        
        # Get source file from dataset attributes
        source_file = dataset.attrs.get("source_file", "")
        if source_file in files_metadata:
            file_key = source_file
        else:
            # Fallback to transport files
            for transport_file in transport_files:
                if transport_file in files_metadata:
                    file_key = transport_file
                    break
        
        if not file_key:
            # Check if files metadata exists and has entries
            if files_metadata:
                file_key = list(files_metadata.keys())[0]
            else:
                # No files metadata available, use fallback
                file_key = None
        
        if file_key and file_key in files_metadata:
            file_meta = files_metadata[file_key]
            variable_mapping = file_meta.get("variable_mapping", {})
            variables_meta = file_meta.get("variables", {})
        else:
            # Fall back to empty mappings
            variable_mapping = {}
            variables_meta = {}
        
        mapping_data = []
        
        for orig_var in dataset.data_vars:
            # Get standardized name from mapping, default to original if not mapped
            standardized_name = variable_mapping.get(orig_var, orig_var)
            
            # Get variable metadata
            var_meta = variables_meta.get(orig_var, {})
            var_data = dataset[orig_var]
            var_stats = statistics["variables"].get(orig_var, {})
            
            # Get description and long_name from metadata or attributes
            description = var_meta.get("description", var_data.attrs.get("description", ""))
            long_name = var_meta.get("long_name", var_data.attrs.get("long_name", ""))
            
            # Create display description: prioritize description, then add long_name in bold
            if description:
                if long_name and long_name != orig_var and long_name != description:
                    display_description = f"**{long_name}**: {description}"
                else:
                    display_description = description
            elif long_name and long_name != orig_var:
                display_description = long_name
            else:
                display_description = "No description available"
            
            # Get size from variable - show shape instead of total elements
            if hasattr(var_data, 'shape'):
                size = str(var_data.shape)
            elif hasattr(var_data, 'size'):
                size = str(var_data.size)
            else:
                size = "unknown"
            
            row = {
                "Original Variable": orig_var,
                "Standardized Name": standardized_name,
                "Description": display_description,
                "Units": var_meta.get("units", var_data.attrs.get("units", "unknown")),
                "Data Type": var_stats.get("dtype", "unknown"),
                "Dimensions": str(var_stats.get("dimensions", [])),
                "Size": size,
                "Min Value": var_stats.get("min", "N/A"),
                "Max Value": var_stats.get("max", "N/A"),
                "Missing %": f"{var_stats.get('missing_data_pct', 0.0):.1f}%"
            }
            mapping_data.append(row)
        
        return pd.DataFrame(mapping_data)
    
    @staticmethod
    def generate_plot(dataset: xr.Dataset, dataset_name: str) -> Optional[str]:
        """Generate a plot for the dataset and return the relative path."""
        try:
            # Create reports plots directory if it doesn't exist
            plots_dir = Path("docs/source/_static/reports")
            plots_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate plot filename (clean dataset name for filename)
            clean_name = dataset_name.replace(" ", "_").replace(".nc", "")
            plot_filename = f"{clean_name}_timeseries.png"
            plot_path = plots_dir / plot_filename
            
            # Find 1-dimensional time series variables indexed against time
            data_vars = list(dataset.data_vars.keys())
            time_coords = [coord for coord in dataset.coords if 'time' in coord.lower()]
            
            if not time_coords:
                print(f"  No time coordinate found in {dataset_name}")
                return None
            
            time_coord = time_coords[0]  # Use first time coordinate
            
            # Find 1D time series variables
            timeseries_vars = []
            for var in data_vars:
                var_data = dataset[var]
                # Check if variable is 1D and has time as its dimension
                if (len(var_data.dims) == 1 and 
                    time_coord in var_data.dims and
                    var_data.dtype.kind in ['f', 'i'] and  # numeric
                    'flag' not in var.lower()):  # not a flag variable
                    timeseries_vars.append(var)
            
            if not timeseries_vars:
                print(f"  No 1D time series variables found in {dataset_name}")
                return None
            
            # Prioritize variables by type for time series
            moc_vars = [var for var in timeseries_vars if 'moc' in var.lower()]
            transport_vars = [var for var in timeseries_vars if any(x in var.lower() for x in ['transport', '_t_', 't_', 'stream'])]
            temp_vars = [var for var in timeseries_vars if any(x in var.lower() for x in ['temp', 'tg_'])]
            
            # Choose variable to plot in order of preference
            if moc_vars:
                var_to_plot = moc_vars[0]
                plot_type = "MOC"
            elif transport_vars:
                var_to_plot = transport_vars[0]
                plot_type = "Transport"
            elif temp_vars:
                var_to_plot = temp_vars[0]
                plot_type = "Temperature"
            else:
                var_to_plot = timeseries_vars[0]
                plot_type = "Time Series"
            
            print(f"  Generating plot for {dataset_name} using variable: {var_to_plot}")
            
            # Use plotters to create the plot
            title = f"{dataset_name.upper()} {plot_type} Time Series"
            fig, ax = plotters.plot_amoc_timeseries(
                dataset, 
                varnames=[var_to_plot],
                title=title,
                resample_monthly=False,
                plot_raw=True,
                figsize=(8, 3)
            )
            
            # Customize plot
            if hasattr(fig, 'get_axes') and fig.get_axes():
                ax = fig.get_axes()[0]
                if hasattr(ax, 'legend'):
                    legend = ax.legend()
                    if legend:
                        legend.set_visible(False)
            
            # Save plot
            fig.savefig(plot_path, dpi=150, bbox_inches='tight', facecolor='white')
            
            # Import matplotlib.pyplot if not already imported
            try:
                import matplotlib.pyplot as plt
                plt.close(fig)
            except:
                pass
            
            # Return relative path for Sphinx (from reports directory)
            return f"../_static/reports/{plot_filename}"
            
        except Exception as e:
            print(f"  Warning: Failed to generate plot for {dataset_name}: {e}")
            log_debug(f"Plot generation failed for {dataset_name}: {e}")
            return None
    
    @staticmethod
    def generate_array_report(array_name: str, all_files: bool = True, output_file: str = None) -> str:
        """Generate comprehensive report for any array following the read.{array}() pattern.
        
        Parameters
        ----------
        array_name : str
            Name of the array (e.g., 'rapid', 'osnap', 'move', 'samba')
        all_files : bool, optional
            Whether to include all files in the report, by default True
        output_file : str, optional
            Path to write the RST report. If None, returns RST content as string.
            
        Returns
        -------
        str
            RST content of the report
            
        Examples
        --------
        >>> from amocatlas.report import ReportUtils
        >>> rst_content = ReportUtils.generate_array_report('rapid')
        >>> rst_content = ReportUtils.generate_array_report('osnap', all_files=False)
        """
        from amocatlas import read
        import pathlib
        
        print(f'Loading {array_name.upper()} datasets for report generation...')
        
        # Get the read function for this array
        read_func = getattr(read, array_name.lower())
        
        # Load datasets with attribute tracking (if supported)
        try:
            # Try with tracking first
            result = read_func(
                all_files=all_files,
                transport_only=not all_files,  # If all_files=False, only transport
                track_added_attrs=True,
                raw=False  # Use standardized data
            )
        except TypeError as e:
            if 'track_added_attrs' in str(e):
                # Reader doesn't support tracking, use without it
                print(f"  Note: {array_name} reader doesn't support metadata tracking yet")
                result = read_func(
                    all_files=all_files,
                    transport_only=not all_files,
                    track_added_attrs=False,
                    raw=False
                )
            else:
                raise
        
        # Handle both single dataset and multiple dataset returns
        if isinstance(result, tuple):
            datasets_or_dataset, attr_changes_or_list = result
            if isinstance(datasets_or_dataset, list):
                datasets = datasets_or_dataset
                attr_changes_list = attr_changes_or_list
            else:
                # Single dataset returned
                datasets = [datasets_or_dataset]
                attr_changes_list = [attr_changes_or_list]
        else:
            # No tracking enabled, fallback
            if isinstance(result, list):
                datasets = result
                attr_changes_list = [{"added": [], "modified": []} for _ in datasets]
            else:
                datasets = [result]
                attr_changes_list = [{"added": [], "modified": []}]
        
        print(f'Loaded {len(datasets)} {array_name.upper()} datasets')
        
        if len(datasets) == 1:
            # Single dataset - use standard report generation
            dataset = datasets[0]
            attr_changes = attr_changes_list[0]
            
            report_data = StandardizedDatasetReport(f'{array_name.upper()}', dataset, attr_changes)
            rst_content = _generate_rst_report(report_data)
            
        else:
            # Multiple datasets - create comprehensive report
            lines = []
            lines.extend([
                f'{array_name.upper()} Dataset Report',
                '=' * (len(array_name) + 15),
                '',
                f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                '',
                f'This report covers all available {array_name.upper()} datasets.',
                '',
            ])
            
            for i, (dataset, attr_changes) in enumerate(zip(datasets, attr_changes_list)):
                source_file = dataset.attrs.get('source_file', f'dataset_{i}')
                print(f'Processing {source_file}...')
                
                try:
                    # Create report for this individual dataset (use just source_file as name)
                    report_data = StandardizedDatasetReport(source_file.replace('.nc', ''), dataset, attr_changes)
                    
                    # Generate individual report and extract content
                    individual_rst = _generate_rst_report(report_data, skip_source_header=True)
                    rst_lines = individual_rst.split('\n')
                    
                    # Add filename as section header
                    lines.extend([
                        source_file,
                        '-' * len(source_file),
                        '',
                    ])
                    
                    # Find where the actual content starts (skip the main title and header)
                    content_start = 0
                    skip_title = True
                    for j, line in enumerate(rst_lines):
                        if skip_title and line.startswith('====='):
                            # Found end of title, skip next few lines 
                            content_start = j + 3
                            skip_title = False
                            break
                        elif line.startswith('Dataset Overview') or line.startswith('Coordinate Information'):
                            content_start = j
                            break
                    
                    # Add the content (everything after the main title)
                    if content_start > 0 and content_start < len(rst_lines):
                        for line in rst_lines[content_start:]:
                            lines.append(line)
                    else:
                        # Fallback to basic info if parsing fails
                        lines.extend([
                            'Dataset Overview',
                            '^^^^^^^^^^^^^^^^',
                            '',
                            f'- **Source File**: {source_file}',
                            f'- **Variables**: {list(dataset.data_vars.keys())}',
                            f'- **Coordinates**: {list(dataset.coords.keys())}',
                            '',
                            'Note: Full report generation failed - showing basic information.',
                            '',
                        ])
                        
                except Exception as e:
                    print(f'Error processing {source_file}: {e}')
                    import traceback
                    print(f'Full traceback: {traceback.format_exc()}')
                    # Add basic fallback
                    lines.extend([
                        'Dataset Overview',
                        '^^^^^^^^^^^^^^^^',
                        '',
                        f'- **Source File**: {source_file}',
                        f'- **Error**: Could not generate full analysis - {e}',
                        '',
                    ])
            
            rst_content = '\n'.join(lines)
        
        # Write to file if requested
        if output_file:
            output_path = pathlib.Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(rst_content)
            print(f'Report written to: {output_path}')
        
        return rst_content
    
    @staticmethod
    def dataframe_to_rst_table(df: pd.DataFrame) -> List[str]:
        """Convert pandas DataFrame to RST table format."""
        if df.empty:
            return ["(No data available)"]
        
        # Use all available columns - the calling function should provide the right subset
        display_df = df.copy()
        
        # Format numeric columns
        for col in ["Min Value", "Max Value"]:
            if col in display_df.columns:
                display_df[col] = display_df[col].apply(lambda x: f"{x:.2f}" if isinstance(x, (int, float)) and not pd.isna(x) else str(x))
        
        lines = []
        
        # Calculate column widths
        col_widths = {}
        for col in display_df.columns:
            col_widths[col] = max(
                len(str(col)),
                display_df[col].astype(str).str.len().max() if not display_df[col].empty else 0
            )
        
        # Create header separator
        header_sep = "+" + "+".join("-" * (col_widths[col] + 2) for col in display_df.columns) + "+"
        
        # Add table
        lines.append(header_sep)
        
        # Add header row
        header_row = "|" + "|".join(f" {col:<{col_widths[col]}} " for col in display_df.columns) + "|"
        lines.append(header_row)
        
        # Add header separator
        header_sep2 = "+" + "+".join("=" * (col_widths[col] + 2) for col in display_df.columns) + "+"
        lines.append(header_sep2)
        
        # Add data rows
        for _, row in display_df.iterrows():
            data_row = "|" + "|".join(f" {str(row[col]):<{col_widths[col]}} " for col in display_df.columns) + "|"
            lines.append(data_row)
            lines.append(header_sep)
        
        lines.append("")
        return lines


class BaseDatasetReport:
    """Base class for dataset analysis results."""
    
    def __init__(self, dataset_name: str, dataset: xr.Dataset):
        self.dataset_name = dataset_name
        self.dataset = dataset
        self.analysis_time = datetime.now()
        
        # Computed properties
        self._statistics = None
        self._temporal_info = None
        self._coordinate_info = None
        self._plot_path = None

class RawDatasetReport(BaseDatasetReport):
    """Report generator for raw (unprocessed) datasets."""
    
    def __init__(self, dataset_name: str, dataset: xr.Dataset, added_attrs: list[str] = None):
        super().__init__(dataset_name, dataset)
        # Filter out AMOCatlas-added attributes to get truly raw metadata
        if added_attrs:
            self.metadata = {k: v for k, v in dataset.attrs.items() if k not in added_attrs}
        else:
            self.metadata = dict(dataset.attrs)  # Fallback to all attrs if no tracking
        
        # Store added attributes for reference
        self.added_attrs = added_attrs or []
        
        # No variable mapping for raw data
        self._variable_mapping = None


class StandardizedDatasetReport(BaseDatasetReport):
    """Report generator for standardized datasets with variable mapping and metadata tracking."""
    
    def __init__(self, dataset_name: str, dataset: xr.Dataset, attr_changes: dict = None):
        super().__init__(dataset_name, dataset)
        # Use all metadata (includes AMOCatlas standardization)
        self.metadata = dict(dataset.attrs)
        
        # Store attribute changes for highlighting
        self.attr_changes = attr_changes or {"added": [], "modified": []}
        
        # Initialize variable mapping (will be computed lazily)
        self._variable_mapping = None
        
    @property 
    def metadata_changes_summary(self) -> str:
        """Return a summary of metadata changes for display."""
        lines = []
        added = self.attr_changes.get("added", [])
        modified = self.attr_changes.get("modified", [])
        
        if added:
            lines.append("**Added by AMOCatlas processing:**")
            lines.append("")
            for attr in added:
                # Skip 'files', 'variables', and 'coordinates' attributes
                if attr.lower() in ['files', 'variables', 'coordinates']:
                    continue
                value = self.metadata.get(attr, "")
                lines.append(f"- **{attr.replace('_', ' ').title()}**: {value}")
            lines.append("")
            
        if modified:
            lines.append("**Modified by AMOCatlas processing:**")
            lines.append("")
            for attr in modified:
                # Skip 'files', 'variables', and 'coordinates' attributes
                if attr.lower() in ['files', 'variables', 'coordinates']:
                    continue
                value = self.metadata.get(attr, "")
                lines.append(f"- **{attr.replace('_', ' ').title()}**: {value}")
            lines.append("")
            
        if not added and not modified:
            lines.append("*No metadata modifications detected.*")
            lines.append("")
            
        return "\n".join(lines)
    
    @property
    def variable_mapping(self) -> pd.DataFrame:
        """Standardized data may have variable mapping - returns empty DataFrame if none available."""
        if self._variable_mapping is None:
            try:
                self._variable_mapping = self._create_variable_mapping_table()
            except Exception:
                # If mapping fails, return empty DataFrame
                self._variable_mapping = pd.DataFrame()
        return self._variable_mapping
    
    
    @property  
    def coordinate_info(self) -> pd.DataFrame:
        """Get coordinate information table for raw data."""
        if self._coordinate_info is None:
            self._coordinate_info = ReportUtils.create_coordinate_info_table(self.dataset)
        return self._coordinate_info
    
    @property
    def statistics(self) -> Dict[str, Any]:
        """Get dataset statistics."""
        if self._statistics is None:
            self._statistics = ReportUtils.compute_dataset_statistics(self.dataset)
        return self._statistics
    
    @property
    def variable_mapping(self) -> pd.DataFrame:
        """Get variable mapping table."""
        if self._variable_mapping is None:
            self._variable_mapping = ReportUtils.create_variable_mapping_table(
                self.dataset, self.statistics, self.metadata
            )
        return self._variable_mapping
    
    @property
    def temporal_info(self) -> Dict[str, Any]:
        """Get temporal coverage information."""
        if self._temporal_info is None:
            self._temporal_info = ReportUtils.analyze_temporal_coverage(self.dataset)
        return self._temporal_info
    
    @property
    def plot_path(self) -> Optional[str]:
        """Get path to generated plot."""
        if self._plot_path is None:
            self._plot_path = ReportUtils.generate_plot(self.dataset, self.dataset_name)
        return self._plot_path
    
    def _compute_statistics(self) -> Dict[str, Any]:
        """Compute comprehensive dataset statistics."""
        stats = {
            "total_variables": len(self.dataset.data_vars),
            "total_coordinates": len(self.dataset.coords),
            "total_attributes": len(self.dataset.attrs),
            "file_size_mb": self.dataset.nbytes / (1024 * 1024),
            "variables": {}
        }
        
        # Compute statistics for each data variable
        for var_name, var in self.dataset.data_vars.items():
            var_stats = {
                "dtype": str(var.dtype),
                "shape": var.shape,
                "dimensions": list(var.dims),
                "has_time": "time" in var.dims or "TIME" in var.dims,
                "units": var.attrs.get("units", "unknown"),
                "long_name": var.attrs.get("long_name", var_name),
                "missing_data_pct": 0.0
            }
            
            # Compute min/max/mean for numeric variables
            if np.issubdtype(var.dtype, np.number):
                # Handle potential NaN values
                valid_data = var.where(np.isfinite(var), drop=True)
                if valid_data.size > 0:
                    var_stats.update({
                        "min": float(valid_data.min().values),
                        "max": float(valid_data.max().values),
                        "mean": float(valid_data.mean().values),
                        "std": float(valid_data.std().values),
                    })
                    # Calculate missing data percentage
                    total_size = var.size
                    valid_size = valid_data.size
                    var_stats["missing_data_pct"] = ((total_size - valid_size) / total_size) * 100
            
            stats["variables"][var_name] = var_stats
        
        return stats
    
    def _create_variable_mapping_table(self) -> pd.DataFrame:
        """Create variable mapping table from metadata."""
        # Get the first file's metadata (for transport_only, should be transport file)
        if "files" not in self.metadata:
            return pd.DataFrame()
        
        # Find the transport file or use the first file
        transport_files = ["moc_transports.nc", "transport.nc", "transports.nc"]
        file_key = None
        
        for transport_file in transport_files:
            if transport_file in self.metadata["files"]:
                file_key = transport_file
                break
        
        if not file_key:
            # Check if files metadata exists
            if "files" in self.metadata and self.metadata["files"]:
                file_key = list(self.metadata["files"].keys())[0]
            else:
                # No files metadata, fall back to looking for variable_mapping directly
                file_key = None
        
        if file_key and "files" in self.metadata:
            file_meta = self.metadata["files"][file_key]
            variable_mapping = file_meta.get("variable_mapping", {})
            variables_meta = file_meta.get("variables", {})
        else:
            # Fall back to dataset-level metadata
            variable_mapping = self.metadata.get("variable_mapping", {})
            variables_meta = self.metadata.get("variables", {})
        
        mapping_data = []
        
        for orig_var in self.dataset.data_vars:
            # Get standardized name from mapping, default to original if not mapped
            standardized_name = variable_mapping.get(orig_var, orig_var)
            
            # Get variable metadata
            var_meta = variables_meta.get(orig_var, {})
            var_data = self.dataset[orig_var]
            var_stats = self.statistics["variables"].get(orig_var, {})
            
            # Get description and long_name from metadata or attributes
            description = var_meta.get("description", var_data.attrs.get("description", ""))
            long_name = var_meta.get("long_name", var_data.attrs.get("long_name", ""))
            
            # Create display description: prioritize description, then add long_name in bold
            if description:
                if long_name and long_name != orig_var and long_name != description:
                    display_description = f"**{long_name}**: {description}"
                else:
                    display_description = description
            elif long_name and long_name != orig_var:
                display_description = long_name
            else:
                display_description = "No description available"
            
            # Get size from variable - show shape instead of total elements
            if hasattr(var_data, 'shape'):
                size = str(var_data.shape)
            elif hasattr(var_data, 'size'):
                size = str(var_data.size)
            else:
                size = "unknown"
            
            row = {
                "Original Variable": orig_var,
                "Standardized Name": standardized_name,
                "Description": display_description,
                "Units": var_meta.get("units", var_data.attrs.get("units", "unknown")),
                "Data Type": var_stats.get("dtype", "unknown"),
                "Dimensions": str(var_stats.get("dimensions", [])),
                "Size": size,
                "Min Value": var_stats.get("min", "N/A"),
                "Max Value": var_stats.get("max", "N/A"),
                "Missing %": f"{var_stats.get('missing_data_pct', 0.0):.1f}%"
            }
            mapping_data.append(row)
        
        return pd.DataFrame(mapping_data)
    
    def _analyze_temporal_coverage(self) -> Dict[str, Any]:
        """Analyze temporal coverage of the dataset."""
        # Find time coordinate
        time_coords = []
        for coord_name in self.dataset.coords:
            if coord_name.lower() in ['time', 'date'] or 'time' in coord_name.lower():
                time_coords.append(coord_name)
        
        if not time_coords:
            return {"has_time": False}
        
        time_coord = time_coords[0]  # Use first time coordinate found
        time_data = self.dataset[time_coord]
        
        # Convert to pandas datetime if needed
        if hasattr(time_data, 'to_pandas'):
            time_series = time_data.to_pandas()
        else:
            time_values = time_data.values
            # Handle different time formats
            if hasattr(time_values, '__iter__') and len(time_values) > 0:
                # Check the dtype first
                if str(time_data.dtype).startswith('datetime64'):
                    # Already datetime64, just convert to pandas
                    time_series = pd.to_datetime(time_values)
                else:
                    # Numeric values - check if they look like seconds since 1970
                    try:
                        sample_val = float(time_values[0])
                        if sample_val > 1e9:  # Likely seconds since 1970
                            time_series = pd.to_datetime(time_values, unit='s')
                        else:
                            time_series = pd.to_datetime(time_values)
                    except (ValueError, TypeError):
                        time_series = pd.to_datetime(time_values)
            else:
                time_series = pd.to_datetime(time_values)
        
        # Remove invalid times
        valid_times = time_series.dropna()
        
        if len(valid_times) == 0:
            return {"has_time": True, "valid_times": False}
        
        # Calculate temporal statistics
        start_date = valid_times.min()
        end_date = valid_times.max()
        
        time_info = {
            "has_time": True,
            "valid_times": True,
            "coordinate_name": time_coord,
            "start_date": start_date,
            "end_date": end_date,
            "total_records": len(valid_times),
            "time_span_days": ReportUtils._safe_time_diff_days(end_date, start_date),
            "time_span_years": ReportUtils._safe_time_diff_days(end_date, start_date) / 365.25,
        }
        
        # Estimate sampling frequency
        if len(valid_times) > 1:
            time_diffs = valid_times.diff().dropna()
            median_diff = time_diffs.median()
            time_info["median_sampling_interval"] = median_diff
            time_info["estimated_frequency"] = self._estimate_frequency(median_diff)
        
        return time_info
    
    def _estimate_frequency(self, median_diff: pd.Timedelta) -> str:
        """Estimate sampling frequency from median time difference."""
        hours = median_diff.total_seconds() / 3600
        
        if hours < 1:
            return f"{int(median_diff.total_seconds()//60)}min"
        elif hours < 12:
            return f"{hours:.1f}H"
        elif 10 <= hours <= 14:
            return "12H"
        elif 20 <= hours <= 28:
            return "daily"
        elif 28 <= hours <= 35:
            return "monthly"
        elif 720 <= hours <= 760:  # ~30-31 days 
            return "monthly"
        else:
            return f"{hours:.1f}H"
    
    def _generate_plot(self) -> Optional[str]:
        """Generate a plot for the dataset and return the path."""
        try:
            # Create reports plots directory if it doesn't exist
            plots_dir = Path("docs/source/_static/reports")
            plots_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate plot filename
            plot_filename = f"{self.dataset_name}_timeseries.png"
            plot_path = plots_dir / plot_filename
            
            # Try to find a suitable variable for plotting (prefer MOC variables)
            moc_vars = [var for var in self.dataset.data_vars if 'moc' in var.lower()]
            if moc_vars:
                var_to_plot = moc_vars[0]
            else:
                # Fall back to first variable
                var_to_plot = list(self.dataset.data_vars)[0]
            
            # Use plotters to create the plot without monthly resampling
            # Figure size: 2/3rds as wide, maintaining aspect ratio
            title = f"{self.dataset_name.upper()} Time Series"
            fig, ax = plotters.plot_amoc_timeseries(
                self.dataset, 
                varnames=[var_to_plot],
                title=title,
                resample_monthly=False,
                plot_raw=True,
                figsize=(7, 2.5)  # Slightly wider figure
            )
            
            # Turn off legend and save the plot
            ax = fig.get_axes()[0]
            ax.legend().set_visible(False)
            fig.savefig(plot_path, dpi=150, bbox_inches='tight')
            plt.close(fig)
            
            # Return relative path for Sphinx (from reports directory)
            return f"../_static/reports/{plot_filename}"
            
        except Exception as e:
            log_debug(f"Failed to generate plot for {self.dataset_name}: {e}")
            return None


def analyze_standardized_dataset(dataset_name: str, transport_only: bool = True, all_files: bool = False, dataset_index: int = 0) -> Union[StandardizedDatasetReport, List[StandardizedDatasetReport]]:
    """Analyze a standardized dataset and return comprehensive report data with metadata tracking.
    
    Parameters
    ----------
    dataset_name : str
        Name of the dataset (e.g., "rapid", "move")
    transport_only : bool, optional
        Whether to load transport-only data, by default True
    dataset_index : int, optional
        Index of dataset to analyze when multiple files available, by default 0
    
    Returns
    -------
    StandardizedDatasetReport
        Comprehensive analysis results with variable mapping and metadata tracking
    
    Examples
    --------
    >>> report_data = analyze_standardized_dataset("rapid", transport_only=True)
    >>> print(f"Dataset has {report_data.statistics['total_variables']} variables")
    >>> print(f"Added attributes: {report_data.attr_changes['added']}")
    """
    from amocatlas import read
    
    # Get the read function for this dataset
    read_func = getattr(read, dataset_name.lower())
    
    # Load standardized data with attribute tracking
    dataset, attr_changes = read_func(
        transport_only=transport_only, 
        raw=False,  # Get standardized data
        track_added_attrs=True
    )
    
    return StandardizedDatasetReport(dataset_name, dataset, attr_changes)


def analyze_dataset(dataset_name: str, transport_only: bool = True, dataset_index: int = 0) -> RawDatasetReport:
    """Analyze a dataset and return comprehensive report data.
    
    Parameters
    ----------
    dataset_name : str
        Name of the dataset (e.g., "rapid26n", "move16n")
    transport_only : bool, optional
        Whether to load transport-only data, by default True
    dataset_index : int, optional
        Index of dataset to analyze when multiple files available, by default 0
    
    Returns
    -------
    DatasetReport
        Comprehensive analysis results
    
    Examples
    --------
    >>> report_data = analyze_dataset("rapid26n", transport_only=True)
    >>> print(f"Dataset has {report_data.statistics['total_variables']} variables")
    >>> # Analyze second RAPID dataset
    >>> report_data = analyze_dataset("rapid", transport_only=False, dataset_index=1)
    """
    log_info(f"Analyzing dataset: {dataset_name}")
    
    # Load the dataset using the read API
    read_func = getattr(read, dataset_name.replace("26n", "").replace("16n", "").replace("34s", "").replace("55n", "").replace("47n", "noac47n").replace("41n", "wh41n"))
    
    # Load dataset with raw=True and track added attributes to get truly raw metadata
    if dataset_name.lower() == 'rapid' and not transport_only:
        result = read_func(all_files=True, raw=True, track_added_attrs=True)
        if isinstance(result, tuple):
            datasets, added_attrs_list = result
            # Handle both list and single dataset cases
            if isinstance(datasets, list):
                if dataset_index >= len(datasets):
                    raise ValueError(f"Dataset index {dataset_index} out of range. Available datasets: 0-{len(datasets)-1}")
                dataset = datasets[dataset_index]
                added_attrs = added_attrs_list[dataset_index]
            else:
                # Single dataset returned
                if dataset_index != 0:
                    raise ValueError(f"Dataset index {dataset_index} out of range. Only one dataset available.")
                dataset = datasets
                added_attrs = added_attrs_list
        else:
            # Fallback if tracking not supported
            datasets = result
            # Handle both list and single dataset cases
            if isinstance(datasets, list):
                if dataset_index >= len(datasets):
                    raise ValueError(f"Dataset index {dataset_index} out of range. Available datasets: 0-{len(datasets)-1}")
                dataset = datasets[dataset_index]
            else:
                # Single dataset returned
                if dataset_index != 0:
                    raise ValueError(f"Dataset index {dataset_index} out of range. Only one dataset available.")
                dataset = datasets
            added_attrs = []
    else:
        result = read_func(transport_only=transport_only, raw=True, track_added_attrs=True)
        if isinstance(result, tuple):
            datasets, added_attrs_list = result
            # Handle both list and single dataset cases
            if isinstance(datasets, list):
                if dataset_index >= len(datasets):
                    raise ValueError(f"Dataset index {dataset_index} out of range. Available datasets: 0-{len(datasets)-1}")
                dataset = datasets[dataset_index]
                added_attrs = added_attrs_list[dataset_index]
            else:
                # Single dataset returned
                if dataset_index != 0:
                    raise ValueError(f"Dataset index {dataset_index} out of range. Only one dataset available.")
                dataset = datasets
                added_attrs = added_attrs_list
        else:
            # Fallback if tracking not supported
            datasets = result
            # Handle both list and single dataset cases
            if isinstance(datasets, list):
                if dataset_index >= len(datasets):
                    raise ValueError(f"Dataset index {dataset_index} out of range. Available datasets: 0-{len(datasets)-1}")
                dataset = datasets[dataset_index]
            else:
                # Single dataset returned
                if dataset_index != 0:
                    raise ValueError(f"Dataset index {dataset_index} out of range. Only one dataset available.")
                dataset = datasets
            added_attrs = []
    
    log_debug(f"Loaded dataset with {len(dataset.data_vars)} variables, {len(added_attrs)} attributes added by AMOCatlas")
    
    return RawDatasetReport(dataset_name, dataset, added_attrs)


def generate_dataset_report(dataset_name: str, transport_only: bool = True, 
                          output_format: str = "rst", dataset_index: int = 0) -> str:
    """Generate a comprehensive dataset report.
    
    Parameters
    ----------
    dataset_name : str
        Name of the dataset to report on
    transport_only : bool, optional
        Whether to analyze transport-only data, by default True
    output_format : str, optional
        Output format ("rst", "markdown", "html"), by default "rst"
    dataset_index : int, optional
        Index of dataset to analyze when multiple files available, by default 0
    
    Returns
    -------
    str
        Generated report in the specified format
    """
    # Analyze the standardized dataset (with variable mapping and metadata tracking)
    report_data = analyze_standardized_dataset(dataset_name, transport_only=transport_only, dataset_index=dataset_index)
    
    if output_format.lower() == "rst":
        return _generate_rst_report(report_data)
    else:
        raise NotImplementedError(f"Output format '{output_format}' not yet implemented")


def _generate_rst_report(report_data: BaseDatasetReport, skip_source_header: bool = False) -> str:
    """Generate RST-formatted report.
    
    Parameters
    ----------
    report_data : BaseDatasetReport
        Report data to format
    skip_source_header : bool, optional
        If True, skip adding the source file header (for multi-dataset reports)
    """
    dataset_name = report_data.dataset_name
    stats = report_data.statistics
    temporal = report_data.temporal_info
    mapping_df = report_data.variable_mapping
    coordinate_df = report_data.coordinate_info
    # Use regular metadata for display
    metadata = report_data.metadata if hasattr(report_data, 'metadata') else {}
    
    # Build the RST content
    lines = []
    
    # Title  
    title = f"{dataset_name.upper()} Dataset Report"
    lines.extend([
        title,
        "=" * len(title),
        "",
        f"Generated: {report_data.analysis_time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ])
    
    # Source file as level 2 header (skip if requested)
    if not skip_source_header:
        source_file = report_data.dataset.attrs.get('source_file', 'Unknown source')
        lines.extend([
            source_file,
            "-" * len(source_file),
            "",
        ])
    
    # Dataset Overview  
    lines.extend([
        "Dataset Overview",
        "^^^^^^^^^^^^^^^^",
        "",
    ])
    
    if metadata:
        # Use case-insensitive lookup for common fields
        def get_field(field_name, default='Unknown'):
            # Try exact match first
            if field_name in metadata:
                return metadata[field_name]
            # Try capitalized version
            cap_field = field_name.capitalize()
            if cap_field in metadata:
                return metadata[cap_field]
            # Try title case version
            title_field = field_name.replace('_', ' ').title().replace(' ', '_')
            if title_field in metadata:
                return metadata[title_field]
            return default
        
        lines.extend([
            f"- **Project**: {get_field('project')}",
            f"- **Description**: {get_field('description', 'No description available')}",
        ])
        
        # Citation field
        citation = get_field('citation')
        if citation and citation != 'Unknown':
            lines.append(f"- **Citation**: {citation}")
        
        # Acknowledgement field  
        acknowledgement = get_field('acknowledgement')
        if acknowledgement and acknowledgement != 'Unknown':
            lines.append(f"- **Acknowledgement**: {acknowledgement}")
        
        # Website field - try multiple variations
        website = get_field('website') or get_field('weblink') or get_field('web_link')
        if website and website != 'Unknown':
            lines.append(f"- **Website**: {website}")
        
        # DOI field - try multiple variations
        doi = get_field('doi') or get_field('DOI')
        if doi and doi != 'Unknown':
            # Make DOI clickable if it's not already a URL
            if not doi.startswith('http'):
                if doi.startswith('doi:'):
                    doi_code = doi.replace('doi:', '').strip()
                else:
                    doi_code = doi
                doi_url = f"http://doi.org/{doi_code}"
            else:
                doi_url = doi
            lines.append(f"- **DOI**: {doi_url}")
    
    # Add source file information from dataset attributes
    if hasattr(report_data.dataset, 'attrs'):
        attrs = report_data.dataset.attrs
        if attrs.get('source_file'):
            lines.append(f"- **Source File**: {attrs['source_file']}")
        if attrs.get('data_product'):
            lines.append(f"- **Data Product**: {attrs['data_product']}")
            
    # Temporal Coverage
    if temporal.get("has_time") and temporal.get("valid_times"):
        lines.extend([
            f"- **Time Coverage**: {ReportUtils._safe_format_date(temporal['start_date'])} to {ReportUtils._safe_format_date(temporal['end_date'])}",
            f"- **Record Length**: {temporal['total_records']:,} observations ({temporal['time_span_years']:.1f} years)",
        ])
        
        if "estimated_frequency" in temporal:
            lines.append(f"- **Sampling Frequency**: {temporal['estimated_frequency']}")
    
    # Add citation if available
    if metadata.get('citation'):
        citation = metadata['citation']
        
        # Make DOI clickable if present
        import re
        doi_pattern = r'doi:\s*([0-9]+\.[0-9]+/[^\s]+)'
        doi_match = re.search(doi_pattern, citation)
        
        if doi_match:
            doi = doi_match.group(1)
            doi_url = f"http://doi.org/{doi}"
            citation = re.sub(doi_pattern, f'doi: {doi_url}', citation)
        
        lines.extend([
            "",
            "**Citation:**",
            "",
            f"    {citation}",
        ])
    
    lines.append("")
    
    # Dataset Statistics
    lines.extend([
        "Dataset Statistics", 
        "^^^^^^^^^^^^^^^^^^",
        "",
        f"- **Total Variables**: {stats['total_variables']}",
        f"- **Total Coordinates**: {stats['total_coordinates']}",
        f"- **Dataset Size**: {stats['file_size_mb']:.2f} MB",
        "",
    ])
    
    # Coordinate Information
    lines.extend([
        "Coordinate Information",
        "^^^^^^^^^^^^^^^^^^^^^^",
        "",
        "The following table shows information about the dataset coordinates:",
        "",
    ])
    
    if not coordinate_df.empty:
        coord_key_columns = ["Coordinate", "Standardized Name", "Description", "Units", "Size", "Min Value", "Max Value"]
        coord_display_df = coordinate_df[coord_key_columns].copy()
        lines.extend(ReportUtils.dataframe_to_rst_table(coord_display_df))
    else:
        lines.append("No coordinate information available.")
    
    lines.append("")
    
    # Variable Mapping Table
    lines.extend([
        "Variable Mapping and Statistics",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^",
        "",
        "The following table shows the mapping from original variable names to standardized names,",
        "along with key statistics for each variable.",
        "",
    ])
    
    # Generate RST table for variables
    if not mapping_df.empty:
        var_key_columns = ["Original Variable", "Standardized Name", "Description", "Units", "Size", "Min Value", "Max Value", "Missing %"]
        var_display_df = mapping_df[var_key_columns].copy()
        lines.extend(ReportUtils.dataframe_to_rst_table(var_display_df))
    else:
        lines.append("No variable mapping information available.")
    
    lines.append("")
    
    # Add plot if available
    plot_path = report_data.plot_path
    if plot_path:
        lines.extend([
            "Dataset Visualization",
            "^^^^^^^^^^^^^^^^^^^^^",
            "",
            f".. figure:: {plot_path}",
            "   :alt: AMOC time series plot",
            "   :align: center",
            "   :scale: 80%",
            "",
            f"   Time series plot for {dataset_name.upper()} dataset.",
            "",
        ])
    
    # Complete Metadata
    lines.extend([
        "Complete Metadata",
        "^^^^^^^^^^^^^^^^^",
        "",
        "The following metadata provides comprehensive information about this dataset:",
        "",
    ])
    
    # Display all metadata in structured format, but filter out verbose sections
    excluded_keys = ['citation', 'files', 'variables', 'coordinates']  # Skip verbose metadata
    for key, value in metadata.items():
        if key not in excluded_keys:
            formatted_key = key.replace('_', ' ').title()
            
            # Update time coverage with actual dataset values if available
            if key in ['time_coverage_start', 'time_coverage_end'] and temporal.get("has_time") and temporal.get("valid_times"):
                if key == 'time_coverage_start':
                    value = ReportUtils._safe_format_date(temporal['start_date'])
                elif key == 'time_coverage_end':
                    value = ReportUtils._safe_format_date(temporal['end_date'])
            
            if isinstance(value, (list, tuple)):
                lines.append(f"- **{formatted_key}**: {', '.join(map(str, value))}")
            elif isinstance(value, dict):
                # Skip large dictionary dumps
                if len(str(value)) > 200:
                    lines.append(f"- **{formatted_key}**: [Complex metadata structure - {len(value)} items]")
                else:
                    lines.append(f"- **{formatted_key}**: {str(value)}")
            else:
                # Make DOI clickable if it's a DOI field
                if key.lower() in ['doi', 'digital_object_identifier'] and str(value).strip():
                    doi_value = str(value).strip()
                    if doi_value.startswith('http'):
                        # Already a URL
                        lines.append(f"- **{formatted_key}**: {doi_value}")
                    else:
                        # Convert to clickable URL
                        if doi_value.startswith('doi:'):
                            doi_value = doi_value[4:].strip()
                        elif doi_value.startswith('10.'):
                            pass  # Already just the DOI part
                        lines.append(f"- **{formatted_key}**: https://doi.org/{doi_value}")
                else:
                    lines.append(f"- **{formatted_key}**: {value}")
    
    lines.append("")
    
    # Add metadata changes section for StandardizedDatasetReport
    if isinstance(report_data, StandardizedDatasetReport):
        lines.extend([
            "Metadata Processing Changes",
            "^^^^^^^^^^^^^^^^^^^^^^^^^^^",
            "",
            report_data.metadata_changes_summary,
        ])
    
    return "\n".join(lines)


def _dataframe_to_rst_table(df: pd.DataFrame) -> List[str]:
    """Convert pandas DataFrame to RST table format."""
    if df.empty:
        return ["(No data available)"]
    
    # Use all available columns - the calling function should provide the right subset
    display_df = df.copy()
    
    # Format numeric columns
    for col in ["Min Value", "Max Value"]:
        if col in display_df.columns:
            display_df[col] = display_df[col].apply(lambda x: f"{x:.2f}" if isinstance(x, (int, float)) and not pd.isna(x) else str(x))
    
    lines = []
    
    # Calculate column widths
    col_widths = {}
    for col in display_df.columns:
        col_widths[col] = max(
            len(str(col)),
            display_df[col].astype(str).str.len().max() if not display_df[col].empty else 0
        )
    
    # Create header separator
    header_sep = "+" + "+".join("-" * (col_widths[col] + 2) for col in display_df.columns) + "+"
    
    # Add table
    lines.append(header_sep)
    
    # Add header row
    header_row = "|" + "|".join(f" {col:<{col_widths[col]}} " for col in display_df.columns) + "|"
    lines.append(header_row)
    
    # Add header separator
    header_sep2 = "+" + "+".join("=" * (col_widths[col] + 2) for col in display_df.columns) + "+"
    lines.append(header_sep2)
    
    # Add data rows
    for _, row in display_df.iterrows():
        data_row = "|" + "|".join(f" {str(row[col]):<{col_widths[col]}} " for col in display_df.columns) + "|"
        lines.append(data_row)
        lines.append(header_sep)
    
    lines.append("")
    return lines


def _assess_metadata_completeness(report_data: BaseDatasetReport) -> int:
    """Assess metadata completeness and return a score out of 100."""
    score = 0
    metadata = report_data.metadata if hasattr(report_data, 'metadata') else {}
    
    # Required fields (20 points each)
    required_fields = ["project", "institution", "description", "time_coverage_start", "time_coverage_end"]
    for field in required_fields:
        if field in metadata and metadata[field]:
            score += 20
    
    return min(score, 100)


def rapid(all_files: bool = True, output_file: str = None) -> str:
    """Generate comprehensive RAPID dataset report.
    
    Parameters
    ----------
    all_files : bool, optional
        Whether to include all RAPID files in the report, by default True
    output_file : str, optional
        Path to write the RST report. If None, returns RST content as string.
        
    Returns
    -------
    str
        RST content of the report
        
    Examples
    --------
    >>> from amocatlas import report
    >>> rst_content = report.rapid()  # Generate report for all RAPID files
    >>> rst_content = report.rapid(all_files=False)  # Only transport file
    """
    return ReportUtils.generate_array_report('rapid', all_files=all_files, output_file=output_file)


def osnap(all_files: bool = True, output_file: str = None) -> str:
    """Generate comprehensive OSNAP dataset report."""
    return ReportUtils.generate_array_report('osnap', all_files=all_files, output_file=output_file)


def move(all_files: bool = True, output_file: str = None) -> str:
    """Generate comprehensive MOVE dataset report."""
    return ReportUtils.generate_array_report('move', all_files=all_files, output_file=output_file)


def samba(all_files: bool = True, output_file: str = None) -> str:
    """Generate comprehensive SAMBA dataset report."""
    return ReportUtils.generate_array_report('samba', all_files=all_files, output_file=output_file)


def all(arrays: List[str] = None, output_dir: str = "docs/source/reports") -> Dict[str, str]:
    """Generate reports for all available arrays.
    
    Parameters
    ----------
    arrays : list of str, optional
        List of array names to generate reports for. If None, generates reports for all available arrays.
    output_dir : str, optional
        Directory to write report files to, by default "docs/source/reports"
        
    Returns
    -------
    dict
        Dictionary mapping array names to their RST report content
        
    Examples
    --------
    >>> from amocatlas import report
    >>> reports = report.all()  # Generate reports for all arrays
    >>> reports = report.all(['rapid', 'osnap'])  # Only specific arrays
    """
    import pathlib
    
    if arrays is None:
        # List of all available arrays (matching the ReaderUtils datasource mapping)
        arrays = ['rapid', 'osnap', 'move', 'samba', 'mocha', 'fw2015', 'wh41n', 'dso']
    
    output_path = pathlib.Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    reports = {}
    print(f"Generating reports for {len(arrays)} arrays...")
    
    for array_name in arrays:
        try:
            print(f"\nGenerating {array_name.upper()} report...")
            
            # Generate report
            rst_content = ReportUtils.generate_array_report(array_name, all_files=True)
            reports[array_name] = rst_content
            
            # Write to file
            output_file = output_path / f"{array_name}_report.rst"
            output_file.write_text(rst_content)
            print(f"Written: {output_file}")
            
        except Exception as e:
            print(f"Failed to generate report for {array_name}: {e}")
            reports[array_name] = f"Error: {e}"
    
    print(f"\nGenerated {len([r for r in reports.values() if not r.startswith('Error:')])} reports successfully")
    return reports


# Example usage and testing
if __name__ == "__main__":
    # Test with RAPID dataset
    print("Generating RAPID dataset report...")
    report = generate_dataset_report("rapid", transport_only=True)
    print(report[:500] + "..." if len(report) > 500 else report)