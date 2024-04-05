from machine import Pin
import neopixel
import time

# Configuração inicial
NUM_LEDS = 25  # Número total de LEDs na matriz 5x5
PIN = 7  # O pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

x = 25

# Cores
WHITE = (25, 25, 25)
BLUE = (0, 0, 25)
RED = ( 25, 0 , 0)
OFF = (0, 0, 0)

def cascade_effect(wait):
    # Cria um efeito de cascata de luzes brancas e azuis
    for i in range(NUM_LEDS):
        # Define a cor de cada LED
        if i % 2 == 0:  # Se for par, branco
            np[i] = WHITE
        else:  # Se for ímpar, azul
            np[i] = BLUE
        np.write()  # Atualiza o estado dos LEDs
        time.sleep(wait)  # Espera um pouco antes de mudar o próximo LED

    time.sleep(1)  # Espera um segundo no final do efeito

    for i in range(NUM_LEDS):
        # Define a cor de cada LED
        if i % 2 == 0:  # Se for par, branco
            np[i] = OFF
        else:  # Se for ímpar, azul
            np[i] = RED
        np.write()  # Atualiza o estado dos LEDs
        time.sleep(wait)  # Espera um pouco antes de mudar o próximo LED

    time.sleep(1)  # Espera um segundo no final do efeito

    
    
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)  # Desliga todos os LEDs
    np.write()

while True:
    cascade_effect(0.1)  # Chama a função de efeito com um intervalo de 0.1 segundos
    x = x-5
    WHITE = (x, x, x)
    BLUE = (0, 0, 25)
    RED = (25, 0 , 0)
    OFF = (25-x, 25-x, 25-x)
    if x < 1:
        x = 25