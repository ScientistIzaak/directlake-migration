# Imports
import fabric_cat_tools as fct
from fabric_cat_tools.TOM import connect_semantic_model

#----------------------------------------#
# -------- Add Field Parameters -------- #
#----------------------------------------#
def add_field_parameter_template(param_table_name, param_objects, dataset_name, workspace_name):
    """
    Function to add field parameters to a semantic model in Microsoft Fabric.
    
    Parameters:
    param_table_name (str): Name of the parameter table.
    param_objects (list): List of objects (fields) to add as parameters.
    dataset_name (str): Name of the dataset.
    workspace_name (str): Name of the workspace.
    """
    
    # Add Field Parameters
    with connect_semantic_model(dataset=dataset_name, workspace=workspace_name, readonly=False) as tom:
        tom.add_field_parameter(
            table_name=param_table_name,
            objects=param_objects
        )
    print(f"Field parameters added to {param_table_name} in dataset {dataset_name} and workspace {workspace_name}.")

# Example usage with placeholder variables
param_table_name = 'YOUR_PARAMETER_TABLE'
param_objects = ["'YOUR_TABLE'[YOUR_COLUMN1]", "'YOUR_TABLE'[YOUR_COLUMN2]"]
dataset_name = 'YOUR_DATASET'
workspace_name = 'YOUR_WORKSPACE'

add_field_parameter_template(param_table_name, param_objects, dataset_name, workspace_name)


#---------------------------------------#
# ------------ Move Measures ---------- #
#---------------------------------------#
def move_measures(source_semantic, source_table, source_workspace, destination_semantic, destination_table, destination_workspace):
    """
    Function to move all measures from one semantic model and table to another in Microsoft Fabric.
    
    Parameters:
    source_semantic (str): Name of the source dataset/semantic model.
    source_table (str): Name of the source table containing the measures.
    source_workspace (str): Name of the workspace containing the source dataset.
    destination_semantic (str): Name of the destination dataset/semantic model.
    destination_table (str): Name of the destination table where the measures will be copied.
    destination_workspace (str): Name of the workspace containing the destination dataset.
    """
    
    # Connect to the source semantic model and fetch all measures from the source table
    with connect_semantic_model(dataset=source_semantic, workspace=source_workspace, readonly=False) as source_tom:
        # Loop through all measures in the source dataset
        for measure in source_tom.all_measures():
            print(f"Moving measure: {measure.Name}")

            # Connect to the destination semantic model and add the measure
            with connect_semantic_model(dataset=destination_semantic, workspace=destination_workspace, readonly=False) as destination_tom:
                destination_tom.add_measure(
                    measure_name=measure.Name,  # Extract the measure's name
                    expression=measure.Expression,  # The DAX expression behind the measure
                    table_name=destination_table,  # Target table in destination dataset
                )
    print(f"All measures moved from {source_table} to {destination_table}.")

# Example usage with placeholder variables
source_semantic = 'YOUR_SOURCE_SEMANTIC'
source_table = 'YOUR_SOURCE_TABLE'
source_workspace = 'YOUR_SOURCE_WORKSPACE'

destination_semantic = 'YOUR_DESTINATION_SEMANTIC'
destination_table = 'YOUR_DESTINATION_TABLE'
destination_workspace = 'YOUR_DESTINATION_WORKSPACE'

move_measures(source_semantic, source_table, source_workspace, destination_semantic, destination_table, destination_workspace)

#---------------------------------------#
# ------ Rebind & Refresh Report ------ #
#---------------------------------------#
def rebind_report_and_refresh_model(report_name, report_workspace, dataset_name, dataset_workspace):
    """
    Function to rebind a report to a new dataset and refresh the semantic model in Microsoft Fabric.
    
    Parameters:
    report_name (str): Name of the report to be rebound.
    report_workspace (str): Name of the workspace containing the report.
    dataset_name (str): Name of the dataset to rebind the report to.
    dataset_workspace (str): Name of the workspace containing the dataset.
    """
    
    # Rebind the semantic model to the report
    fct.report_rebind(report_name, dataset_name, dataset_workspace=dataset_workspace, report_workspace=report_workspace)
    print(f"Report '{report_name}' successfully rebound to dataset '{dataset_name}'.")

    # Refresh the semantic model after rebinding
    fct.refresh_semantic_model(dataset=dataset_name, workspace=dataset_workspace)
    print(f"Semantic model for dataset '{dataset_name}' in workspace '{dataset_workspace}' has been refreshed.")

# Example usage with placeholder variables
report_name = 'YOUR_REPORT_NAME'
report_workspace = 'YOUR_REPORT_WORKSPACE'

dataset_name = 'YOUR_DATASET_NAME'
dataset_workspace = 'YOUR_DATASET_WORKSPACE'

rebind_report_and_refresh_model(report_name, report_workspace, dataset_name, dataset_workspace)
