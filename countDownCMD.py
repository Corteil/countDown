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




    # enter target time and date here

day=28
month=02
year=2015
hour=16
minutes=30
sec=0


targetTime = datetime.datetime(year, month, day, hour, minutes) # sets up target time
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
    time.sleep(1)

print ("\rwhat time is it? It's Party Time") # prints Party Time 


