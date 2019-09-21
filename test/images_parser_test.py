
from app.images_parser import parse_families, Fam, parse_images, Img

def test_parse_families():
    fams = parse_families()
    assert len(fams) == 11
    assert isinstance(fams[0], Fam)
    assert [fam.name for fam in fams] == [
        "Acer calcaratum Gagnep",
        "Acer davidii Franch",
        "Acer fabri Hance",
        "Acer fabri var. rubrocarpum Metc",
        "Acer laevigatum Wall",
        "Acer laurinum Hassk",
        "Acer palmatum C.P.Thunberg ex A.Murray",
        "Acer rubrum L",
        "Acer saccharum Marshall",
        "Acer stachyophyllum Hiern",
        "Acer truncatum Bunge"
    ]

def test_parse_images():
    images = parse_images()
    assert len(images) == 894
    assert isinstance(images[0], Img)
