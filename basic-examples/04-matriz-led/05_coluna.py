from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(7), 25)
colunas = [[24, 15, 14, 5, 4], [23, 16, 13, 6, 3], [22, 17, 12, 7, 2], [21, 18, 11, 8, 1], [20, 19, 10, 9, 0]]

while True:
    for coluna in colunas:
        for i in range(25):
            np[i] = (0, 0, 0)
        for led in coluna:
            np[led] = (0, 0, 30)
        np.write()
        time.sleep_ms(350)
