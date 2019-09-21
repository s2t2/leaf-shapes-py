

import os
from pdb import set_trace as bpoint # we're stuck in 3.6 at the moment, otherwise we could use breakpoint()
# import pandas

IMG_FAMILIES_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "img", "families")

def parse_images():
    subdirs = os.listdir(IMG_FAMILIES_DIRPATH)
    #subdirs.pop(subdirs.index(".gitignore"))
    #subdirs.pop(subdirs.index(".DS_Store"))
    #subdirs.pop(subdirs.index("leaf-shapes.jpg"))
    subdirs = [s for s in subdirs if s not in [".gitignore", ".DS_Store"]]
    subdirs.sort()
    images = []
    for family_name in subdirs:
        family_dirpath = os.path.join(IMG_FAMILIES_DIRPATH, family_name)
        img_filenames = os.listdir(family_dirpath)
        #print("--------------")
        print(family_name.upper(), f"({len(img_filenames)})")
        for img_filename in img_filenames:
            #img = {"family": family_name, "filename": img_filename}
            img = Img(family_name, img_filename)
            print(os.path.isfile(img.filepath()))
            images.append(img)
    return images

# class Family(): TODO
    # def __init__(self, name):
    #     self.name = name

class Img():
    def __init__(self, family_name, filename):
        self.family = family_name
        self.family_name = family_name
        self.filename = filename

    def uuid(self):
        return self.filename.replace(".jpg","")

    def family_dirpath(self):
        return os.path.join(IMG_FAMILIES_DIRPATH, self.family_name)

    def filepath(self):
        return os.path.join(self.family_dirpath(), self.filename)

    #def is_leaf(parameter_list):
    #    return False
    #
    #def likelihood_of_leaf(parameter_list):
    #    return 0.84

if __name__ == "__main__":

    images = parse_images()

    families = list(set([img.family_name for img in images])) # todo: Family(img.family_name)

    # images, families = parse_images()

    print(len(images), "IMAGES:")
    for img in images:
        # print(img.family.upper(), ">", img.filename)
        print(img.uuid())

    #breakpoint()
    #bpoint()
    # img.filepath()
