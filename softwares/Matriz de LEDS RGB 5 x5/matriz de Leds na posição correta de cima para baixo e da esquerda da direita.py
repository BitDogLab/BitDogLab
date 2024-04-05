import time
from machine import Pin
import neopixel

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Definindo a matriz de LEDs
LED_MATRIX = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

# Função para acender cada LED em sequência de (0,0) a (4,4)
def cycle_matrix():
    for row in range(5):
        for col in range(5):
            led_index = LED_MATRIX[row][col]
            np[led_index] = (255, 255, 255)  # Define o LED como branco
            np.write()  # Atualiza o estado da matriz
            time.sleep(1)  # Mantém o LED aceso por 1 segundo
            np[led_index] = (0, 0, 0)  # Desliga o LED
            np.write()  # Atualiza o estado da matriz

# Executa a função
cycle_matrix()
