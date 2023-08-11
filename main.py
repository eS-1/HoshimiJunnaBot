from apscheduler.schedulers.blocking import BlockingScheduler

from misskey_bot import noteText
from twitter_bot import tweetText

twische = BlockingScheduler()


@twische.scheduled_job('interval', minutes=30, start_date="2023-08-12 00:30:00")
def timed_job():
    tweetText()
    noteText()


if __name__ == "__main__":
    twische.start()
