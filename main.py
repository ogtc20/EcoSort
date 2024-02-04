import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

prediction_endpoint = os.getenv('PredictionEndpoint')
prediction_key = os.getenv('PredictionKey')
project_id = os.getenv('ProjectID')
model_name = os.getenv('ModelName')

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=prediction_credentials)

img_url1 = 'https://sushiumi.ca/cdn/shop/products/20210406_173613_530x@2x.jpg?v=1617745009'
response = predictor.classify_image_url(project_id, model_name, img_url1)

print(response.deserialize)

