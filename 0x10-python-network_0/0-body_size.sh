#!/bin/bash
#takes URL, sends request to URL, displays size of body
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2 
