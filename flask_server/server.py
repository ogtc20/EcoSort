from flask import Flask, request
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import base64

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def hello_world():
    data = request.get_json(force=True)
    image_data = data['image']
    imgdata = base64.b64decode(image_data)
    filename = 'cam_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return 'Receive Successfully and Saved image'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)