from machine import Pin, PWM
import time

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

def cor(vr, vg, vb):
    r.duty_u16(vr * 257)
    g.duty_u16(vg * 257)
    b.duty_u16(vb * 257)

while True:
    cor(255, 0, 0)
    time.sleep(2)
    cor(255, 180, 0)
    time.sleep(1)
    cor(0, 255, 0)
    time.sleep(2)
