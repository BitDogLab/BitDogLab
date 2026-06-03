import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(7), 25)

it=100# ontensidade do LED, pode variar de 1 a 255

# definir cores para os LEDs
BLU = (0, 0, 1*it)# BLUE
GRE = (0, 1*it, 0)# GREEN
RED = (1*it, 0, 0)
YEL = (1*it, 1*it, 0)# YELLOW
MAGE = (1*it, 0, 1*it)# MANGENTA
CYA = (0, 1*it, 1*it)# CYAN
WHI = (1*it, 1*it, 1*it)# WHIE
BLA = (0, 0, 0)# BLACK

happy = [
    [BLA, BLA, BLA, BLA, BLA],
    [BLA, BLU, BLA, BLU, BLA],
    [BLA, BLA, BLA, BLA, BLA],
    [BLU, BLA, BLA, BLA, BLU],
    [BLA, BLU, BLU, BLU, BLA]
]

sad = [
    [BLA, BLA, BLA, BLA, BLA],
    [BLA, BLU, BLA, BLU, BLA],
    [BLA, BLA, BLA, BLA, BLA],
    [BLA, BLU, BLU, BLU, BLA],
    [BLU, BLA, BLA, BLA, BLU]
]

eyeblink = [
    [BLA, BLA, BLA, BLA, BLA],
    [BLA, BLU, BLA, GRE, BLA],
    [BLA, BLA, BLA, BLA, BLA],
    [BLU, BLA, BLA, BLA, BLU],
    [BLA, BLU, BLU, BLU, BLA]
]


heart = [
    [BLA, RED, BLA, RED, BLA],
    [RED, RED, RED, RED, RED],
    [RED, RED, RED, RED, RED],
    [BLA, RED, RED, RED, BLA],
    [BLA, BLA, RED, BLA, BLA]
]

smallheart = [
    [BLA, BLA, BLA, BLA, BLA],
    [BLA, RED, BLA, RED, BLA],
    [BLA, RED, RED, RED, BLA],
    [BLA, BLA, RED, BLA, BLA],
    [BLA, BLA, BLA, BLA, BLA]
]

while True:

# definir a matriz 5x5
    led_matrix = heart

# inverter a matriz
    inverted_matrix = led_matrix[::-1]

# exibir a matriz invertida nos LEDs
    for i in range(5):
        for j in range(5):
            np[i*5+j] = inverted_matrix[i][j]

    np.write()

# aguardar 1 segundo
    time.sleep(1)

    led_matrix = smallheart

# inverter a matriz
    inverted_matrix = led_matrix[::-1]

# exibir a matriz invertida nos LEDs
    for i in range(5):
        for j in range(5):
            np[i*5+j] = inverted_matrix[i][j]

    np.write()

    time.sleep(1)

