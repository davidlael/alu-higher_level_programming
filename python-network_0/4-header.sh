#!/bin/bash
# Sends a GET request to a URL with the X-HolbertonSchool-User-Id header set to 2211
curl -s -H "X-HolbertonSchool-User-Id: 2211" "$1"
