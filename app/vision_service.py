# adapted from: https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-analyze
from pdb import set_trace as breakpoint
from pprint import pprint
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("VISION_API_KEY", default="OOPS")
API_ENDPOINT = os.getenv("VISION_API_ENDPOINT", default="OOPS")


def analyze_image_url(image_url):
    request_url = f"{API_ENDPOINT}/vision/v2.0/analyze"
    headers = {"Ocp-Apim-Subscription-Key": API_KEY}
    params = {"visualFeatures": "Categories,Description,Color"}
    request_body = {"url": image_url}

    response = requests.post(request_url, headers=headers, params=params, json=request_body)
    response.raise_for_status() # does this raise if status not 200?

    parsed_response = json.loads(response.text)
    return parsed_response

if __name__ == "__main__":

    example_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
    print("IMAGE URL", example_url)

    parsed_response = analyze_url(example_url)
    pprint(parsed_response)

    #breakpoint()


    #from io import BytesIO
    #from PIL import Image
    ## If you are using a Jupyter notebook, uncomment the following line.
    ## %matplotlib inline
    #import matplotlib.pyplot as plt
    #
    ## Display the image and overlay it with the caption.
    #image = Image.open(BytesIO(requests.get(image_url).content))
    #plt.imshow(image)
    #plt.axis("off")
    #_ = plt.title(image_caption, size="x-large", y=-0.1)
    #plt.show()
