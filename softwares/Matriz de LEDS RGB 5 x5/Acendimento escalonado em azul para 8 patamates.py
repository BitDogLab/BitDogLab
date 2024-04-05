import time
import neopixel
import machine

# Configuração inicial
n = 25
pin = machine.Pin(7, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, n)

# Definição das sequências de acendimento
patamares = [
    [2],
    [1, 2, 3],
    [7, 1, 2, 3],
    [12, 6, 7, 8, 0, 1, 2, 3, 4],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14, 15, 19],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14, 15, 19, 20, 21, 23, 24]
]

def acender_leds(patamar, color):
    for i in patamar:
        np[i] = color
    np.write()

# Acendendo em azul
for patamar in patamares:
    acender_leds(patamar, (0, 0, 55))
    time.sleep(1)

# Acendendo em vermelho
for patamar in patamares:
    acender_leds(patamar, (55, 0, 0))
    time.sleep(1)


