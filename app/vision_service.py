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

def analyze_image(image_filepath):
    request_url = f"{API_ENDPOINT}/vision/v2.0/analyze"
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/octet-stream" # avoids "TypeError: Object of type 'bytes' is not JSON serializable"
    }
    params = {"visualFeatures": "Categories,Description,Color"}

    #request_body = {"url": image_url}

    # Supported input methods: raw image binary or image URL.
    #breakpoint()
    # https://stackoverflow.com/questions/44126333/python-method-to-upload-an-image-to-microsoft-cognitive-vision-from-local-machin

    with open(image_filepath, "rb") as image_file:
        request_body = image_file.read()

    #requests.post(api_url,
    #                params=params,
    #                headers=header,
    #                data=img_data)

    response = requests.post(request_url, headers=headers, params=params, data=request_body) # needs to be "data" not "json"
    response.raise_for_status() # does this raise if status not 200?

    parsed_response = json.loads(response.text)
    return parsed_response

if __name__ == "__main__":

    #example_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
    #print("IMAGE URL", example_url)
    #parsed_response = analyze_image_url(example_url)
    #pprint(parsed_response)

    #breakpoint()

    example_filepath = os.path.join(os.path.dirname(__file__), "test", "img", "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg")
    print("IMAGE FILEPATH", example_filepath)
    parsed_response = analyze_url(example_filepath)
    pprint(parsed_response)

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
