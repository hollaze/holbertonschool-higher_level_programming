#!/bin/bash
#request to port 5000, output: You got me!
curl -so 0.0.0.0:5000/catch_me -w "You got me!"
