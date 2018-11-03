import smtplib, time, random

now = time.time()
milliseconds = '%03d' % int((now - int(now)) * 1000)
current = (time.strftime("%d/%m/%Y  %H:%M:%S " + milliseconds))
#print current

random_number1 = random.randint(1, 500)
random_number2 = random.randint(500, 999)
#print random_number1
#print random_number2

def sendmail():
    to = 'mcdermott.gearoid@gmail.com'
    gmail_user = 'mcdermg@tcd.ie'
    gmail_pwd = 'Timeclock7636'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: '+str(random_number1)+'-'+milliseconds+'-'+str(random_number1)+'\n'
    #print header
    msg = header + '\n It is '+current+'\n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    #print 'done!'
    smtpserver.close()

sendmail()




