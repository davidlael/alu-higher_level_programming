#!/bin/bash
# Sends a GET request to a URL with the X-HolbertonSchool-User-Id header set to 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
