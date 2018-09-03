import time

from celery import Celery

broker = "amqp://127.0.0.1:5672"
backend = "redis://127.0.0.1:6379/0"

app = Celery("my_task", broker=broker, backend=backend)


@app.task
def add(x, y):
    time.sleep(5)
    return x + y
