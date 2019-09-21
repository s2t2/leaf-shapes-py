# Contributor's Guide

## Setup

Clone the repo:

```sh
git clone ___________/leaf-shapes-py
cd leaf-shapes-py
```

Obtain a zip file of images from the Peabody team, unzip it and copy the containing 11 folders into the "img" directory in this repository. FYI - each directory is named after a specific tree family (e.g "Acer rubrum L") and contains images of preserved leaves from that family.


Setup a virtual environment:

```sh
conda create -n leaf-env-36 python=3.6
conda activate leaf-env-36
```

## Installation

From within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Write a report of metadata about the images:

```sh
python -m app.metadata_extraction
```

## Testing

Install the testing framework, "pytest" (first-time only):

```sh
pip install pytest # first-time only
```

Run tests:

```sh
pytest
```
