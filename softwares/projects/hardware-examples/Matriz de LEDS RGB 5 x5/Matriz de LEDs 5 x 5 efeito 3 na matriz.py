import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(7), 25)

# definir cores para os LEDs
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (80, 0, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# definir a matriz 5x5
led_matrix = [
    [BLACK, BLACK, 	BLACK, 	BLACK, 	BLACK],
    [BLUE, 	BLACK, 	BLUE, 	BLUE, 	BLACK],
    [BLACK, BLACK, 	BLACK, 	BLACK, 	BLACK],
    [BLACK, BLACK, 	BLACK, 	BLACK, 	BLACK],
    [BLUE, 	BLUE, 	BLUE, 	BLUE, 	BLUE]
]

# inverter a matriz
inverted_matrix = led_matrix[::-1]

# exibir a matriz invertida nos LEDs
for i in range(5):
    for j in range(5):
        np[i*5+j] = inverted_matrix[i][j]

np.write()

# aguardar 1 segundo
time.sleep(1)
