#funcionando
import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(7), 25)

# definir cores para os LEDs
#RED = (255, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
#BLUE = (0, 0, 255)
BLUE = (80, 0, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(1)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = RED
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(1)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(5)


# apagar todos os LEDs
for i in range(len(np)):
    np[i] = BLACK
np.write()

