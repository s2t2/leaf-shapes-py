
from app.images_parser import parse_images, Img

def test_parse_images():

    images = parse_images()

    assert len(images) == 894
    assert isinstance(images[0], Img)
