import os
import pytest

from app.image_classifier import leafiness_confidence, leafiness_classification

CI = os.environ.get("CI") == "true"

TEST_IMAGES_DIRPATH = os.path.join(os.path.dirname(__file__), "img")
leaf_filepath = os.path.join(TEST_IMAGES_DIRPATH, "2d58d3f20ea40863b92e64c9d9c62ad53ea696b9f342797b85967680e3bd9eb4.jpg")
nonleaf_filepath = os.path.join(TEST_IMAGES_DIRPATH, "3c9eaca94c87f8bd0cca9d7596848add682ba95d640d2e05d09b6f717c5000a1.jpg")

#def test_leafiness_confidence():
#    assert False
#
#def test_leafiness_classification():
#    assert False
