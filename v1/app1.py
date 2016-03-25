#!flask/bin/python
from flask import Flask, jsonify, request
import time

app = Flask(__name__)


# @app.route('/hello-world/logs', methods=['GET'])
# def log():
#
#     return jsonify({'success': hw_json})


@app.route('/<key>', methods=['GET'])
def log1(key):
    if key == 'hello-world/logs':
        hw_json = [
                    {
                        "message": "hello, world"
                    }
                    ]
        return jsonify({'success': hw_json})

    if key == 'v1/logs':
        ipAddress = request.remote_addr
        timestamp = str(int(time.time()))

        logs = [
                {
                    "logset": [
                                {
                                    "endpoint": "hello-world"
                                },
                                {
                                    "logs": [
                                                {
                                                "ip": ipAddress,
                                                "timestamp": timestamp
                                                }
                                    ]
                                }
                    ]
                }
        ]

        return jsonify({'success': logs})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
