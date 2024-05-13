from machine import Pin
from utime import time, localtime, sleep
from select import select
from sys import stdin

timeDelta = 0
year,month,day,hour,minute,second,wday,yday = 0,0,0,0,0,0,0,0

def timeNow(timeDelta):
    return (time() + timeDelta)

def checkTimeSyncUSB(timeDelta):
    ch, buffer = '',''
    while stdin in select([stdin], [], [], 0)[0]:
        ch = stdin.read(1)
        buffer = buffer+ch
    if buffer:
        for i in range(len(buffer)):
            if buffer[i] == 'T':
                break
        buffer = buffer[i:]
        if buffer[:1] == 'T':
            if buffer[1:11].isdigit():
                syncTime = int(buffer[1:11])
                if syncTime > 1609459201: # Thursday 1st January 2021 00:00:01
                    timeDelta = syncTime - int(time())
                else:
                    syncTime = 0
    return timeDelta

led_onboard = Pin(25, Pin.OUT)
lastTime = timeNow(timeDelta)

while True:
    timeDelta = checkTimeSyncUSB(timeDelta)        
    correctedRTC = timeNow(timeDelta)
    
    #
    # every second do the following ...
    #
    if correctedRTC != lastTime:
        lastTime=correctedRTC

        if timeDelta == 0:
            for i in range(5):
                led_onboard.toggle()
                sleep(0.03)
            led_onboard.value(0)

        (year,month,day,hour,minute,second,wday,yday)=localtime(correctedRTC)
        correctedRTCstring="%d-%02d-%02dT%02d:%02d:%02d" % (year,month,day,hour,minute,second)

        #
        # every 5 seconds do the following ...
        #
        if (second % 5) == 0:
            print('CorrectedRTC Unix epoch time     :',end='');print(correctedRTC)
            print('CorrectedRTC localtime list      :',end='');print(localtime(correctedRTC))
            print('CorrectedRTC composite date/time :',end='');print(correctedRTCstring)
            print()