from apscheduler.schedulers.blocking import BlockingScheduler
from reply import replyAsBot

replyJob = BlockingScheduler()


@replyJob.scheduled_job('interval', minutes=1)
def reply_job():
    replyAsBot()


if __name__ == "__main__":
    replyJob.start()
