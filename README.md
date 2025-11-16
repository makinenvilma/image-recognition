# Image Recognition App

A small project exploring image-recognition techniques in Python.  
Users can upload an image (or use a camera input), and the app runs basic preprocessing and a model/pipeline to recognize objects or classify the image.  
Built end-to-end to practice ML workflows and web integration.

## Features

- **Image Upload / Camera Input** – Test recognition on your own images.  
- **Preprocessing Pipeline** – Resize, normalize, and transform images before inference.  
- **Prediction Output** – Displays predicted label(s) and basic confidence/score.  
- **Simple UI** – Minimal interface for quick experiments and demos.

## Screenshots

**Sample Prediction**  
_Example result view after submitting an image._

**Preprocessing Preview**  
_Example view of preprocessed/augmented image before inference._

## Tech Stack

- **Back-end:** Python (web server, e.g., Flask/FastAPI)  
- **ML / Vision:** (e.g., OpenCV, scikit-image, scikit-learn, TensorFlow or PyTorch)  
- **Front-end:** HTML, CSS, JavaScript (basic demo UI)  

## How It Works

1. **Input** – User selects or captures an image.  
2. **Preprocessing** – The image is resized/normalized and optionally filtered/augmented.  
3. **Inference** – The model or algorithm produces predictions (class label or features).  
4. **Display** – The app shows the result and any relevant scores.

## Installation & Setup

> Use the Python setup first. If you also have a separate front-end, run it from the project root.

### 1) Back-end (Python)

1. **Clone the repository**
   ```bash
   git clone https://github.com/makinenvilma/image-recognition.git
   cd image-recognition
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000` (or as defined in `app.py`).

### 2) Front-end (optional)

1. **Install Node dependencies**
   ```bash
   npm install
   ```

2. **Start the dev server**
   ```bash
   npm run dev
   ```
