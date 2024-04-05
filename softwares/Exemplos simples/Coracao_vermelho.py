from machine import Pin
import neopixel
import time

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Definindo a matriz de LEDs para formar um coração
coracao = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
 
]

# Função para acender a matriz de LEDs com base no padrão do coração
def acender_coracao():
    for i in range(5):
        for j in range(5):
            index = i * 5 + j
            if coracao[i][j] == 1:
                np[index] = (20, 0, 0)  # Vermelho para formar o coração
            else:
                np[index] = (0, 0, 0)  # Desliga o LED

    np.write()

# Acender o coração por alguns segundos
acender_coracao()
time.sleep(5)

# Desligar todos os LEDs
for i in range(NUM_LEDS):
    np[i] = (0, 0, 0)

np.write()