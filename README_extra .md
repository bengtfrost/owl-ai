This file explains the general workflow for modifying the `camel-ai` package, installing it in editable mode, and ensuring that the `owl` project uses the modified `camel-ai` package.

````markdown
# Workflow for Modifying and Using `camel-ai` in `owl`

This document outlines the steps to modify the `camel-ai` package, install it in editable mode, and ensure that the `owl` project uses the modified version of `camel-ai`. This workflow assumes that both `camel-ai` and `owl` are separate repositories with their own virtual environments.

---

## Step 1: Fork or Clone `camel-ai`
1. If you haven't already, fork or clone the `camel-ai` repository to make modifications:
   ```bash
   git clone <camel-ai-repository-url> /path/to/camel-ai
   ```
2. Navigate to the cloned repository:
   ```bash
   cd /path/to/camel-ai
   ```

---

## Step 2: Modify the `camel-ai` Source Code
1. Make changes to the `camel-ai` source code. For example, to modify `_utils.py`:
   ```bash
   nano /path/to/camel-ai/camel/agents/_utils.py
   ```
2. Save your changes.

---

## Step 3: Install `camel-ai` in Editable Mode
1. Activate the `camel-ai` virtual environment:
   ```bash
   source /path/to/camel-ai/.venv/bin/activate
   ```
2. Install `camel-ai` in editable mode using `uv`:
   ```bash
   uv pip install -e .
   ```
3. Verify the installation:
   ```bash
   uv pip list | grep camel
   ```
   Ensure that `camel` is listed as installed in editable mode (e.g., `camel @ file:///path/to/camel-ai`).
4. Deactivate the `camel-ai` virtual environment:
   ```bash
   deactivate
   ```

---

## Step 4: Use the Modified `camel-ai` in `owl`
1. Activate the `owl` virtual environment:
   ```bash
   source /path/to/owl-ai/.venv/bin/activate
   ```
2. Uninstall the existing `camel` package from the `owl` virtual environment:
   ```bash
   uv pip uninstall camel
   ```
3. Install the modified `camel-ai` package into the `owl` virtual environment in editable mode:
   ```bash
   cd /path/to/camel-ai
   uv pip install -e .
   ```
4. Verify the installation:
   ```bash
   uv pip list | grep camel
   ```
   Ensure that `camel` is listed as installed in editable mode (e.g., `camel @ file:///path/to/camel-ai`).
5. Deactivate the `owl` virtual environment:
   ```bash
   deactivate
   ```

---

## Step 5: Verify Changes in Both Repositories
1. To confirm that the `owl` project is using the modified `camel-ai` package, check the `_camel_ai.pth` file in the `owl` virtual environment:
   ```bash
   cat /path/to/owl-ai/.venv/lib/python3.10/site-packages/_camel_ai.pth
   ```
   The file should contain the path to your `camel-ai` source directory:
   ```
   /path/to/camel-ai
   ```
2. Check if the changes in `camel-ai` are reflected in the `owl` virtual environment:
   ```bash
   cat /path/to/owl-ai/.venv/lib/python3.10/site-packages/camel/agents/_utils.py
   ```
   Ensure the changes you made in `/path/to/camel-ai/camel/agents/_utils.py` are reflected here.

---

## Step 6: Test the Changes
1. Run your `owl` project to ensure that the modified `camel-ai` package is being used:
   ```bash
   cd /path/to/owl-ai
   uv run <your-test-script>.py
   ```
2. Verify that the changes in `camel-ai` are functioning as expected.

---

## Advantages of This Workflow
- **Editable Mode (`-e`)**: Both `camel-ai` and `owl` use the same source code for `camel-ai`, so any changes in `camel-ai` are immediately reflected in both projects.
- **No Reinstallation Overhead**: You don’t need to rebuild or reinstall the `camel-ai` package after every change.
- **Consistency**: Both repositories (`camel-ai` and `owl`) use the same version of `camel-ai`.

---

## Notes on the `_camel_ai.pth` File
The `_camel_ai.pth` file in the `owl` virtual environment ensures that the `owl` project uses the `camel-ai` source code directly. If the file is missing or incorrect, reinstall `camel-ai` in editable mode in the `owl` virtual environment.

---

## Summary
1. Modify the `camel-ai` source code in `/path/to/camel-ai`.
2. Install `camel-ai` in editable mode in both the `camel-ai` and `owl` virtual environments.
3. Verify and test the changes to ensure that the `owl` project uses the modified `camel-ai` package.

This workflow ensures a smooth development process while leveraging `uv` commands and editable installations.
````

This `README_extra.md` file provides a general and reusable explanation of the workflow for modifying and using `camel-ai` in `owl`. It includes steps for forking/cloning, making changes, installing in editable mode, and verifying the changes.
