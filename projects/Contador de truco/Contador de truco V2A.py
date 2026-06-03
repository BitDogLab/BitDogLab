import machine, neopixel
import time
import numpy as np

np = neopixel.NeoPixel(machine.Pin(7), 25)

it = 100 # intensidade do LED, pode variar de 1 a 255

# define cores para os LEDs
B = (0, 0, 1*it) # BLUE
G = (0, 1*it, 0) # GREEN
R = (1*it, 0, 0) # RED
Y = (1*it, 1*it, 0) # YELLOW
M = (1*it, 0, 1*it) # MAGENTA
C = (0, 1*it, 1*it) # CYAN
W = (1*it, 1*it, 1*it) # WHITE
O = (0, 0, 0) # BLACK

B0 = [
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O]
]

B1 = [
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, R]
]

B2 = [
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, R],
    [O, O, O, O, R]
]

B3 = [
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R]
]

B4 = [
    [O, O, O, O, O],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R]
]

B5 = [
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R]
]

B6 = [
    [O, O, O, R, R],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R]
]

B7 = [
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, O, R],
    [O, O, O, O, R],
    [O, O, O, O, R]
]


B8 = [
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, O, R],
    [O, O, O, O, R]
]

B9 = [
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, O, R]
]

B10 = [
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R]
]

B11 = [
    [O, O, R, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R]
]

B12 = [
    [O, O, R, R, R],
    [O, O, R, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R]
]

# Define um dicionário que mapeia as coordenadas da matriz para um índice do LED
matrix_to_led_index = {
    (0, 0): 0, (0, 1): 1, (0, 2): 2, (0, 3): 3, (0, 4): 4,
    (1, 0): 9, (1, 1): 8, (1, 2): 7, (1, 3): 6, (1, 4): 5,
    (2, 0): 10, (2, 1): 11, (2, 2): 12, (2, 3): 13, (2, 4): 14,
    (3, 0): 19, (3, 1): 18, (3, 2): 17, (3, 3): 16, (3, 4): 15,
    (4, 0): 20, (4, 1): 21, (4, 2): 22, (4, 3): 23, (4, 4): 24,
}


# Definindo os pinos dos botões e as variáveis de controle
BUTTON_B_PIN = 5
BUTTON_A_PIN = 6
a = 0
b = 0

# Configura as portas dos botões como entrada
#button_a = machine.Pin(BUTTON_A_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
button_b = machine.Pin(BUTTON_B_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)


# Loop principal
while True:
    # Verifica se o botão B foi pressionado
    if button_b.value() == 1:
        b += 1
        if b > 12:
            b = 0
        print("B: {}".format(b))
        time.sleep_ms(200) # Aguarda um pequeno intervalo para evitar múltiplas contagens

    Bb = "B" + str(b)
    
    # Define a matriz 5x5
    led_matrix = eval(Bb)

    # Exibe a matriz nos LEDs
    for i in range(5):
        for j in range(5):
            # Obtém o índice do LED correspondente às coordenadas da matriz
            led_index = matrix_to_led_index[(i, j)]
            # Define a cor do LED na posição correspondente
            np[led_index] = led_matrix[i][j]

    np.write()

    # Aguarda 1 segundo
    time.sleep(1)





