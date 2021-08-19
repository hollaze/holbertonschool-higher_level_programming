#!/bin/bash
#Sends request to URL passed as argument, displays only the status code
curl -so /dev/null -w "%{http_code}" "$1"
