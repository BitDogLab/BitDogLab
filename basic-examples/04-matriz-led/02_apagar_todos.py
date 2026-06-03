from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(7), 25)

for i in range(25):
    np[i] = (0, 0, 0)
np.write()
