#!/usr/bin/python

# sudo crontab -e
# @reboot python /home/pi/sendmail.py &

import smtplib
import time
from socket import *

RPI_MAIL = 'raspberrypi@gmail.com'
RPI_MAIL_PSW = '1234'
OWNER = 'owner@mail.com'

time.sleep(20) # wait to ensure network connection
# print "retrieving local ip address"	
s = socket(AF_INET, SOCK_DGRAM)
s.connect(("gmail.com", 80))
local_ip_addr = s.getsockname()[0]
s.close()


username = RPI_MAIL
password = RPI_MAIL_PSW
fromaddr = username
toaddrs  = OWNER
msg = "\r\n".join([
  "From: " + fromaddr,
  "To: " + toaddrs,
  "Subject: Raspberry Pi # - IP Address",
  "",
  local_ip_addr
  ])
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()