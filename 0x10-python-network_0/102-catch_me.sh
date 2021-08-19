#!/bin/bash
#request to port 5000, output: You got me!
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
