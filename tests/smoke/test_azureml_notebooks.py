# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# This test is based on the test suite implemented for Recommenders project
# https://github.com/Microsoft/Recommenders/tree/master/tests

import os
import glob
import papermill as pm
import pytest
import shutil

# Unless manually modified, python3 should be
# the name of the current jupyter kernel
# that runs on the activated conda environment
KERNEL_NAME = "cv"
OUTPUT_NOTEBOOK = "output.ipynb"

@pytest.mark.amlnotebooks
def test_20_notebook_run(
    classification_notebooks,
    subscription_id,
    resource_group,
    workspace_name,
    workspace_region
    ):
    notebook_path = classification_notebooks["20_azure_workspace_setup"]
    pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        parameters=dict(
            PM_VERSION=pm.__version__,
            subscription_id=subscription_id,
            resource_group=resource_group,
            workspace_name=workspace_name,
            workspace_region=workspace_region
        ),
        kernel_name=KERNEL_NAME,
    )


@pytest.mark.azureml_test
def test_21_notebook_run(
    classification_notebooks,
    subscription_id,
    resource_group,
    workspace_name,
    workspace_region):
    notebook_path = classification_notebooks["21_deployment_on_azure_container_instances"]
    pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        parameters=dict(
            PM_VERSION=pm.__version__,
            subscription_id=subscription_id,
            resource_group=resource_group,
            workspace_name=workspace_name,
            workspace_region=workspace_region),
        kernel_name=KERNEL_NAME,
    )

def test_22_notebook_run(
    classification_notebooks,
    subscription_id,
    resource_group,
    workspace_name,
    workspace_region):
    notebook_path = classification_notebooks["22_deployment_on_azure_kubernetes_service"]
    pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        parameters=dict(
            PM_VERSION=pm.__version__,
            subscription_id=subscription_id,
            resource_group=resource_group,
            workspace_name=workspace_name,
            workspace_region=workspace_region),
        kernel_name=KERNEL_NAME,
    )

def test_23_notebook_run(
    classification_notebooks,
    subscription_id,
    resource_group,
    workspace_name,
    workspace_region):
    notebook_path = classification_notebooks["23_aci_aks_web_service_testing"]
    pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        parameters=dict(
            PM_VERSION=pm.__version__,
            subscription_id=subscription_id,
            resource_group=resource_group,
            workspace_name=workspace_name,
            workspace_region=workspace_region),
        kernel_name=KERNEL_NAME,
    )
