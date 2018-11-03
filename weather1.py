#!/usr/bin/python
#import serial
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost", "root", "Caltek11", "mcdermg_db")
c = db.cursor()

# Insert data
try:
    #curs.execute ("INSERT INTO weather (`wdate`, `wtime`, `Humidity`, `Temperature`, `HeatIndex`) VALUES ( now(), now(), 1, 2, 3 );")
    curs.execute ("INSERT INTO weather (`wdate`, `wtime`, `Humidity`, `Temperature`, `HeatIndex`) VALUES ( now(), now(), 4, 5, 6 );")
    curs.execute ("INSERT INTO weather (`wdate`, `wtime`, `Humidity`, `Temperature`, `HeatIndex`) VALUES ( now(), now(), 7, 8, 9 );")	

    db.commit()
    print "Data committed"

except:
    print "Error: the database is being rolled back"
    db.rollback()

#ser = serial.Serial('/dev/ttyACM0',9600)
#while 1 :
	#print(ser.readline())



# MySQL input
#c = conn.cursor()

#c.execute ("INSERT INTO weather (`wdate`, `wtime`, `Humidity`, `Temperature`, `HeatIndex`) VALUES ( now(), now(), 1, 2, 3 );")
#db.commit()
#print('data inputted to db')