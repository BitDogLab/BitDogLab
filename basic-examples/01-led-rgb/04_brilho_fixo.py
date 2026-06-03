from machine import Pin, PWM
import time

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

while True:
    r.duty_u16(12000)
    g.duty_u16(0)
    b.duty_u16(12000)
    time.sleep(1)
