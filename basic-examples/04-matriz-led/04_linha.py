from machine import Pin
import neopixel
import time

np = neopixel.NeoPixel(Pin(7), 25)

# Ordem fisica dos LEDs na matriz 5x5 da BitDogLab.
linhas = [[24, 23, 22, 21, 20], [15, 16, 17, 18, 19], [14, 13, 12, 11, 10], [5, 6, 7, 8, 9], [4, 3, 2, 1, 0]]

while True:
    for linha in linhas:
        for i in range(25):
            np[i] = (0, 0, 0)
        for led in linha:
            np[led] = (30, 0, 0)
        np.write()
        time.sleep_ms(350)
