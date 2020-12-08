import os
import base64
import requests
from pathlib import Path

# Passing in a real face Image
with open(str(Path(__file__).resolve().parent) + '/images/1.png', 'rb') as img_file:
    my_string = base64.b64encode(img_file.read())

r = requests.post("http://0.0.0.0:5000/v2/detectcnic",
                  data={'image': my_string})

assert(r.status_code, "200")

# Passing in a fake Image
with open(str(Path(__file__).resolve().parent) + '/images/2.png', 'rb') as img_file:
    my_string = base64.b64encode(img_file.read())

r = requests.post("http://0.0.0.0:5000/v2/detectcnic",
                  data={'image': my_string})

assert(r.status_code, "403")
