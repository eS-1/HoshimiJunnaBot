import random
from typing import List


def gyoshiteKotoba() -> str:
    texts: List[str] = []
    with open("gyoshiteKotoba.txt", encoding="UTF-8") as f:
        texts = [s.strip() for s in f.readlines()]
    
    first: List[str] = []
    second: List[str] = []
    third: List[str] = []
    names: List[str] = []
    for i in texts:
        text: List[str] = i.split(',')
        first.append(text[0])
        second.append(text[1])
        third.append(text[2])
        if len(text) == 4:
            names.append(text[3])
    
    size = len(first) - 1
    index0 = random.randint(0, size)
    index1 = random.randint(0, size)
    index2 = random.randint(0, size)

    # index0 = index1 = index2 = 0

    replyText: str = first[index0] + "\n" + second[index1] + "\n" + third[index2] + "\n\n"
    if index0 == index1 == index2 and index0 < len(names):
        replyText += names[index0] + "の言葉よ。"
    else:
        replyText += "……知らない言葉よ。"
    
    return replyText


if __name__ == "__main__":
    print(gyoshiteKotoba())
