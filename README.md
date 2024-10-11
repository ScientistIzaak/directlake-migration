# Microsoft Fabric Report Migration to DirectLake

This repository provides a Python-based solution for migrating Microsoft Fabric reports from Import/Direct Query to DirectLake. The script automates the transition of measures, field parameters, and report rebinding using the `fabric_cat_tools` library.

## Features
- Move Field Parameter Tables
- Move Measures
- Rebind Reports to new DirectLake semantic models
- Refresh semantic models

## Requirements
- Python 3.x
- `fabric_cat_tools` (Thanks to [m-kovalsky's repository](https://github.com/m-kovalsky/fabric_cat_tools))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/directlake-migration.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Install `fabric_cat_tools`:
   ```bash
   %pip install "https://raw.githubusercontent.com/m-kovalsky/fabric_cat_tools/main/fabric_cat_tools-0.4.1-py3-none-any.whl"
   ```
## Usage

1. Edit the migrate_reports.py file to set your source and destination semantic models, tables, and workspaces.
  
2. Run the script:
    ```bash
    python migrate_reports.py
    ```

This will migrate field parameters, measures, and rebind the reports for DirectLake.

## Credits
Special thanks to m-kovalsky for the fabric_cat_tools library, which made this tool possible.

## License
This project is licensed under the MIT License.

### `requirements.txt`

```text
fabric_cat_tools==0.4.1
```
