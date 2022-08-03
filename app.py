import cv2
import base64
import numpy as np
from PIL import Image
from io import BytesIO
from os import environ
from dataset import return_music_url
from tensorflow.keras.models import  load_model
from tensorflow.keras.preprocessing import image
from flask import Flask,request,render_template,jsonify

app = Flask(__name__)
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = load_model("fer7_model.h5")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    img_data = data['image']

    starter = img_data.find(',')
    image_data = img_data[starter+1:]
    image_data = bytes(image_data, encoding="ascii")
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    img = np.array(im)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
    
    for (x, y, w, h) in faces_detected:
        gray_img = gray_img[y:y + w, x:x + h]

    roi_gray = cv2.resize(gray_img, (48, 48))
    img_pixels = image.img_to_array(roi_gray)
    img_pixels = np.expand_dims(img_pixels, axis=0)
    img_pixels /= 255

    predictions = model.predict(img_pixels)

    max_index = np.argmax(predictions[0])
    emotions = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise" ]
    predicted_emotion = emotions[max_index]

    predicted_music_url = return_music_url(predicted_emotion)
    predirect_music_url_a = predicted_music_url[0]
    predirect_music_url_b = predicted_music_url[1]
    
    return jsonify(status="success", predicted_emotion=predicted_emotion, predirect_music_url_a=predirect_music_url_a, predirect_music_url_b=predirect_music_url_b)

# app.run(port=environ.get("PORT", 5000),host="0.0.0.0")
app.run(debug=True)