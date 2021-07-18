from apscheduler.schedulers.blocking import BlockingScheduler
from tweetText import tweetText

twische = BlockingScheduler()


@twische.scheduled_job('interval', minutes=30, start_date="2021-07-18 23:30:00")
def timed_job():
    tweetText()


if __name__ == "__main__":
    twische.start()
