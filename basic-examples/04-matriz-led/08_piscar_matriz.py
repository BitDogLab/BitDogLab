from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(7), 25)

while True:
    for i in range(25):
        np[i] = (0, 20, 20)
    np.write()
    time.sleep_ms(400)
    for i in range(25):
        np[i] = (0, 0, 0)
    np.write()
    time.sleep_ms(400)
