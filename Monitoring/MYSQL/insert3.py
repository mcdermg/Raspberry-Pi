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
	#this can use a for loop for modular program if more data is needed
	a = pieces[0]
	b = pieces[1]
	c = pieces[2]
	d = pieces[3]

	now = time.strftime('%Y-%m-%d %H:%M:%S')
	
	DeviceID = 1
	RoomID = 1

	#use this to get all into temp table
	readings = (now,DeviceID,RoomID,a,b,c,d)
	

	#connect with database
	con = MySQLdb.connect('ec2-54-229-40-6.eu-west-1.compute.amazonaws.com', 'pi', 'password5252', 'shrewsbury');

	with con:
		cur = con.cursor()
		cur.execute("""INSERT INTO weather (ReadingTime,DeviceID,RoomID,DigTemp,DH11Humdity,DH11Temp,DH11HeatIndex) VALUES (%s,%s,%s,%s,%s,%s) """, readings)
		print 'Succesfully Inserted the values to DB'
db()
