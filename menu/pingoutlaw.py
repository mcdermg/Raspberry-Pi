#!/usr/bin/python


import os, time

print('before')

f = open("/home/pi/Desktop/timeuplog/pingoutlaw.txt","a")
f.write("\n")
f.write(time.ctime())
f.close()

os.system("ping 192.168.1.10")

print('after')
