from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def recognize_breed(image):
    breeds = ["Golden Retriever", "Dalmatian", "German Shepherd"]

    return breeds[hash(image) % len(breeds)]

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
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)