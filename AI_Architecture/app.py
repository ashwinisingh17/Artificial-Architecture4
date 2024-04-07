from flask import Flask, send_file, request, jsonify
import os
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the directory where images are stored
IMAGE_DIRECTORY = r'C:\Users\Adarsh Verma\Downloads\ROBIN\ROBIN'

@app.route('/execute-python-script', methods=['GET', 'POST'])
def execute_python_script():
    if request.method == 'POST':
        try:
            request_data = request.json['value']
            request_data = int(request_data)  # Convert to integer
            
            if request_data == 3:
                image_directory = os.path.join(IMAGE_DIRECTORY, 'Dataset_3rooms')
                num_images_to_select = 4
            elif request_data == 4:
                image_directory = os.path.join(IMAGE_DIRECTORY, 'Dataset_4rooms')
                num_images_to_select = 4
            elif request_data == 5:
                image_directory = os.path.join(IMAGE_DIRECTORY, 'Dataset_5rooms')
                num_images_to_select = 4
            else:
                return jsonify({"error": "Invalid request value"})
            
            image_files = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
            num_images_to_select = min(num_images_to_select, len(image_files))
            random_images = random.sample(image_files, num_images_to_select)
            
            return jsonify({"random_images": random_images})
        except Exception as e:
            return jsonify({'error': str(e)}) 
    else:
        return "This is a GET request. Use a POST request to send data."

@app.route('/images/<path:filename>')
def serve_image(filename):
    # Construct the path to the requested image
    image_path = os.path.join(IMAGE_DIRECTORY, filename)
    # Return the image file
    return send_file(image_path)

if __name__ == "__main__":
    app.run(debug=True)

