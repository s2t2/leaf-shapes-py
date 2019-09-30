from pdb import set_trace as breakpoint
from pprint import pprint
import os
import pytest

from app.vision_service import analyze_image_tags, analyze_image

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
    image_filepath = os.path.join(os.path.dirname(__file__), "..", "img", "imports",
        "Acer calcaratum Gagnep", "3ef3ac88e7a2d68f02a59fea866998ef336ebd24cef1c37a9da322048b4a5449.jpg"
    )
    tags = analyze_image_tags(image_filepath) #> [{'name': 'text', 'confidence': 0.9591830372810364}, {'name': 'screenshot', 'confidence': 0.5648662447929382}]
    breakpoint()

    #parsed_response = analyze_image(image_filepath)
    #>{
    #>    'categories': [
    #>        {'name': 'abstract_', 'score': 0.0078125},
    #>        {'name': 'others_', 'score': 0.01171875},
    #>        {'detail': {'landmarks': []}, 'name': 'outdoor_', 'score': 0.00390625}
    #>    ],
    #>    'color': {
    #>        'accentColor': 'B98C12',
    #>        'dominantColorBackground': 'White',
    #>        'dominantColorForeground': 'White',
    #>        'dominantColors': ['White'],
    #>        'isBWImg': False,
    #>        'isBwImg': False
    #>    },
    #>    'description': {
    #>        'captions': [
    #>            {'confidence': 0.5368590697912834, 'text': 'a close up of a tree'}
    #>        ],
    #>        'tags': ['photo', 'table', 'sitting', 'black', 'bird', 'tree', 'white', 'cat']
    #>    },
    #>    'metadata': {'format': 'Jpeg', 'height': 1343, 'width': 800},
    #>    'objects': [
    #>        {'confidence': 0.572, 'object': 'animal', 'rectangle': {'h': 389, 'w': 348, 'x': 236, 'y': 866}},
    #>        {'confidence': 0.552, 'object': 'mammal', 'parent': {'confidence': 0.694, 'object': 'animal'}, 'rectangle': {'h': 313, 'w': 294, 'x': 34, 'y': 966}}
    #>    ],
    #>    'requestId': 'c9712fd4-f47f-4db4-9597-de9bb7e891ce',
    #>    'tags': [
    #>        {'confidence': 0.9591830372810364, 'name': 'text'},
    #>        {'confidence': 0.5648662447929382, 'name': 'screenshot'}
    #>    ]
    #>}
