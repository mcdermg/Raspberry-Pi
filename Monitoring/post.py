#!/usr/bin/python
import json
import urllib2

data = {
    "CUSTOMER_ID":"3",
    "CUSTOMER_NAME":"Python",
    "CUSTOMER_LOCATION":"Post scritp"
}

req = urllib2.Request('https://9thz0k5588.execute-api.eu-west-1.amazonaws.com/Development/customer')
req.add_header('Content-Type', 'application/json')
req.add_header('x-api-key', 'your-key')

response = urllib2.urlopen(req, json.dumps(data))
