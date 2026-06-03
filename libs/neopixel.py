import machine
import neopixel
import time

# Configuração da matriz
NUM_COLS = 5
NUM_ROWS = 5
NUM_LEDS = NUM_COLS * NUM_ROWS
PIN_NUM = 7  # GPIO7

# Inicialização do Neopixel
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_LEDS)

def set_pixel(x, y, r, g, b):
    """
    Define a cor de um pixel específico na matriz.
    """
    index = (NUM_ROWS - 1 - y) * NUM_COLS + x
    np[index] = (r, g, b)

def update_display():
    """
    Atualiza a matriz.
    """
    np.write()

# Limpa a matriz
np.fill((0, 0, 0))
update_display()

# Acende os LEDs linha por linha, da esquerda para a direita, com 50% de brilho
for y in range(NUM_ROWS):
    for x in range(NUM_COLS):
        set_pixel(x, y, 0, 0, 127)  # Acende em azul com 50% de intensidade
        update_display()
        time.sleep(0.2)  # Pausa de 200ms antes de acender o próximo LED
