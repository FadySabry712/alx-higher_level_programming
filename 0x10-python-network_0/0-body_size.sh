#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, display body
curl -s "$1" | wc -c
