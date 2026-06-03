from machine import Pin, PWM
import time

# LED RGB da BitDogLab: vermelho 13, verde 11, azul 12.
r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

def cor(vr, vg, vb):
    # Recebe valores de 0 a 255 e converte para o PWM do MicroPython.
    r.duty_u16(vr * 257)
    g.duty_u16(vg * 257)
    b.duty_u16(vb * 257)

while True:
    cor(255, 0, 0)
    time.sleep(0.5)
    cor(0, 0, 0)
    time.sleep(0.5)
