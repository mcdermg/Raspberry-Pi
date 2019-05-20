#!/usr/bin/python

import sys
import Adafruit_DHT
import json
import time

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 2)
if humidity is not None and temperature is not None:
    timestamp = int(time.time())

    data = {
        "id":None,
        "tenant":"test",
        "home":"main",
        "room":"living room",
        "timstamp":timestamp,
        "temperature":temperature,
        "humidity":humidity
    }

    req = urllib2.Request('https://api-gw-url.aws-region.amazonaws.com/production/ClimateMonitor')
    req.add_header('Content-Type', 'application/json')
    req.add_header('x-api-key', 'your-key')

    response = urllib2.urlopen(req, json.dumps(data))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
