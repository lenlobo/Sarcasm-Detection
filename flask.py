from flask import Flask, request, render_template, redirect
from Model import rfc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
app = Flask(__name__)
@app.route('/kek',methods=['GET','POST'])
def sarcaaa():
	if request.method =='POST':
		vList=[]
		sent=request.form['sent']
		sid=SentimentIntensityAnalyzer()
		valt=sid.polarity_scores(sent)
		for key,val in valt.items():
			vList.append(val)
		result=rfc.predict([vList])
		if result[0]==1:
			message='Sarcasm'
		elif result[0]==0:
			message='Not sarcasm'
		return render_template('kek.html',messages=message)
@app.route('/')
def home():			 
    return render_template('home.html')
if __name__ == '__main__':
	app.run(debug=True, port = 5000)
