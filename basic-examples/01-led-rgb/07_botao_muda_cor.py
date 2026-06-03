from machine import Pin, PWM
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)
r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)
cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]
i = 0

def cor(c):
    r.duty_u16(c[0] * 257)
    g.duty_u16(c[1] * 257)
    b.duty_u16(c[2] * 257)

while True:
    if botao.value() == 0:
        i = (i + 1) % len(cores)
        cor(cores[i])
        time.sleep_ms(250)
