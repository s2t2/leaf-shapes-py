

import os

IMG_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "img", "training")

def parse_images():
    subdirs = os.listdir(IMG_DIRPATH)
    subdirs.pop(subdirs.index(".gitignore"))
    #subdirs.pop(subdirs.index(".DS_Store"))
    #subdirs.pop(subdirs.index("leaf-shapes.jpg"))
    #subdirs = [s for s in subdirs if s not in [".gitignore", ".DS_Store"]]
    subdirs.sort()
    images = []
    for dirname in subdirs:
        dirpath = os.path.join(IMG_DIRPATH, dirname)
        img_filenames = os.listdir(dirpath)
        #print("--------------")
        #print(dirname.upper(), f"({len(img_filenames)})")
        for img_filename in img_filenames:
            images.append({"filename": img_filename, "family": dirname})
    return images

if __name__ == "__main__":

    images = parse_images()
    print(len(images), "IMAGES:")

    for img in images:
        print(img["family"].upper(), ">", img["filename"])
