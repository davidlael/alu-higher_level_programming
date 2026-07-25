#!/bin/bash
# Displays all HTTP methods accepted by the server
curl -sI "$1" | grep -i "^Allow:" | cut -d ' ' -f 2- | tr -d '\r'
