# Handwritten Text Recognition

This  uses the Hugging Face `transformers` model to recognise handwritten text from an uploaded image.
## Model in action

[![Model Inference](![Screenshot 2024-11-01 122304](https://github.com/user-attachments/assets/fa09aab3-f726-47d4-a84c-0ceca79e2cd8)
)](https://youtu.be/Il7Y1UyMASo))


[Watch the video]

## Setup Instructions
Here is how to test the model and get inferences for your handwritten texts

### 1. Clone the repository

`git clone https://github.com/cyberholic/Hand-Writing-Detection.git`
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


