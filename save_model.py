# USAGE
# Start the server:
# 	python save_model.py
#
# Small util file to save ResNet50 as a .h5 file locally. 


from keras.applications import ResNet50
import tensorflow as tf


if __name__ == "__main__":
    print((" Building ResNet50 Keras App"))
    model = ResNet50(weights="imagenet")

    print((" Saving ResNet50 Keras model resnet50_model.h5"))
    model.save('resnet50_model.h5')

