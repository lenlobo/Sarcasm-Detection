# Sarcasm-Detection

## Dependencies:
* Numpy
* Pandas
* Flask
* Scikit-learn
* Tweepy
## Generate tweets :
Can directly use the tweets.json directly 
or
 ### run python tweepy.py
  Creates a csv file with tweets containing #sarcasm. Tweepy takes in query which is #sarcasm and the number of tweets to be extracted, that is count.
  Make a column using an ipynb notebook such as jupyter into the csv called label. Set label to 1 for all the sarcastic tweets
  Do the same, just change the query in the tweepy.py file to anything random. for example q='#airlines'.
  This will generate tweets which are not sarcastic. Make the label column for the same with value 0 and merge both the csv files and randomize the data.
 ## Data Preprocessing :
  It is important to clean the text(tweets) data by removing the Username,Datetime, emoji's and hashtags from the tweets
 ## run python clean.py 
 this will clean the dataset row by row.
 ## Next run python model.py
  This will create a model. The model used here is RandomForest. The model is used for prediction or classification of the tweets.
 ## Next run python flask.py
  Flask is an module for python to connect between HTML5 websites and the Python code, for example the model here.
  This should start a localhost webserver, go to the link "localhost:5000".
 
 ## I've created a basic input output website as it was not the highlight of this project, one can create the website on its own as well just change the 'paths' in the flask.py file.
