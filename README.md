# Zarr Demo

This project demonstrates how to use the Zarr library for chunked, compressed, N-dimensional arrays in Python.

## Features
- Create a Zarr array
- Write data to a Zarr array
- Read data from a Zarr array

## Requirements
- Python >3.7 (zarr v2) or >=3.11 (zarr v3)
- zarr
- numpy

## Setup

Clone the repository in your local machine.

Create a virtual environment using the provided `.yml` files (Conda):

   ```
   conda env create -f env_config_Zarr_v2.yml or env_config_Zarr_v3.yml 
   ```

## Usage
In VSCode, open the notebook `zarr_demo.ipynb` and run the cells to see how to create, write, and read Zarr arrays.

If you prefer to use jupyter notebook, from your terminal run:

   ```
   conda activate zarr_demo_v2 or zarr_demo_v3

   python -m ipykernel install --user --name zarr_demo_v3 --display-name "zarr_demo_v3"

   jupyter lab
   ```
Open the `zarr_demo.ipynb` notebook from JupyterLab.


