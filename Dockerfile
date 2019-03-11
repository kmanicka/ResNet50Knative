FROM python:3.6
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r ./requirements.txt

# COPY resnet50_model.h5 /app
RUN wget https://github.com/kmanicka/ResNet50Knative/releases/download/resnet50/resnet50_model.h5 

COPY imagenet_class_index.json /app

COPY app.py /app
CMD ["python", "app.py"]~