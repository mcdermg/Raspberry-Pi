#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial, MySQLdb, time

ser = serial.Serial('/dev/ttyACM0',9600).flush()

def db():
	ser = serial.Serial('/dev/ttyACM0',9600)
	var = ser.readline()
	#print var
	#read data from arduino
	data = var
	pieces = data.split(" , ")
	#print (pieces[0],pieces[1],pieces[2],pieces[3])
	a = pieces[0]
	b = pieces[1]
	c = pieces[2]
	d = pieces[3]

	now = time.strftime('%Y-%m-%d %H:%M:%S')
	print now
	#ALTER TABLE Writers ADD ReadingTime DATETIME;
	values = (a,now)
	#connect with database
	con = MySQLdb.connect('localhost', 'username', 'password', 'db_name');

	with con:
		cur = con.cursor()
		cur.execute("""INSERT INTO Writers(Name,ReadingTime) VALUES (%s,%s)""", values)
		#cur.execute("""INSERT INTO Writers(Name) VALUES (%s)""", b)
		#cur.execute("""INSERT INTO Writers(Name) VALUES (%s)""", c)
		#cur.execute("""INSERT INTO Writers(Name) VALUES (%s)""", d)
		print 'Succesfully Inserted the values to DB'
db()
