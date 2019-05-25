#!/usr/bin/python

#Temperature reading programme by Gary Mc Dermott 20190520

#sys library for exiting if no reading
import sys
#Adafruit library for getting sensor readings
import Adafruit_DHT
#JSON library for sending data
import json
#Time library for timestamp
import time
import datetime
#urlib library for sending post to endpoint
import urllib2
#decimal library for lamda float issue
from decimal import Decimal
#Socket ibrary for getting hostname
import socket

#TODO REMOVE - for testing creting random ids
import random


#Not required now but may beed to adapt for Python 3.
#TODO Will need to add toggle for 2 functions one is pyhton 2 other is 3 call depending on toggle
#try:
#    # For Python 3.0 and later
#    from urllib.request import urlopen
#except ImportError:
#    # Fall back to Python 2's urllib2
#    from urllib2 import urlopen

#Declare the pins that the sensor is attached to on the Pi
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

#get hostname
host = socket.gethostname()

#Handle if there is an issue getting readings
if humidity is not None and temperature is not None:
    #declare timestamp & make it str for dynamo
    timestamp = str(datetime.datetime.now())
    #make temp and humidity ok for DynamoDB
    h = str(Decimal(humidity))
    t = str(Decimal(temperature))

    #TODO remove for testing
    cid = str(Decimal(random.randint(1, 50)))

    #JSON data to be sent
    data = {
        "CUSTOMER_ID":cid,
        "tenant":host,
        "home":"Amenabar",
        "room":"Study",
        "timstamp":timestamp,
        "temperature":t,
        "humidity":h
    }

    #set the endpoint
    req = urllib2.Request('https://oen28a79ij.execute-api.eu-west-1.amazonaws.com/dev/monitoring')
    #Add header to explicitly stat json for POST
    req.add_header('Content-Type', 'application/json')
    #req.add_header('x-api-key', 'your-key')

    response = urllib2.urlopen(req, json.dumps(data))
    #for debugging #TODO remove
else:
    #Handle no readings
    #TODO add this to logfile with timestamp
    print('Failed to get reading. Try again!')
    sys.exit(1)
