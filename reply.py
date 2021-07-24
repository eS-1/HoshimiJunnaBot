import time
import tweepy
from config import myAPI
from gyoshiteKotoba import gyoshiteKotoba


def replyAsBot():
    nowTime: float = time.time()
    status = myAPI.mentions_timeline(count=20)

    for mention in status:
        mentionTime = mention.created_at.timestamp()

        baseText: str = "@" + str(mention.user.screen_name) + " "

        if nowTime - mentionTime < 60:
            if "御して言葉" in mention.text:
                replyText = baseText + gyoshiteKotoba()
            
                i = 0
                while i < 100:
                    try:
                        myAPI.update_status(status=replyText, in_reply_to_status_id=mention.id)
                    except tweepy.TweepError:
                        i += 1
                        replyText = baseText + gyoshiteKotoba()
                    else:
                        break


def test():
    status = myAPI.mentions_timeline(cont=20)
    for mention in status:
        mentionTime = mention.created_at.timestamp()
        print(time.time() - mentionTime)


if __name__ == "__main__":
    test()
