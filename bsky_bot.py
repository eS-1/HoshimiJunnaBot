import atproto.exceptions
from config import bskyClient
from sentence import importTexts, makeSentence


def postText():
    text = makeSentence(importTexts())
    for i in range(100):
        try:
            bskyClient.send_post(text=text, langs=["jp"])
        except (atproto.exceptions.AtProtocolError):
            text = makeSentence(importTexts())
        else:
            break

if __name__ == "__main__":
    bskyClient.send_post("test tweet")
