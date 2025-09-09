{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a71138f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports\n",
    "import numpy as np\n",
    "import zarr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "47303d43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data written to Zarr store 'example.zarr'.\n",
      "Data written to Zarr store 'sparse_example.zarr'.\n"
     ]
    }
   ],
   "source": [
    "# Create data to store in the Zarr store\n",
    "data = np.random.rand(100, 100).astype('float32')\n",
    "\n",
    "sparse_data = np.zeros((1000, 1000), dtype='float32')\n",
    "sparse_data[sparse_data < 0.8] = 0  # Make it sparse\n",
    "\n",
    "# Create a Zarr store and write data to it\n",
    "zarr_store = zarr.open('example.zarr', mode='w', shape=data.shape, dtype=data.dtype, compressor=zarr.Blosc(cname='zstd', clevel=3, shuffle=2))\n",
    "zarr_store[:] = data    \n",
    "\n",
    "sparse_store = zarr.open('sparse_example.zarr', mode='w', shape=sparse_data.shape, dtype=sparse_data.dtype, compressor=zarr.Blosc(cname='zstd', clevel=3, shuffle=2))\n",
    "sparse_store[:] = sparse_data\n",
    "\n",
    "print(\"Data written to Zarr store 'example.zarr'.\")\n",
    "print(\"Data written to Zarr store 'sparse_example.zarr'.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d05bd89e",
   "metadata": {},
   "source": [
    "### Explanation of Zarr Store Creation\n",
    "\n",
    "```python\n",
    "zarr.open(\n",
    "    'example.zarr',\n",
    "    mode='w',\n",
    "    shape=data.shape,\n",
    "    dtype=data.dtype,\n",
    "    compressor=zarr.Blosc(cname='zstd', clevel=3, shuffle=2),\n",
    "    chunks=(50, 50)  # Optional: specify chunk size\n",
    ")\n",
    "```\n",
    "\n",
    "- **'example.zarr'**: Path to the Zarr store on disk.\n",
    "- **mode='w'**: Write mode; creates a new store or overwrites an existing one.\n",
    "- **shape=data.shape**: Shape of the array to store (e.g., (100, 100)).\n",
    "- **dtype=data.dtype**: Data type of the array (e.g., float32).\n",
    "- **compressor=zarr.Blosc(...)**: Use Blosc compressor with Zstandard codec, compression level 3, and byte shuffling.\n",
    "- **chunks=(50, 50)**: (Optional) Store data in 50x50 blocks for efficient access and better compression.\n",
    "\n",
    "**Using chunks is recommended** for large arrays, as it improves read/write performance and compression."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "137790f1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data loaded from Zarr store 'example.zarr':\n",
      "[[0.05025649 0.15987594 0.976944   ... 0.57433313 0.93962246 0.916729  ]\n",
      " [0.31012645 0.04879308 0.14425835 ... 0.9346751  0.4659635  0.7248583 ]\n",
      " [0.14628652 0.7530553  0.5462516  ... 0.799341   0.04548542 0.47115627]\n",
      " ...\n",
      " [0.44548213 0.22238499 0.38521996 ... 0.0972312  0.83554995 0.8931943 ]\n",
      " [0.12062085 0.0247786  0.32600683 ... 0.09308951 0.58562607 0.2910144 ]\n",
      " [0.86853516 0.16844063 0.239198   ... 0.36172217 0.56837755 0.57919437]]\n"
     ]
    }
   ],
   "source": [
    "# Load data from the Zarr store\n",
    "loaded_data = zarr.open('example.zarr', mode='r')\n",
    "print(\"Data loaded from Zarr store 'example.zarr':\")\n",
    "print(loaded_data[:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8cb8844c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original data size: 40000 bytes\n",
      "Zarr stored data size: 33146 bytes\n",
      "Sparse original data size: 4000000 bytes\n",
      "Sparse Zarr stored data size: 1432 bytes\n"
     ]
    }
   ],
   "source": [
    "# Compare size of compressed vs uncompressed data\n",
    "original_size = data.nbytes\n",
    "zarr_size = zarr_store.nbytes_stored\n",
    "sparse_original_size = sparse_data.nbytes\n",
    "sparse_zarr_size = sparse_store.nbytes_stored\n",
    "print(f\"Original data size: {original_size} bytes\")\n",
    "print(f\"Zarr stored data size: {zarr_size} bytes\")\n",
    "print(f\"Sparse original data size: {sparse_original_size} bytes\")\n",
    "print(f\"Sparse Zarr stored data size: {sparse_zarr_size} bytes\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9b58ed24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data written to Zarr store 'grouped_example.zarr' with groups and datasets.\n"
     ]
    }
   ],
   "source": [
    "# Create a group structure in Zarr\n",
    "root = zarr.open('grouped_example.zarr', mode='w')\n",
    "group1 = root.create_group('group1')\n",
    "\n",
    "# We omit compression here for simplicity\n",
    "group1.create_dataset('data1', data=np.random.rand(50, 50).astype('float32'))\n",
    "group1.create_dataset('data2', data=np.random.rand(30, 30).astype('float32'))\n",
    "group2 = root.create_group('group2')\n",
    "group2.create_dataset('data3', data=np.random.rand(20, 20).astype('float32'))\n",
    "\n",
    "print(\"Data written to Zarr store 'grouped_example.zarr' with groups and datasets.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "72638b83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Metadata added to 'grouped_example.zarr':\n",
      "{'description': 'This is a grouped Zarr store example', 'version': '1.0'}\n"
     ]
    }
   ],
   "source": [
    "# Add metadata to the grouped Zarr store zarr specifications v2\n",
    "root.attrs['description'] = 'This is a grouped Zarr store example'\n",
    "root.attrs['version'] = '1.0'\n",
    "print(\"Metadata added to 'grouped_example.zarr':\")\n",
    "print(root.attrs.asdict())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bd766b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add metadata to the Zarr store zarr specifications v3\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "ABCM4S",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
