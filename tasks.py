from celery import Celery
import twitter

app = Celery('tasks', backend='redis', broker='redis://localhost:6379')

@app.task
def load_feed():
    pass
