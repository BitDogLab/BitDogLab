import time
from machine import Pin
import neopixel

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# 
LED = {
    0: 24, 1: 23, 2: 22, 3: 21, 4: 20,
    5: 15, 6: 16, 7: 17, 8: 18, 9: 19,
    10: 14, 11: 13, 12: 12, 13: 11, 14: 10,
    15: 5, 16: 6, 17: 7, 18: 8, 19: 9,
    20: 4, 21: 3, 22: 2, 23: 1, 24: 0
}

# Função para acender cada LED em sequência de 0 a 24
def cycle_matrix():
    for i in range(NUM_LEDS):
        np[LED[i]] = (255, 255, 255)  # Define o LED como branco
        np.write()  # Atualiza o estado da matriz
        time.sleep(1)  # Mantém o LED aceso por 1 segundo
        np[LED[i]] = (0, 0, 0)  # Desliga o LED
        np.write()  # Atualiza o estado da matriz

# Executa a função
cycle_matrix()

