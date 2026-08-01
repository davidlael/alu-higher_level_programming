#!/bin/bash
# Sends a GET request to a URL with the X-HolbertonSchool-User-Id header set to your ID
curl -s -H "X-HolbertonSchool-User-Id: YOUR_REAL_ID" "$1"
