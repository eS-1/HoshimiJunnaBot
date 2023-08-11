from misskey.misskey import (MisskeyAPIException,
                             MisskeyAuthorizeFailedException)

from config import misskeyClient
from sentence import importTexts, makeSentence


def noteText():
    text = makeSentence(importTexts())
    for i in range(100):
        try:
            misskeyClient.notes_create(text=text)
        except (MisskeyAPIException, MisskeyAuthorizeFailedException):
            text = makeSentence(importTexts())
        else:
            break


if __name__ == "__main__":
    noteText()
