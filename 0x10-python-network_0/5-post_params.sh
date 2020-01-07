#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -d "email=hr%40holbertonschool%2Ecom&subject=I%20will%20always%20be%20here%20for%20PLD" -s -X POST "$1"
