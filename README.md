# Sarcasm-Detection
## Introduction
Sarcasm detection is a challenging task in natural language processing (NLP). This project aims to detect sarcasm in tweets using machine learning techniques. The process involves data collection, preprocessing, model training, and web deployment.

## Dependencies:
Numpy
Pandas
Flask
Scikit-learn
Tweepy
## Data Collection:
### Generate tweets:
Option 1: Use the provided tweets.json directly.
Option 2: Use tweepy.py to fetch tweets containing #sarcasm. This script creates a CSV file with sarcastic tweets labeled as 1. Additionally, generate non-sarcastic tweets by changing the query in the script. Merge both CSV files and randomize the data.
## Data Preprocessing:
Clean the text data by removing usernames, datetime, emojis, and hashtags from the tweets.
Run: python clean.py
## Model Training:
Train a sarcasm detection model using the preprocessed data. Random Forest Classifier is used in this project.
Run:
python model.py
## Web Deployment:
Use Flask to create a web application for sarcasm detection.
A basic input-output website is provided; however, customization is encouraged to make it more professional.
Run:
python flask.py
This starts a localhost web server. Visit "localhost:5000" in your browser.

### Next Steps:
Improving Model Performance: Experiment with different machine learning algorithms and hyperparameters to improve accuracy.
Enhancing Web Interface: Design a more user-friendly and visually appealing web interface.
Scalability: Scale the model and web application to handle larger datasets and higher traffic.
Feel free to expand and enhance this project to make it more professional and effective in detecting sarcasm in tweets. Your contributions are welcome!
