# adapted from: https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts/python-analyze

import os
import json
import requests

API_KEY = os.getenv("VISION_API_KEY")
API_ENDPOINT = os.getenv("VISION_API_ENDPOINT")

request_url = API_ENDPOINT + "vision/v2.0/analyze"
headers = {'Ocp-Apim-Subscription-Key': API_KEY}
params = {'visualFeatures': 'Categories,Description,Color'}
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/" + "Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg"
request_body = {'url': image_url}
response = requests.post(request_url, headers=headers, params=params, json=request_body)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(json.dumps(response.json()))
image_caption = analysis["description"]["captions"][0]["text"].capitalize()



exit()

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
