#!/bin/bash
# Sends a GET request with X-HolbertonSchool-User-Id header set to 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
