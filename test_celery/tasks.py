from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from test_celery.celery import CONNECTION_POOLS

from .celery import app

@app.task
def add(x, y):
    return x + y

def send_results():
    # send results to rmq

    try:
        # task = data['task']
        task = 'test_celery.tasks.test'
        # broker = data['broker']
        broker = 'lizard'
        pool = CONNECTION_POOLS[broker]
        connection = pool.acquire()
        # logger.info('Sending task %s', task)
        app.send_task(task, args=['args'], connection=connection)
    except Exception as e:
        # logger.error(e)
        print(e)
    finally:
        connection.release()


@app.task
def test(*args):
    import time
    print("ARGS   ", args)
    time.sleep(10)
    print("Done testing")
