#from pdb import set_trace as breakpoint
import os
import pytest

from app.vision_service import analyze_image_tags

LEAF_TAGS = ["leaf", "plant", "tree"] # if an image returns one of these tags, consider it to be a leaf

def leafiness_confidence(image_filepath):
    tags = analyze_image_tags(image_filepath)
    confidences = [tag["confidence"] for tag in tags if tag["name"] in LEAF_TAGS]
    if confidences:
        return max(confidences)
    else:
        return 0

#LEAFINESS_THRESHOLD = .6 # if an image is at least this likely to be a leaf, classify it as a leaf
#
#def leafiness_classification(image_filepath):
#    if leafiness_confidence(image_filepath) > LEAFINESS_THRESHOLD:
#        return True
#    else:
#        return False

if __name__ == "__main__":
    images = parse_images()
    print(len(images), "IMAGES...")
