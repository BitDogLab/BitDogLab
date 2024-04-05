from machine import Pin
import neopixel

# Configurações iniciais
NUM_LEDS = 25  # Número total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Mapeamento da matriz de LEDs com a origem no canto inferior esquerdo
LED_MATRIX = [
    [24, 23, 22, 21, 20],    
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]


'''LED_MATRIX = [
    [0, 1, 2, 3, 4],
    [9, 8, 7, 6, 5],
    [10, 11, 12, 13, 14],
    [19, 18, 17, 16, 15],
    [20, 21, 22, 23, 24]
]'''

# Função que define o controle de acendimento da posição e da dor de cada LED da Matriz do BitDogLab
def leds(x, y, r, g, b):
    if 0 <= x <= 4 and 0 <= y <= 4:
        led_index = LED_MATRIX[4-y][x]
        np[led_index] = (r, g, b)
        np.write()
    else:
        print("Coordenadas inválidas.")

# Exemplo de uso
leds(0, 0, 0, 0, 50)  # Acende o LED no canto inferior esquerdo em vermelho
