

import os
from pdb import set_trace as bpoint # we're stuck in 3.6 at the moment, otherwise we could use breakpoint()

# import numpy as np
# import pandas

FAMILIES_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "img", "families")

def family_dirnames():
    dirnames = os.listdir(FAMILIES_DIRPATH)
    dirnames = [name for name in dirnames if name not in [".gitignore", ".DS_Store"]] # removes extraneous hidden files
    dirnames.sort()
    return dirnames

def parse_families():
    return [Fam(family_name) for family_name in family_dirnames()]

def parse_images():
    images = []
    for fam in parse_families():
        for img in fam.images:
            images.append(img)
    return images

class Fam():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Family '{self.name}'>"

    @property
    def dirpath(self):
        return os.path.join(FAMILIES_DIRPATH, self.name)

    @property
    def img_filenames(self):
        return os.listdir(self.dirpath)

    @property
    def images(self):
        return [Img(self.name, img_filename) for img_filename in self.img_filenames]

class Img():
    def __init__(self, family_name, filename):
        self.family_name = family_name
        self.filename = filename
        self.name = filename

    def __repr__(self):
        return f"<Image '{self.family_name}' / '{self.name}'>"

    @property
    def uuid(self):
        return self.filename.replace(".jpg","")

    @property
    def filepath(self):
        return os.path.join(IMG_FAMILIES_DIRPATH, self.family_name, self.filename)

    #def is_leaf(parameter_list):
    #    return False
    #
    #def likelihood_of_leaf(parameter_list):
    #    return 0.84

if __name__ == "__main__":

    families = parse_families()
    print(f"TREE FAMILIES: ({len(families)})")
    for fam in families:
        print(" + ", fam.name.upper(), f"({len(fam.img_filenames)})")

    images = parse_images()
    print(f"LEAF IMAGES ({len(images)}):")
    for img in images:
        # print(img.family.upper(), ">", img.filename)
        print(" + ", img.family_name.upper(), img.uuid)

    #breakpoint()
    #bpoint()
    # img.filepath()
