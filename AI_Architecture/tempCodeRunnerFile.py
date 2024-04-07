from flask import Flask, request, jsonify
import os
import random

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5500')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

# Handle preflight requests
@app.route('/bedroom', methods=['OPTIONS'])
def options_bedroom():
    response = jsonify({'message': 'CORS preflight request successful'})
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response


# Diabetes controller
@app.route('/bedroom', methods=['POST'])
def diagnose_diabetes():
    try:
        request_data = request.json
        if request_data == 3:
            image_directory = r'C:\Users\Adarsh Verma\Downloads\ROBIN\ROBIN\Dataset_3rooms'
            num_images_to_select = 4
        elif request_data == 4:
            image_directory = r'C:\Users\Adarsh Verma\Downloads\ROBIN\ROBIN\Dataset_4rooms'
            num_images_to_select = 4
        elif request_data == 5:
            image_directory = r'C:\Users\Adarsh Verma\Downloads\ROBIN\ROBIN\Dataset_5rooms'
            num_images_to_select = 4
        else:
            return jsonify({"error": "Invalid request value"})
        
        image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]
        num_images_to_select = min(num_images_to_select, len(image_files))
        random_images = random.sample(image_files, num_images_to_select)
        
        print("Randomly selected images:", random_images)
        return jsonify({"random_images": random_images})
    except Exception as e:
        return jsonify({'error': str(e)}) 

if __name__ == '__main__':
    app.run(debug=True)
