import os
import pytest

from app.vision_service import analyze_image_url, analyze_image

CI = os.environ.get("CI") == "true"

EXPECTED_ATTRIBUTES = ["categories", "color", "description", "requestId", "metadata"]

@pytest.mark.skipif(CI, reason="prevent HTTP requests on CI, credentials not on CI")
def test_analyze_image_url():
    example_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/"
    example_url += "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
    parsed_response = analyze_image_url(example_url)
    assert list(parsed_response.keys()) == EXPECTED_ATTRIBUTES

@pytest.mark.skipif(CI, reason="prevent HTTP requests on CI, credentials not on CI")
def test_analyze_image():
    example_filepath = os.path.join(os.path.dirname(__file__), "img", "450px-Broadway_and_Times_Square_by_night.jpg")
    parsed_response = analyze_image(example_filepath)
    assert list(parsed_response.keys()) == EXPECTED_ATTRIBUTES
