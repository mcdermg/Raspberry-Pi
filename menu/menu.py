#Menu program by Gary Mc Dermott for easy access to frequent tasks version 1.0 26/04/2014

#for acces to command line
import os,time;
#subprocesses supposd to be better - review documentation
#import subprocess;

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.

loop = 1

#this variable holds the user's choice in the menu:

#def scpfile():
    #scp pi@192.168.1.15 filename /home/pi/Desktop

choice = 0

def remote():
    os.system('cd /home/pi/Desktop/remote')
    os.system('pwd')
    print'Remote not implimented in this script version'
    #os.system('python omxremote.py 2856960')
    print " "
    time.sleep(2) # delays for 2 seconds

def wakeonlan():
    os.system('wakeonlan 94:DE:80:AE:D6:B7')
    print " "
    time.sleep(2) # delays for 2 seconds

def systemp():
    os.system('cd systemp/')
    os.system('./temp.sh')
    print " "
    time.sleep(2) # delays for 2 seconds

def startWebcam():
    os.system('sudo service motion start')
    print " "
    time.sleep(2) # delays for 2 seconds

def stopWebcam():
    os.system('sudo service motion stop')
    print " "
    time.sleep(2) # delays for 2 seconds

def amysql():
    os.system('mysql -u pi -p')
    print " "

def editcron():
    os.system('sudo crontab -e')
    print " "

def update():
    os.system('sudo apt-get update')
    print " "

def checkip():
    os.system('ifconfig')
    print " "
    time.sleep(1) # delays for 1 second

def ssh():
    os.system('ssh pi@192.168.1.13')
    print " "


while loop == 1:
    #print what options you have
    print "What would you like to do today?"

    print "your options are:"
    print " "
    print " 1) Quit to command line"
    print " 2) Remote"
    print " 3) WakeonLan"
    print " 4) System Temperature"
    print " 5) Start Webcam"
    print " 6) Stop Webcam"
    print " 7) Aceess mysql"
    print " 8) Edit Cron Jobs"
    print " 9) Update"
    print "10) Check IP"
    print "11) SSH to other Pi"
    print " "

    choice = input("Choose your option: ")
    if choice == 1:
        loop = 0

    elif choice == 2:
        remote();
        
    elif choice == 3:
        wakeonlan();
        
    elif choice == 4:
        systemp();
        
    elif choice == 5:
        startWebcam();
        
    elif choice == 6:
        stopWebcam();

    elif choice == 7:
        amysql();

    elif choice == 8:
        editcron();

    elif choice == 9:
        update();

    elif choice == 10:
        checkip();

    elif choice == 11:
        ssh();

print " "
print "Goodbye"
print " "