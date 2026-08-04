# Dog Breed Recognition

Upload a photo of a dog and the app identifies it as a golden retriever or a
dalmatian. Those are the only two classes it knows.

The project covers the whole chain: collecting the images, training the model,
serving it through an API and uploading to it from a web page. The model is a
MobileNetV2 base with a new top layer trained on twelve photos.

## Status

All three pieces work and talk to each other. The trained model is committed, so you
can run it without training anything yourself.

Working right now:

- Training script that reads `data/dogs/`, trains a new top layer and saves the model
- Flask API with one endpoint, `POST /api/predict`, taking an uploaded file
- React page with a file picker that shows the predicted breed
- Class names saved next to the model, so adding a breed does not mean editing code

Not done yet:

- Twelve training images, six per breed, with a fifth of those held back for
  validation. Enough to show the pipeline works, not enough for reliable results.
- Every image gets one of the two labels. Nothing checks the confidence score, so a
  photo of something that is not a dog still returns a breed.
- The probability is calculated and then discarded. Only the label is returned.
- No `requirements.txt`, so the Python dependencies have to be installed by hand.
- Flask runs with `debug=True`, and the API address is hardcoded in `src/App.js`.
- `src/App.test.js` is still the one Create React App generated, looking for a "learn
  react" link that no longer exists, so `npm test` fails.

## Tech

TensorFlow and Keras for the model: transfer learning on MobileNetV2 with ImageNet
weights and the base frozen. Flask with flask-cors serves the predictions and Pillow
opens the uploaded file. The front end is Create React App with React 18, one
component, no router.

Images are resized to 224 by 224 and run through the MobileNetV2 preprocessing in both
training and prediction. The two have to match, or the predictions are meaningless.

## Running it

Python 3 and Node are both needed. Install the Python dependencies first, since there
is no requirements file yet:

```bash
pip install tensorflow flask flask-cors pillow numpy
```

Start the API:

```bash
python app.py
```

It listens on http://localhost:5000. On macOS that port is often already taken by the
AirPlay receiver, which can be turned off in System Settings under General, AirDrop
and Handoff.

Then the front end, in a second terminal:

```bash
npm install
npm start
```

That opens http://localhost:3000. Pick an image and press the button. The first
prediction is slow while TensorFlow warms up.

## Training it again

The model in the repo is ready to use, so this is only needed when the pictures
change. Images go in folders named after the breed:

```
data/dogs/Golden_Retriever/
data/dogs/Dalmatian/
```

Then:

```bash
python train_model.py
```

Five epochs, and it writes `dog_breed_model.keras` and `class_names.txt`. The folder
names become the labels, so a third folder is all it takes to add a third breed.
Restart the API afterwards; the model is loaded once at startup.

## Layout of the code

```
train_model.py          trains the model, writes the two files below
dog_breed_model.keras   the trained model, committed to the repo
class_names.txt         one label per line, in the order the model outputs them
app.py                  Flask API, loads the model and serves /api/predict
data/dogs/              training images, one folder per breed
src/App.js              the entire front end
public/                 Create React App shell
```

## How a prediction works

The browser posts the file as `multipart/form-data` to `/api/predict`. Flask opens it
with Pillow, converts to RGB, resizes to 224 by 224 and runs the MobileNetV2
preprocessing. The model returns a probability per class, `argmax` takes the highest,
and the matching line of `class_names.txt` comes back as JSON with the underscore
swapped for a space.

## Next up

1. Many more images per breed
2. Return the confidence, and say "not sure" below some threshold
3. A `requirements.txt`
4. Delete or rewrite the leftover Create React App test
5. More breeds, which only requires adding more folders
