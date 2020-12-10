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

model = os.getcwd() + "/model.h5"

classifier = tensorflow.keras.models.load_model(model, compile=False)


def _base64_to_image(base_string):
    base_string = base64.b64decode(base_string)
    base_string = io.BytesIO(base_string)
    base_string = Image.open(base_string)
    base_string = base_string.resize((128, 128))
    base_string = np.array(base_string)
    base_string = base_string[:, :, ::-1].copy()

    return base_string


def CheckReality(img):
    img = _base64_to_image(img)
    # img = image.load_img(img, target_size=(128, 128))
    img = image.img_to_array(img)
    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = classifier.predict(img, batch_size=None, steps=1)

    if (prediction[:, :] > 0.5):
        logging.info("FAKE")
        return 0

    logging.info("REAL")
    return 1
