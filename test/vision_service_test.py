import os
import pytest

from app.vision_service import analyze_image_url

CI = os.environ.get("CI") == "true"

@pytest.mark.skipif(CI, reason="1) prevent HTTP requests on CI, 2) credentials not on CI")
def test_analyze_image_url():
    example_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
    parsed_response = analyze_image_url(example_url)
    assert list(parsed_response.keys()) == [
        "categories", "color", "description", "requestId", "metadata"
    ]
