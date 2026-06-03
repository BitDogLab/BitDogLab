from machine import Pin, PWM

a = Pin(5, Pin.IN, Pin.PULL_UP) #botao A
b = Pin(6, Pin.IN, Pin.PULL_UP) #botao B
r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)

while True:
    r.duty_u16(65535 if a.value() == 0 else 0)
    g.duty_u16(65535 if b.value() == 0 else 0)
