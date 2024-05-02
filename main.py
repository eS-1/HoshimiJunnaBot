from apscheduler.schedulers.blocking import BlockingScheduler

from bsky_bot import postText
from misskey_bot import noteText
from twitter_bot import tweetText

twische = BlockingScheduler()


@twische.scheduled_job('interval', minutes=30, start_date="2024-05-03 00:00:00")
def timed_job():
    tweetText()
    noteText()
    postText()


if __name__ == "__main__":
    twische.start()
