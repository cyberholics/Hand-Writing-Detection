from flask import Flask, request, jsonify, render_template
from transformers import pipeline
from PIL import Image
import os

app = Flask(__name__)

# Load the handwritten text detection pipeline
pipe = pipeline("image-to-text", model="microsoft/trocr-base-handwritten", cache_dir="./model_cache")

# Path to store uploaded images temporarily
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Open the image and convert to RGB
        image = Image.open(file_path).convert("RGB")
        
        # Perform text recognition
        generated_text = pipe(image)
        os.remove(file_path)  # Clean up the uploaded file

        return jsonify({'recognized_text': generated_text[0]['generated_text']})

if __name__ == '__main__':
    app.run(debug=True)
 