# Zarr Demo

This project demonstrates how to use the Zarr library for chunked, compressed, N-dimensional arrays in Python.

# Zarr basics

Zarr is a library for chunked, compressed, N-dimensional arrays in Python. It provides a simple and efficient way to store and manipulate large datasets.
It supports various storage backends, including local file systems and cloud storage.

![Zarr Terminology](https://zarr-specs.readthedocs.io/en/latest/_images/terminology-hierarchy.excalidraw.png)

## Features
- Create arrays and groups in a Zarr store
- Store/read JSON metadata via attributes
- Configure chunking and compression (codec pipeline)
- Work with ZIP stores
- Managing a Zarr store with a dedicated manager class
- Exercise: Use Zarr in a PyTorch DataLoader (https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)

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
   ```
   ``` 
   python -m ipykernel install --user --name zarr_demo_v3 --display-name "zarr_demo_v3"
   ```
   ```
   jupyter lab
   ```
Open the `zarr_demo.ipynb` notebook from JupyterLab.


