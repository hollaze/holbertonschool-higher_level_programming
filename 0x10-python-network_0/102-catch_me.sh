#!/bin/bash
#request to port 5000, output: You got me!
curl -s 0.0.0.0:5000/catch_me -o /dev/null -w "You got me!"
