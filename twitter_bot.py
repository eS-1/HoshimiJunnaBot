import tweepy

from config import myClient
from sentence import importTexts, makeSentence


def tweetText():
    '''
    ツイートする。
    '''
    texts = importTexts()
    tweet = makeSentence(texts)

    i = 0
    while i < 100:
        try:
            myClient.create_tweet(text=tweet)
        except tweepy.TweepyException:
            i += 1
            tweet = makeSentence(texts)
        else:
            break


# テスト用
if __name__ == "__main__":
    print(makeSentence(importTexts()))
