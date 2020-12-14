import os
import io
import base64
import imutils
import logging
import tensorflow
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing import image

model = os.getcwd() + "/model.h5"

classifier = tensorflow.keras.models.load_model(model, compile=False)


def _base64_to_image(base_string):
    base_string = base64.b64decode(base_string)
    base_string = io.BytesIO(base_string)
    base_string = Image.open(base_string)
    base_string = base_string.resize((128, 128))
    img = image.img_to_array(base_string)
    img = img / 255
    img = np.expand_dims(img, axis=0)

    return img


def check_reality(img):
    img = _base64_to_image(img)
    prediction = classifier.predict(img, batch_size=None, steps=1)

    if (prediction[:, :] > 0.5):
        logging.info("FAKE")
        return 0

    logging.info("REAL")
    return 1
