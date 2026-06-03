from machine import Pin
import time

a = Pin(5, Pin.IN, Pin.PULL_UP)
b = Pin(6, Pin.IN, Pin.PULL_UP)

while True:
    if a.value() == 0:
        print("A")
    if b.value() == 0:
        print("B")
    time.sleep_ms(150)
