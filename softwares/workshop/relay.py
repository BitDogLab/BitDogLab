from machine import Pin
import utime

while True:
    gp16 = Pin(16, Pin.OUT)
    gp16.toggle()
    utime.sleep(5)