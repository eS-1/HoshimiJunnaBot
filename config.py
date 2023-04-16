import os
import tweepy


myClient = tweepy.Client(bearer_token=os.environ["BEARER_TOKEN"])
