from apscheduler.schedulers.blocking import BlockingScheduler
from reply import replyAsBot

replyJob = BlockingScheduler()


@replyJob.scheduled_job('interval', minutes=5)
def reply_job():
    replyAsBot()


if __name__ == "__main__":
    replyJob.start()
