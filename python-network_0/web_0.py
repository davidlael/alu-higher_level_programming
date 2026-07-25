#!/usr/bin/python3
"""Simple web server for network tasks"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/route_4', methods=['GET'])
def route_4():
    user_id = request.headers.get('X-HolbertonSchool-User-Id')
    if user_id == '98':
        return 'OK'
    return 'NOP'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
