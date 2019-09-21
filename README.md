# Leaf Shapes (Python)

Programatically identifying and classifying leaf shapes. :seedling: :leaves: :herb: :maple_leaf:

### Installation and Setup

Clone the repo and navigate there from the command-line:

```sh
git clone git@github.com:s2t2/leaf-shapes-py.git
cd leaf-shapes-py
```

> NOTE: subsequent commands assume you're running them from the repo's root directory.

Acquire the leaf images! Obtain a zip file of images from the [research team](http://peabody.yale.edu/). Unzip it and observe there are 11 subdirectories, each named after a specific tree family (e.g "Acer rubrum L"). Inside the each subdirectory are a number of images of preserved leaves. Not all the images are of leaves though - some look like laboratory slides. Finally, copy all the leaf family image subdirectories into the "img/families" directory in this repository.

Setup a virtual environment:

```sh
conda create -n leaf-env-36 python=3.6
conda activate leaf-env-36
```

> NOTE: subsequent commands assume you're running them from within the virtual environment.

Install package dependencies:

```sh
pip install -r requirements.txt
```

Install the testing framework, "pytest", and any other development dependencies:

```sh
pip install -r dev-requirements.txt
```

## Usage

Write image metadata to "data/images.csv":

```sh
python -m app.image_parser
```

## Testing

Run tests:

```sh
pytest
```

## Debugging

While we're stuck in 3.6, use the following snippet in place of 3.7's `breakpoint()`:

```py
from pdb import set_trace as breakpoint
breakpoint()
```
