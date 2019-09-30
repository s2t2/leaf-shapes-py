

import os
#from pdb import set_trace as breakpoint
import pandas
from requests.exceptions import HTTPError
from app.image_classifier import leafiness_confidence

IMG_IMPORTS_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "img", "imports")

def family_dirnames():
    """Assumes all directories in the image import dir are named after a Tree family (e.g. "Acer rubrum L")"""
    dirnames = os.listdir(IMG_IMPORTS_DIRPATH)
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

def image_records():
    return [
        {
            "family": img.family_name,
            #"filename": img.filename,
            "uuid": img.uuid,
            #"ext": img.ext
            #"leafiness": img.leafiness
        } for img in parse_images()
    ]

def image_records_with_classifications():
    records = []
    for img in parse_images()[1:9]:
        try:
            leafiness = leafiness_confidence(img.filepath)
            print(img, leafiness)
        except HTTPError as err:
            #> requests.exceptions.HTTPError: 400 Client Error: Bad Request for url
            print(img, err)
            leafiness = None

        records.append({
            "family": img.family_name,
            #"filename": img.filename,
            "uuid": img.uuid,
            #"ext": img.ext
            "leafiness": leafiness
        })
    return records



class Fam():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Family '{self.name}'>"

    @property
    def dirpath(self):
        return os.path.join(IMG_IMPORTS_DIRPATH, self.name)

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
        #self.leafiness = None

    def __repr__(self):
        return f"<Image '{self.family_name}' / '{self.name}'>"

    @property
    def ext(self):
        return self.filename.split(".")[-1] #> "jpg"

    @property
    def uuid(self):
        return self.filename.replace(f".{self.ext}", "")

    @property
    def filepath(self):
        return os.path.join(IMG_IMPORTS_DIRPATH, self.family_name, self.filename)

    #@property
    #def leafiness(self):
    #    return leafiness_confidence(self.filepath) # TODO: how to cache this to prevent subsequent requests


if __name__ == "__main__":

    families = parse_families()
    print("--------------------")
    print(f"TREE FAMILIES: ({len(families)})")
    for fam in families:
        print(" + ", fam.name.upper(), f"({len(fam.img_filenames)})")

    images = parse_images()
    print("--------------------")
    print(f"LEAF IMAGES ({len(images)})")

    # WRITE TO CSV

    CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "images.csv")
    df = pandas.DataFrame(image_records_with_classifications())
    df.index.rename("id", inplace=True) # assigns a column label "id" for the index column
    df.index += 1 # starts ids at 1 instead of 0
    df.to_csv(CSV_FILEPATH)
    print("--------------------")
    print("WRITING TO CSV...", os.path.abspath(CSV_FILEPATH))
    print(df.head())
