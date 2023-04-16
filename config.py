import os
import tweepy


myClient = tweepy.Client(
    bearer_token=os.environ["BEARER_TOKEN"],
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_KEY_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"])
