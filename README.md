# Handwritten Text Recognition Flask App

This  uses the Hugging Face `transformers` model to recognise handwritten text from an uploaded image.

## Setup Instructions
Here is how to test the model and get inferences for your handwritten texts

### 1. Clone the repository

`git clone https://github.com/cyberholics/Hand-Writing-Detection.git`
`cd Hand-Writing-Detection `

### 2. Set up the environment using Conda

`conda env create -f environment.yml`
`conda activate HWR`

### 3. Run the Flask App

After setting up the environment, run the Flask app: `python app.py`
This will start the server, and you can access the app at http://127.0.0.1:5000 in your browser.

### 4. Usage
Navigate to the app, upload an image containing your handwritten text, or use your camera.
The app will return the recognised text.


