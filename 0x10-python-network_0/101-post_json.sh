#!/bin/bash
#sends JSON POST request to URL passed as the first argument, displays body
curl -sX POST "$1" -H 'Content-Type: application/json' -d "@$2"
