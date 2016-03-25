#!flask/bin/python
from flask import Flask, jsonify, request, render_template
import time
import redis

r = redis.Redis('localhost')


app = Flask(__name__)

hw_json = [
            {
                "message": "hello, world"
            }
            ]

@app.route('/', methods=['GET'])
def home():
    return "hello, world"


@app.route('/hello-world/logs', methods=['GET'])

def log():
    ipAddress = request.remote_addr
    timestamp = str(int(time.time()))

    if r.exists('ip_address') and r.exists('timestamp'):
        r.append('ip_address', ipAddress)
        r.append('ip_address', ',')

        r.append('timestamp', timestamp)
        r.append('timestamp', ',')

    else:
        r.set('ip_address', ipAddress)
        r.append('ip_address', ',')

        r.set('timestamp', timestamp)
        r.append('timestamp', ',')



    return jsonify({'success': hw_json})


@app.route('/v1/logs', methods=['GET'])
def log1():
    ip = []
    ip.append(r.mget('ip_address'))
    print ip

    a = ip[0][0]

    ip_a = a.split(',')

    ts = []
    ts.append(r.mget('timestamp'))

    b = ts[0][0]

    ts_a = b.split(',')

    n = [[x, y] for x, y in zip(ip_a, ts_a)]
    l = len(n)

    logs = [
            {
                "logset": [
                            {
                                "endpoint": "hello-world"
                            },
                            {
                                "logs": [
                                            {
                                            "ip": n[g][0],
                                            "timestamp": n[g][1]
                                            } for g in range (l-1)]
                            }
                ]
            }
    ]

    return (jsonify({'success': logs}))


if __name__ == '__main__':
    app.run(debug="True")
