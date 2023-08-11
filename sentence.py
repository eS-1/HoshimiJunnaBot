import random
from typing import List


def importTexts() -> List[str]:
    '''
    テキストファイルから文章を取得する。
    '''
    texts: List[str] = []
    with open("tweetTexts.txt", encoding="UTF-8") as f:
        texts = [s.strip() for s in f.readlines()]
    return texts


def makeSentence(texts: List[str]) -> str:
    '''
    引数の文章を例の台詞っぽくする。
    '''
    text: str = random.choice(texts)
    phrase: List[str] = text.split(',')
    textInTweet: str = "「" + phrase[0] + "」" + phrase[1] + "の言葉よ。"
    return textInTweet


if __name__ == "__main__":
    print(makeSentence(importTexts()))
