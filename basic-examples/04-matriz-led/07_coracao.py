from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(7), 25)
coracao = [2, 6, 8, 10, 14, 15, 19, 21, 23]

for i in range(25):
    np[i] = (0, 0, 0)
for led in coracao:
    np[led] = (40, 0, 0)
np.write()
