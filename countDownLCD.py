#
#count down timer 
#
# by Brian Corteil aka on Twitter @CannonFodder
#
# free to use
#

import sys
import os,time, datetime
from datetime import timedelta
import serial

# Specify your serial port path (/dev/ttyAMA0 is default for Raspberry Pi)
serialport = serial.Serial('/dev/ttyAMA0',9600,serial.EIGHTBITS,serial.PARITY_NONE,
    serial.STOPBITS_ONE,timeout=5,rtscts = False)


    # enter target time and date here

day=28
month=02
year=2015
hour=16
minutes=30
sec=0

# functions

def LCDclear():
    
    clearscreen = [chr(254), chr(88)]
    for i in clearscreen:
        serialport.write(i)
    

def LCDmessage(message):
    serialport.write(message)


# main

targetTime = datetime.datetime(year, month, day, hour, minutes, sec) # sets up target time
timeNow =datetime.datetime.now()

while timeNow <= targetTime:

    timeNow =datetime.datetime.now() # the time now!
    timeNow =datetime.datetime.now()
    remainingTime=(targetTime-timeNow)
    days = remainingTime.days
    secs = remainingTime.seconds
    hrs, secs = divmod(secs, 3600)
    mins, secs = divmod(secs, 60)
    
    sys.stdout.write("\r%dd %dh %dm %ds to the Raspberry Pi Birthday Bash!    " % (days, hrs, mins, secs))
    sys.stdout.flush()
    LCDclear()
    LCDmessage("How long to go?\r%dd %dh %dm %ds" % (days, hrs, mins, secs))
    time.sleep(1)

print ("\r\nwhat time is it? It's Party Time") # prints Party Time
LCDclear() 
LCDmessage("\r\nwhat time is it?\nIt's Party Time")

