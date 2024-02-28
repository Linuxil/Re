from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .func import counter

def start():
    now = datetime.now()
    scheduler = BackgroundScheduler()
    scheduler.add_job(counter, 'interval', seconds=60)
    scheduler.start()
