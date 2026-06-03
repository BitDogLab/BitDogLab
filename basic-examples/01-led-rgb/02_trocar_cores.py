from machine import Pin, PWM
import time

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

def cor(vr, vg, vb):
    r.duty_u16(vr * 257)
    g.duty_u16(vg * 257)
    b.duty_u16(vb * 257)

cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

while True:
    for c in cores:
        cor(c[0], c[1], c[2])
        time.sleep(0.7)
