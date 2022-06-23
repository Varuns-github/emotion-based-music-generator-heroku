from flask import Flask,Response,request,render_template,jsonify
import cv2
from os import environ
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import  load_model

app = Flask(__name__)
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # return frame
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

  
@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture')
def capture():
    # Capture frame-by-frame
    success, frame = camera.read()
    if not success:
        return "Error"
    else:
        # kill the camera
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # cv2.imshow('frame', frame)
            gray_img = gray_img[y:y + w, x:x + h]
        img = cv2.resize(gray_img, (48, 48))
        img_pixels = image.img_to_array(img)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        model = load_model("fer7_model.h5")
        predictions = model.predict(img_pixels)
        max_index = np.argmax(predictions[0])
        emotions = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise" ]
        predicted_emotion = emotions[max_index]

        print(predicted_emotion)

    return jsonify(status="success", predicted_emotion=predicted_emotion)

@app.route('/enable_camera')
def enable_camera():
    # set the global varibale camera to be true
    global camera
    camera = cv2.VideoCapture(0)
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(port=environ.get("PORT", 5000),host="0.0.0.0")