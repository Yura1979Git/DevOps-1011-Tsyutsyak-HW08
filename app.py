import sentry_sdk
import time
import os
import socket
import redis
from sentry_sdk.integrations.flask import FlaskIntegration
from flask import Flask

sentry_sdk.init(
    dsn="https://6b1015457fed4edfb2babaee7758f2db@o4504677437865984.ingest.sentry.io/4504677439242240",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)
cache = redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    visits = get_hit_count()
    html =  '<h3>Hello World!</h3>' \
            '<b>Hostname:</b> {hostname}<br/>' \
            '<b>IP:</b> {local_ip}<br/>' \
            '<b>Visits:</b> {visits}<br/>' \
            '<br/>'
    return html.format(hostname=hostname,local_ip=local_ip, visits=visits)

@app.route('/health')
def health():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    html =  '<h3>Hello World!</h3>' \
            '<b>Hostname:</b> {hostname}<br/>' \
            '<b>IP:</b> {local_ip}<br/>' \
            '<br/>'
    return html.format(hostname=hostname,local_ip=local_ip)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0