from machine import Pin
import utime
 
red = Pin(11, Pin.OUT)
green = Pin(12, Pin.OUT)
blue = Pin(13, Pin.OUT)
 
while True:
    red.value(1)
    green.value(1)
    blue.value(1)
    utime.sleep(1)
 
    red.value(0)
    green.value(1)
    blue.value(1)
    utime.sleep(1)
 
    red.value(1)
    green.value(0)
    blue.value(1)    
    utime.sleep(1)
 
    red.value(1)
    green.value(1)
    blue.value(0)
    utime.sleep(1)