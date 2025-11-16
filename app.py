from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model("dog_breed_model.keras")
with open("class_names.txt", "r", encoding="utf-8") as f:
    class_names = [line.strip() for line in f.readlines()]

IMG_SIZE = (224, 224)

def recognize_breed(image):
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)

    arr = np.array(image)
    arr = np.expand_dims(arr, axis=0)

    arr = tf.keras.applications.mobilenet_v2.preprocess_input(arr)

    preds = model.predict(arr)
    idx = np.argmax(preds[0])

    raw_label = class_names[idx]
    pretty_label = raw_label.replace("_", " ")
    return pretty_label

@app.route('/api/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    try:
        image = Image.open(file.stream)
        breed = recognize_breed(image)
        return jsonify({"breed": breed})
    except Exception as e:
        print("Error in /api/predict:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
