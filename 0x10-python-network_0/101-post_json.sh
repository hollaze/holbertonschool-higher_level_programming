#!/bin/bash
#sends JSON POST request to URL passed as the first argument, displays body
curl -sX POST "$1" -d "$2"
