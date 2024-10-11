# Microsoft Fabric Report Migration to DirectLake

This repository provides a Python-based solution for migrating Microsoft Fabric reports from Import/Direct Query to DirectLake. The script automates the transition of measures, field parameters, and report rebinding using the `fabric_cat_tools` library.

## Features
- Move Field Parameter Tables to DirectLake.
- Move Measures from source to destination semantic models.
- Rebind Reports to new DirectLake semantic models.
- Refresh semantic models after migration.

## Requirements
- Python 3.x
- `fabric_cat_tools` (Thanks to [m-kovalsky's repository](https://github.com/m-kovalsky/fabric_cat_tools))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/directlake-migration.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd directlake-migration
   ```
3. Install `fabric_cat_tools`:
   ```bash
   %pip install "https://raw.githubusercontent.com/m-kovalsky/fabric_cat_tools/main/fabric_cat_tools-0.4.1-py3-none-any.whl"
   ```
## Usage
### 1. Move Field Parameter Tables
This section automates the migration of field parameter tables to DirectLake.

- Edit the Script: Open the migrate_reports.py file and locate the section responsible for moving field parameters.
- Update Parameters: Specify the table name, objects, dataset, and workspace for each field parameter table you wish to migrate. Note that each field parameter table must be updated individually in the script.

Example:
   ```bash
   #Move Field Parameter Table
   param_table_name = 'YOUR_FIELD_PARAMETER_TABLE'
   param_objects = ["'YOUR_TABLE'[YOUR_FIELD1]", "'YOUR_TABLE'[YOUR_FIELD2]"]
   dataset_name = 'YOUR_DATASET'
   workspace_name = 'YOUR_WORKSPACE'
   ```
add_field_parameter_template(param_table_name, param_objects, dataset_name, workspace_name)

### 2. Move Measures
This section copies measures from a source table to a destination table.

- Edit the Script: Locate the section for moving measures in migrate_reports.py.
- Update the Source and Destination: Define the source semantic model, source table, destination dataset, and destination table. This will transfer all measures from the specified source to the target.

Example:
   ``` bash
   # Move Measures
   source_semantic = 'YOUR_SOURCE_SEMANTIC'
   source_table = 'YOUR_SOURCE_TABLE'
   destination_semantic = 'YOUR_DESTINATION_SEMANTIC'
   destination_table = 'YOUR_DESTINATION_TABLE'
   ```
move_measures(source_semantic, source_table, destination_semantic, destination_table)
  
### 3. Rebind Reports
This section rebinds reports to new DirectLake semantic models.

- Edit the Script: Find the rebinding section in migrate_reports.py.
- Specify Report and Workspaces: Update the report name and workspaces to rebind the report to the appropriate dataset.

Example:
   ```bash
   # Rebind Report
   report_name = 'YOUR_REPORT_NAME'
   report_workspace = 'YOUR_REPORT_WORKSPACE'
   dataset_name = 'YOUR_DATASET_NAME'
   dataset_workspace = 'YOUR_DATASET_WORKSPACE'
   ```
rebind_report_and_refresh_model(report_name, report_workspace, dataset_name, dataset_workspace)

### 4. Refresh Semantic Model
This section refreshes the semantic model after all migrations.

- Automatic Refresh: The script will automatically refresh the semantic model after rebinding reports. No additional configuration is needed.


## Credits
Special thanks to m-kovalsky for the fabric_cat_tools library, which made this tool possible.

## License
This project is licensed under the MIT License.

