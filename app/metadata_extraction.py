

import os

IMG_DIRPATH = os.path.join(os.path.dirname(__file__), "..", "img")

#def message():
#    return "Hello"

if __name__ == "__main__":

    subdirs = os.listdir(IMG_DIRPATH)
    subdirs.pop(subdirs.index(".gitignore"))
    subdirs.sort()
    for dirname in subdirs:
        dirpath = os.path.join(IMG_DIRPATH, dirname)
        img_filenames = os.listdir(dirpath)
        #print("--------------")
        print(dirname.upper(), f"({len(img_filenames)})")
        #print(img_filenames)
