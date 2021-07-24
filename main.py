from apscheduler.schedulers.blocking import BlockingScheduler
from tweetText import tweetText
from reply import replyAsBot

twische = BlockingScheduler()
replyJob = BlockingScheduler()


@twische.scheduled_job('interval', minutes=30, start_date="2021-07-19 00:00:00")
def timed_job():
    tweetText()


@replyJob.scheduled_job('interval', minutes=1)
def reply_job():
    replyAsBot()


if __name__ == "__main__":
    twische.start()
    replyJob.start()
