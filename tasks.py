from celery import Celery
from TwitterSearch import TwitterSearchOrder, TwitterSearch
app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def test_task():
    return 42

@app.task
def getTweetsByWords(authdata, word,limit=100):
    tso = TwitterSearchOrder()
    tso.set_keywords([word])
    tso.set_include_entities(False)
    ts = TwitterSearch(consumer_key=authdata['consumer_key'], consumer_secret=authdata['consumer_secret'], access_token=authdata['access_token'], access_token_secret=authdata['access_token_secret'])
    result = []
    c = 0
    for tweet in ts.search_tweets_iterable(tso):
        if c == limit:
            break
        result.append(tweet['text'])
        print(c)
        c+=1
    return {'status': 'Task Completed', 'result': result}


@app.task(bind=True)
def error_handler(sjelf,uuid):
    result = self.app.AsyncResult(uuid)
    print("Task {0} contain errors {1}".format(uuid, result.traceback))

