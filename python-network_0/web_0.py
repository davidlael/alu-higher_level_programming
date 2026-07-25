#!/usr/bin/python3
"""Simple web server for network tasks"""
from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/', methods=['GET'])
def route_0():
    return Response("Hello Holberton School!", status=200)

@app.route('/route_1', methods=['GET'])
def route_1():
    return Response("Route 2", status=200)

@app.route('/route_3', methods=['DELETE'])
def route_3():
    return Response("I'm a DELETE request", status=200)

@app.route('/route_4', methods=['GET', 'OPTIONS', 'HEAD', 'PUT'])
def route_4():
    return Response("Route 4", status=200)

@app.route('/route_5', methods=['GET'])
def route_5():
    uid = request.headers.get('X-HolbertonSchool-User-Id')
    if uid == '98':
        return Response("OK", status=200)
    return Response("NOP", status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
