FROM python:3.6
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r ./requirements.txt

COPY resnet50_model.h5 /app

COPY app.py /app
CMD ["python", "app.py"]~