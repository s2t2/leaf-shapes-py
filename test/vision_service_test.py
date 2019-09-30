#from pdb import set_trace as breakpoint
import os
import pytest

from app.vision_service import analyze_image, analyze_image_tags

CI = os.environ.get("CI") == "true"

EXPECTED_ATTRIBUTES = ["categories", "color", "tags", "description", "objects", "requestId", "metadata"]

#@pytest.mark.skipif(True, reason="prevent HTTP requests on CI, credentials not on CI")
#def test_analyze_image_url():
#    example_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/"
#    example_url += "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
#    parsed_response = analyze_image_url(example_url)
#    assert list(parsed_response.keys()) == EXPECTED_ATTRIBUTES

TEST_IMAGES_DIRPATH = os.path.join(os.path.dirname(__file__), "img")

@pytest.mark.skipif(CI, reason="prevent HTTP requests on CI, credentials not on CI")
def test_analyze_image():
    example_filepath = os.path.join(TEST_IMAGES_DIRPATH, "450px-Broadway_and_Times_Square_by_night.jpg")
    parsed_response = analyze_image(example_filepath)
    assert list(parsed_response.keys()) == EXPECTED_ATTRIBUTES

@pytest.mark.skipif(CI, reason="prevent HTTP requests on CI, credentials not on CI")
def test_analyze_image_tags():
    leaf_filepath = os.path.join(TEST_IMAGES_DIRPATH, "2d58d3f20ea40863b92e64c9d9c62ad53ea696b9f342797b85967680e3bd9eb4.jpg")
    leaf_tags = analyze_image_tags(leaf_filepath)
    assert leaf_tags == [
        {'name': 'text', 'confidence': 0.9871882200241089},
        {'name': 'book', 'confidence': 0.9109231233596802},
        {'name': 'leaf', 'confidence': 0.8837380409240723},
        {'name': 'plant', 'confidence': 0.7578558921813965}
    ]
    assert "leaf" in [tag["name"] for tag in leaf_tags]

    nonleaf_filepath = os.path.join(TEST_IMAGES_DIRPATH, "3c9eaca94c87f8bd0cca9d7596848add682ba95d640d2e05d09b6f717c5000a1.jpg")
    nonleaf_tags = analyze_image_tags(nonleaf_filepath)
    assert nonleaf_tags == [
        {'name': 'text', 'confidence': 0.975858211517334}
    ]
    assert "leaf" not in [tag["name"] for tag in nonleaf_tags]
