# Leaf Shapes (Python)

Programatically identifying and classifying leaf images and shapes.

:seedling: :leaves: :herb: :maple_leaf:

## Repo Setup

Clone the repo and navigate there from the command-line:

```sh
git clone git@github.com:s2t2/leaf-shapes-py.git
cd leaf-shapes-py
```

## Image Acquisition

Obtain a zip file of images from the [research team](http://peabody.yale.edu/).

Unzip it and observe there are a number of subdirectories, each named after a specific tree family (e.g "Acer rubrum L"). Inside the each subdirectory are a number of images of preserved leaves. Not all the images are of leaves though - some look like laboratory slides.

Before proceeding, copy or move all of these subdirectories into the "img/imports" directory in this repository.

## Computer Vision Service Account

Login to your [Azure account](https://azure.microsoft.com) or create a new one. Then [create a new "CognitiveServicesComputerVision" resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesComputerVision).

After the resource has been configured and deployed, you should have access to the resource's API key and endpoint URL. Create a new file called ".env" in the root directory of this repository, and place inside the values for the `VISION_API_KEY` and `VISION_API_ENDPOINT`, respectively. See the ".env.example" file for an example.

## Environment Setup

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

### Leaf Image Detection

Separate leaf images from non-leaf images:

```sh
python -m app.image_classifier
```

This will separate all images in all subdirectories of "img/imports" into two categories (leaf, or non-leaf), and copy the images under corresponding subdirectories of either "img/exports/leaf" or "img/exports/nonleaf", as appropriate.


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
