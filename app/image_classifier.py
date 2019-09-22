
from pdb import set_trace as breakpoint # shim for Python 3.6

from app.images_parser import parse_images

def image_tags(image_filepath):
    # TODO:
    # request to https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/
    # parse the response's "tags" and return them...
    tags = [
        {"name": "text", "confidence": 0.9871882},
        {"name": "book", "confidence": 0.9109231},
        {"name": "leaf", "confidence": 0.883738041},
        {"name": "plant", "confidence": 0.7578559}
    ]
    return tags

LEAF_TAGS = ["leaf", "plant", "tree"] # if an image returns one of these tags, consider it to be a leaf

def leafiness_confidence(image_filepath):
    tags = image_tags(image_filepath)
    confidences = [tag["confidence"] for tag in tags if tag["name"] in LEAF_TAGS]
    if confidences:
        return max(confidences)
    else:
        return 0

LEAFINESS_THRESHOLD = .6 # if an image is at least this likely to be a leaf, classify it as a leaf

def leafiness_classification(image_filepath):
    if leafiness_confidence(image_filepath) > LEAFINESS_THRESHOLD:
        return True
    else:
        return False

#if __name__ == "__main__":
#    images = parse_images()
#    print(len(images), "IMAGES...")
