#Programa exemplo para apagar odos os LEDs da matriz
from machine import Pin
import neopixel

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

def apagar_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)  # Definindo a cor do LED para preto (apagado)
    np.write()  # Atualizando a matriz de LEDs para aplicar as alterações

# Chamando a função para apagar os LEDs
apagar_leds()

#FIM
