from machine import Pin, PWM
import time

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)
g.duty_u16(0)
b.duty_u16(0)

while True:
    for valor in range(0, 256, 5):
        r.duty_u16(valor * 257)
        time.sleep_ms(20)
    for valor in range(255, -1, -5):
        r.duty_u16(valor * 257)
        time.sleep_ms(20)
