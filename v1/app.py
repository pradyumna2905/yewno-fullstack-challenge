#!flask/bin/python
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

hw_json = [
            {
                "message": "hello, world"
            }
            ]



@app.route('/hello-world/logs', methods=['GET'])
def get_tasks():
    return jsonify({'success': hw_json})


@app.route('/v1/logs', methods=['GET'])
def get_tasks1():
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
