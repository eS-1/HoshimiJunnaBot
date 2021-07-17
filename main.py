from apscheduler.schedulers.blocking import BlockingScheduler
from tweetText import tweetText

twische = BlockingScheduler()


@twische.scheduled_job('interval', minutes=1)
def timed_job():
    tweetText()


if __name__ == "__main__":
    twische.start()
