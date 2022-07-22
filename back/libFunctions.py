import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

from PIL.Image import Image
import numpy as np
from PIL import Image
import re
import numpy as np
from PIL import Image
import imagesize
import tensorflow as tf

from sklearn.model_selection import train_test_split
from keras import backend
from keras.layers import Activation
from keras.layers import Input, Lambda, Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.models import Sequential, Model
from tensorflow.keras.optimizers import RMSprop

# from tensorflow.keras.optimizers import RMSprop


def convert_number(n,number):
    x = [a for a in str(number)]
    arr=['0' for i in range(n)]
    for i in range(len(x)):
        arr[-(i+1)]=x[-(i+1)]
    return "".join(arr)


def read_image(image_path, size=(112, 92)):
    """returns processed images"""
    # Open image and convert to grayscale.
    image = Image.open(image_path)
    image = image.convert("L")

    image_array = np.array(image)

    # Resize image to 128, 256 using bilinear interpolation.
    im = Image.fromarray(image_array)
    size = tuple((np.array(im.size) * 0.99999).astype(int))
    image_array_processed = np.array(im.resize(size, Image.BILINEAR))

    # Invert pixel values.
    image_array_processed = 1 - image_array_processed

    # Normalize by dividing pixel values with standard deviation.
    image_array_processed = image_array_processed / np.std(image_array_processed)

    # Expand dimension to (155, 220, 1)
    # image_array_processed = np.expand_dims(image_array_processed, axis=2)

    return image_array_processed