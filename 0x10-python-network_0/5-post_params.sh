#!/bin/bash
#Sends a POST request to the passed URL, and displays the body
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD"
