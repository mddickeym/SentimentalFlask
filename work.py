from flask import Flask, request, render_template
import tweepy
import requests


x = Flask(__name__)


@x.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@x.route('/redirect/', methods=['GET', 'POST'])
def redirect():
    if(request.method == 'POST'):
        hashtag = request.form['hashtag']
        return render_template('redirect.html', hashtag=hashtag)

##import data from redirect

##Create the home page, ask the user for hashtag, pass hashtag to next page
@x.route('/<int:positive>/<int:neutral>/<int:negative>/<hashtag>/',  methods=['GET', 'POST'])
def profile(positive, neutral, negative, hashtag):
    return render_template('results.html', positive=positive, negative=negative, neutral=neutral, hashtag=hashtag)



if(__name__ == "__main__"):
    x.run(debug=True)

##put this code in the methods above below the routing
##call twitter class and pass it the variable, and it returns the three numbers
hashtag = requests.get("localhost:5000/redirect/").text

text = hashtag.split(" ")

profile(60, 45, 33, text[2])
