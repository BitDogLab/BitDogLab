from machine import Pin, PWM
import time

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)
g.duty_u16(0)
b.duty_u16(0)

while True:
    for _ in range(3):
        r.duty_u16(65535)
        time.sleep_ms(90)
        r.duty_u16(0)
        time.sleep_ms(90)
    time.sleep(1)
