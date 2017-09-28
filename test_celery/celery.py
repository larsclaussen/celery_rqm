# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.rst.
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from celery import Celery
from kombu.connection import Connection
from test_celery import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)

CONNECTION_POOLS = {
    broker_name: Connection(broker_url).ChannelPool()
    for broker_name, broker_url
    in app.conf.BROKERS.items()
}

if __name__ == '__main__':
    app.start()


