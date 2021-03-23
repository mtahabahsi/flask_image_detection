from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from imageai.Detection import ObjectDetection



def prediction1(input_path):
    detector = ObjectDetection()
    model_path = "models/yolo-tiny.h5"
    output_path = "static/result/newimage.jpg"
    cikti = " "
    detector.setModelTypeAsTinyYOLOv3()

    detector.setModelPath(model_path)
    detector.loadModel()

    detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
    print(detection)
    for detect in detection:
        cikti += detect["name"]
        cikti += ":"
        cikti += str(detect["percentage_probability"])
        cikti += "\n"
        



    return cikti




    ########

print('Model loaded. Check http://127.0.0.1:2000/')
image_review_tool = Flask(__name__)

MODEL_PATH = 'models/yolo-tiny.h5'
model = load_model(MODEL_PATH)
def prediction(image_path, model):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict_classes(images, batch_size=10)
    return classes

@image_review_tool.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@image_review_tool.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        # Make prediction
        result_t = prediction1(file_path)

        return result_t
    return None

@image_review_tool.route('/mount', methods=['GET', 'POST'])
def mount_image():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'image', secure_filename(f.filename))
        f.save(file_path)
        print(secure_filename(f.filename))
        print("mount image/" + secure_filename(f.filename) + " mounts/hadibakimm")
        
        os.system("mount image/" + secure_filename(f.filename) + " mounts/hadibakimm")

        return "çalıştı işte"
    return None







if __name__ =="__main__":
    image_review_tool.run(debug =True, port=2000)
    #http_server = WSGIServer(('', 2000), image_review_tool)
    #http_server.serve_forever()



