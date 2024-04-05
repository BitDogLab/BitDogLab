#Programa para acender os LEDs individualmente na cor desejada

# Importação das Bibliotecas: Importa as bibliotecas Pin e neopixel necessárias para controlar os LEDs.
from machine import Pin
import neopixel

# Configuração inicial

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
# A Raspberry Pi Pico está conectada à matriz de NeoPixels no pino GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Função para acender um LED específico com uma cor específica
def acender_led(indice, cor):
    """
    Acende um LED específico na matriz NeoPixel.

    :param indice: Índice do LED na matriz (0 a 24 para uma matriz 5x5)
    os índices identificam os 25 LEDs da matriz da seguinte forma:
            24 23 22 21 20
            15 16 17 18 19 
            14 13 12 11 10
            05 06 07 08 09
            04 03 02 01 00
    :param cor: Uma tupla (R, G, B) definindo a cor. Exemplo: (255, 0, 0) para vermelho. O valor de R, G e B deve ser de 0 a 255
    """
    # Verifica se o índice está dentro do intervalo permitido
    if 0 <= indice < NUM_LEDS:
        np[indice] = cor  # Define a cor do LED específico
        np.write()  # Atualiza a matriz de LEDs para aplicar a mudança
    else:
        print("Índice fora do intervalo. Por favor, escolha um índice de 0 a", NUM_LEDS - 1)

# Exemplo de uso da função
# Acendendo o LED com indice [variando de 0 a 24] que define a posição na cor definida pelo vetor: (R, G, B) [variando de 0 a 255 cada cor]
acender_led(12, (25, 25, 25))

# Aguarda 5 segundos antes de desligar o LED
time.sleep(5)

# Desligando todos os LEDs
for i in range(NUM_LEDS):
    np[i] = (0, 0, 0)
np.write()

# FIM