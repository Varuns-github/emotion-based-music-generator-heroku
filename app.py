from os import environ
from flask import Flask,Response,request,render_template,jsonify
import cv2
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import  load_model
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = load_model("fer7_model.h5")

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/capture', methods=['POST'])
def capture():
    # get the json and decode it
    data = request.json
    # convert the image into png

    # save the image

    # convert the base64 string into raw bytes
    img_data = data['image']

    starter = img_data.find(',')
    image_data = img_data[starter+1:]
    image_data = bytes(image_data, encoding="ascii")
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    im.save('image.png')

    img = cv2.imread('image.png')

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (48, 48))
    img_pixels = image.img_to_array(img)
    img_pixels = np.expand_dims(img_pixels, axis=0)
    img_pixels /= 255
    predictions = model.predict(img_pixels)

    max_index = np.argmax(predictions[0])
    emotions = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise" ]
    predicted_emotion = emotions[max_index]

    return jsonify(status="success", predicted_emotion=predicted_emotion)

app.run(port=environ.get("PORT", 5000),host="0.0.0.0")
# app.run(debug=True)