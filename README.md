# Dog Breed Recognition (Golden Retriever & Dalmatian)

A simple end-to-end machine learning project that classifies dog images as either **Golden Retriever** or **Dalmatian**.  
The project includes:

- A **TensorFlow training script** for your own dataset  
- A **Flask API backend** for running predictions  
- A **React frontend** for uploading images and showing results  

---

## Features

- **Image Upload** – User can upload a dog image from the browser  
- **Custom Dataset** – Uses your own images stored locally (`data/dogs/...`)  
- **TensorFlow Model** – MobileNetV2-based classifier (transfer learning)  
- **Flask API** – `/api/predict` endpoint for inference  
- **React UI** – Simple interface to test predictions

---

## Project Structure

```
image-recognition/
│
├── app.py                 # Flask backend for prediction
├── train_model.py         # Script to train the TensorFlow model
├── dog_breed_model.keras  # Saved model (generated after training)
├── class_names.txt        # Saved class labels
│
├── data/
│   └── dogs/
│       ├── Dalmatian/
│       └── Golden_Retriever/
│
├── src/                   # React frontend
│   ├── App.js
│   └── ...other React files
│
└── package.json
```

---

## Training the Model

1. Place your images into:

```
data/dogs/Golden_Retriever/
data/dogs/Dalmatian/
```

2. Run the training script:

```bash
python train_model.py
```

This generates:

- `dog_breed_model.keras`  
- `class_names.txt`

---

## Running the Backend (Flask)

```bash
python app.py
```

Runs at:

```
http://localhost:5000
```

---

## Running the Frontend (React)

```bash
npm install
npm start
```

Runs at:

```
http://localhost:3000
```

The frontend will send prediction requests to the backend's `/api/predict` endpoint.

---

## How Prediction Works

1. User uploads an image  
2. React sends it → `POST /api/predict`  
3. Flask loads the TensorFlow model  
4. Image is resized and preprocessed  
5. Model returns either:
   - **Golden Retriever**
   - **Dalmatian**