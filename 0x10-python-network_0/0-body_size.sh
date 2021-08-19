#!/usr/bin/env bash
#takes URL, sends request to URL, displays size of body of response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2 
