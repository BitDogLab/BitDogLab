from machine import Pin
import neopixel

botao = Pin(5, Pin.IN, Pin.PULL_UP)
np = neopixel.NeoPixel(Pin(7), 25)

while True:
    cor = (30, 30, 0) if botao.value() == 0 else (0, 0, 0)
    for i in range(25):
        np[i] = cor
    np.write()
