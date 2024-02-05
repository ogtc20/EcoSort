from flask import Flask, request
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import base64

app = Flask(__name__)

# Function to return the image classification using the image 
def azure_classify(image_data):
    # Variables required to utlized the Custom Vision API
    prediction_endpoint = os.getenv('PredictionEndpoint')
    prediction_key = os.getenv('PredictionKey')
    project_id = os.getenv('ProjectID')
    model_name = os.getenv('ModelName')

    # Create a prediction instance using the classification model
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    prediction_client = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=prediction_credentials)

    # Store the classification results
    results = prediction_client.classify_image(project_id, model_name, image_data)
    
    toReturn = ""
    # Loop over each label prediction and print any with probability > 50%
    for prediction in results.predictions:
        if prediction.probability > 0.5:
            classification, confidence = prediction.tag_name, prediction.probability
            print(classification, confidence)
            if ((classification == "Plastic") or (classification == "Paper") or (classification == "Cardboard") or (classification == "Battery") or (classification == "Glass") or (classification == "Metal")):
                toReturn = classification + ", Recycle (" + '{:.0%}'.format(confidence) +" confident)"
            elif (classification == "Biological"):
                toReturn = classification + ", Organic Waste (" + '{:.0%}'.format(confidence) +" confident)"
            else:
                toReturn = classification + ", Garbage (" + '{:.0%}'.format(confidence) +" confident)"
            # toReturn += ('{} ({:.0%})'.format(prediction.tag_name, prediction.probability))
            # toReturn += '\n'
    return toReturn
#battery, biological, cardboard, clothes, glass, metal, paper, plastic, shoes, trash

#organic: biological
#recycle: paper, cardboard, battery, glass, metal,
#garbage: shoes, clothes, trash,

@app.route('/api', methods=['POST'])
def hello_world():
    data = request.get_json(force=True)
    image_data = data['image']
    imgdata = base64.b64decode(image_data) #the image sent over by the phone
    filename = 'cam_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    toReturn = azure_classify(imgdata)
    
    return toReturn #the text that gets sent back to the phone

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)