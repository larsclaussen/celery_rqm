import os
import ast


def env(key, default=None, required=False):
    """
    Retrieves environment variables and returns Python natives. The (optional)
    default will be returned if the environment variable does not exist.
    """
    try:
        value = os.environ[key]
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value
    except KeyError:
        if default or not required:
            return default
        raise Exception(
            "Missing required environment variable '%s'" % key)


# Celery
BROKER_URL = 'amqp://guest:guest@{}:{}//'.format(
    env('RABBIT_MQ_HOST', 'localhost'),
    env('RABBIT_MQ_PORT', 5672)
)
CELERY_RESULT_BACKEND = 'amqp://guest:guest@{}:{}//'.format(
    env('RABBIT_MQ_HOST', 'localhost'),
    env('RABBIT_MQ_PORT', 5672)
)
CELERY_IMPORTS = ('test_celery.tasks',)

BROKERS = {
     '3di': 'redis://redis:6379/0',
     'lizard': BROKER_URL,
}
# # # List of modules to import when the Celery worker starts.
# # imports = ('flow.results',)

CELERY_ROUTES = {
    'test_celery.tasks.test': {'queue': 'test_queue'},
}
