#!/bin/bash
# Displays the size of the HTTP response body in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
