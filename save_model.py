# USAGE
# Start the server:
# 	python save_model.py

# import the necessary packages
from keras.applications import ResNet50
import tensorflow as tf


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print((" Saving ResNet50 Keras model resnet50_model.h5"))
    model = ResNet50(weights="imagenet")
    model.save('resnet50_model.h5')

