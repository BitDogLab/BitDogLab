from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(7), 25)

for i in range(25):
    if i % 2 == 0:
        np[i] = (25, 0, 25)
    else:
        np[i] = (0, 25, 0)
np.write()
