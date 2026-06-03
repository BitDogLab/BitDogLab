from machine import Pin, PWM
import time

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)
r.duty_u16(0)
g.duty_u16(0)

while True:
    b.duty_u16(65535)
    time.sleep_ms(150)
    b.duty_u16(0)
    time.sleep_ms(850)
