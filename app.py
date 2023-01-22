import time
import os
import socket
import redis

from flask import Flask

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