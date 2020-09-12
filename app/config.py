import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False
    
    # Enter your API Key and Custom Classifier ID below
    API_KEY = "5aFfvjjwoik8VgkEpTwv8eLFIeJo2ZJgjNsyPa9lZZl-"
    CLASSIFIER_ID = "Safety_Helmet_Detector_2040366225"
