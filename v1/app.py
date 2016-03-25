#!flask/bin/python
from flask import Flask, jsonify, request
import time
import redis

app = Flask(__name__)
r = redis.Redis('localhost')

def insertToDb(ipAddress, timestamp):
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


@app.route('/<path:key>', methods=['GET'])
def log(key):
    if key == 'v1/hello-world/logs':
        ipAddress = request.remote_addr
        timestamp = str(int(time.time()))

        insertToDb(ipAddress, timestamp)
        hw_json = [
                        {
                            "message": "hello, world"
                        }
                    ]




        return jsonify({'success': hw_json})

    if key == 'v1/logs':

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
                                                    } for g in range (l-1)
                                        ]
                                    }
                        ]
                    }
            ]

            return (jsonify({'success': logs}))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
