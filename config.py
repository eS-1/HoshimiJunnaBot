import os

import tweepy
import atproto
from misskey import Misskey


myClient = tweepy.Client(
    bearer_token=os.environ["BEARER_TOKEN"],
    consumer_key=os.environ["API_KEY"],
    consumer_secret=os.environ["API_KEY_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

misskeyClient = Misskey("https://misskey.io/", os.environ["MISSKEY_TOKEN"])

bskyClient = atproto.Client()
bskyClient.login("hoshimijunnabot.bsky.social", os.environ["BLUESKY_BOT_PASS"])
