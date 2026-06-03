from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(7), 25)

while True:
    for qtd in range(26):
        for i in range(25):
            np[i] = (0, 30, 0) if i < qtd else (0, 0, 0)
        np.write()
        time.sleep_ms(150)
