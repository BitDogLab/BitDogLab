from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(7), 25)

while True:
    for pos in range(25):
        for i in range(25):
            np[i] = (0, 0, 0)
        np[pos] = (0, 30, 0)
        np.write()
        time.sleep_ms(120)
