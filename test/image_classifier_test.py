

import os

from app.image_classifier import image_tags, leafiness_confidence, leafiness_classification

TEST_IMAGES_DIRPATH = os.path.join(os.path.dirname(__file__), "img")
leaf_image_filepath = os.path.join(TEST_IMAGES_DIRPATH, "2d58d3f20ea40863b92e64c9d9c62ad53ea696b9f342797b85967680e3bd9eb4.jpeg")
nonleaf_image_filepath = os.path.join(TEST_IMAGES_DIRPATH, "3c9eaca94c87f8bd0cca9d7596848add682ba95d640d2e05d09b6f717c5000a1.jpeg")

def test_image_tags():
    #leaf_image_filepath
    # TAGS: [ { "name": "text", "confidence": 0.9871882 }, { "name": "book", "confidence": 0.9109231 }, { "name": "leaf", "confidence": 0.883738041 }, { "name": "plant", "confidence": 0.7578559 } ]
    # nonleaf_image_filepath
    # TAGS: [ { "name": "text", "confidence": 0.9758582 } ]
    assert False

def test_leafiness_confidence():
    assert False

def test_leafiness_classification():
    assert False
