import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

prediction_endpoint = os.getenv('PredictionEndpoint')
prediction_key = os.getenv('PredictionKey')
project_id = os.getenv('ProjectID')
model_name = os.getenv('ModelName')

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
prediction_client = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=prediction_credentials)

for image in os.listdir('test-images'):
    image_data = open(os.path.join('test-images',image), "rb").read()
    results = prediction_client.classify_image(project_id, model_name, image_data)

    # Loop over each label prediction and print any with probability > 50%
    for prediction in results.predictions:
          if prediction.probability > 0.5:
              print('{} ({:.0%})'.format(prediction.tag_name, prediction.probability))
