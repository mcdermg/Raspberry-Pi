#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb, time
from random import randint

def db():
	a = (randint(0,9))
	b = (randint(0,9))
	c = (randint(0,9))
	d = (randint(0,9))

	now = time.strftime('%Y-%m-%d %H:%M:%S')

	DeviceID = 1

	#use this to get all into temp table
	readings = (a,b,c,d,now,DeviceID)


	#connect with database
	con = MySQLdb.connect('hostname', 'user', 'password', 'dn_name');
	#con = MySQLdb.connect('deviot.cvxdamlpotcj.eu-west-1.rds.amazonaws.com', 'mcdermg', '<password>', 'iot_db');

	with con:
		cur = con.cursor()
		cur.execute("""INSERT INTO weather (DigTemp,DH11Humdity,DH11Temp,DH11HeatIndex,ReadingTime,DeviceID) VALUES (%s,%s,%s,%s,%s,%s) """, readings)
		print 'Succesfully Inserted the values to DB'
db()
