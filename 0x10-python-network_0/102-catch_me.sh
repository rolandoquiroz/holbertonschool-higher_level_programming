#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -s -L -d "user_id=98" -H "Origin: HolbertonSchool" -X PUT 0:5000/catch_me
