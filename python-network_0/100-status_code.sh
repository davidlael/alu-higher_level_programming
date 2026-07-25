#!/bin/bash
# Displays only the status code of the HTTP response
curl -s -o /dev/null -w "%{http_code}" "$1"
