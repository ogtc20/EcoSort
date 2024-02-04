# EcoSort - Your Waste Classification Companion

EcoSort is an Android application that prompts you to take a picture of an item that is meant to be thrown away and returns a result for which disposal bin the item is appropriate. For the application to determine what the material of the item is, we used a custom image classification model that predicts which material the item is made out of. The model was trained and hosted using Microsoft Azure's Custom Vision service, which receives images from the app through API calls and returns a prediction label.

As university students, we come across frequent occurrences of neglect when it comes to waste disposal. Most people don't consider their environmental impact when they are disposing of their waste, as people just want to throw away their trash and move on with their day. After seeing how many items were placed into the wrong disposal bin, we wanted to create a quick solution that would help people place waste in the correct bins. The time it takes to research which materials go in what bin is the biggest deterrent for people placing their waste in the correct bins. To combat this, we decided to build a mobile application for this project, as it is the quickest and most automatic way for people to gain information for these decisions.

## How to use

- **Waste Classification**: Simply take a photo of an item, and EcoSort's AI-powered image classification will determine which disposal bin the item belongs in. 

## Getting Started

### Prerequisites

- You need an Android smartphone to use EcoSort.

### Installation

- Download and install the Ecosort APK file onto your Android device.

- If you'd like a quick demo of the vision model, you can do so by running the <code>main.py</code> file independently. To     do this, you'll have to install a couple of packages by running a set of commands on your terminal (you'll need to have      installed pip onto your device for these commands to be valid)

  <code>pip install azure.cognitiveservices.vision.customvision</code>

  <code>pip install msrest</code>

## Credits
- Our image classification model is currently being hosted with Microsoft Azure's Custom Vision service. The model was trained with Azure's Custom Vision web-based studio, which can be found at: https://www.customvision.ai/

- The data used to train the model was sourced from a garbage classification dataset created by Mostafa Mohammed. The    dataset features thousands of pictures of trash that are labelled with their classifications. You can access the dataset     here: https://www.kaggle.com/datasets/mostafaabla/garbage-classification
---
