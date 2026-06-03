import machine, neopixel
import time
import numpy as np

np = neopixel.NeoPixel(machine.Pin(7), 25)

it = 100 # intensidade do LED, pode variar de 1 a 255

def or_led_tuples(led_matrix):
    # Flatten the 2D list of tuples into a 1D list of tuples
    led_tuples = [led for row in led_matrix for led in row]

"""
# define cores para os LEDs
B = (0, 0, 1*it) # BLUE
G = (0, 1*it, 0) # GREEN
R = (1*it, 0, 0) # RED
Y = (1*it, 1*it, 0) # YELLOW
M = (1*it, 0, 1*it) # MAGENTA
C = (0, 1*it, 1*it) # CYAN
W = (1*it, 1*it, 1*it) # WHITE
O = (0, 0, 0) # BLACK
"""
B = (0, 0, 255) # BLUE
G = (0, 255, 0) # GREEN
R = (255, 0, 0) # RED
Y = (255, 255, 0) # YELLOW
M = (255, 0, 255) # MAGENTA
C = (0, 255, 255) # CYAN
W = (255, 255, 255) # WHITE
O = (0, 0, 0) # BLACK

c = [
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O]
]

A0 = [
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O]
]

A1 = [
    [B, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O]
]

A2 = [
    [B, O, O, O, O],
    [B, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O]
]

A3 = [
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [O, O, O, O, O],
    [O, O, O, O, O]
]

A4 = [
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [O, O, O, O, O]
]

A5 = [
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O]
]

A6 = [
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, B, O, O, O]
]

A7 = [
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O]
]


A8 = [
    [B, O, O, O, O],
    [B, O, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O]
]

A9 = [
    [B, O, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O]
]
A10 = [
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O]
]

A11 = [
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, B, O, O]
]

A12 = [
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, O, O, O],
    [B, B, B, O, O],
    [B, B, B, O, O]
]

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
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, R, R, R]
]

B12 = [
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, O, R, R],
    [O, O, R, R, R],
    [O, O, R, R, R]
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
button_a = machine.Pin(BUTTON_A_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_b = machine.Pin(BUTTON_B_PIN, machine.Pin.IN, machine.Pin.PULL_DOWN)


# Loop principal
while True:
    
    
     # Verifica se o botão A foi pressionado
    if button_a.value() == 1:
        a += 1
        if a > 12:
            a = 0
        print("A: {}".format(a))
        time.sleep_ms(200) # Aguarda um pequeno intervalo para evitar múltiplas contagens

    Aa = "A" + str(a)
    
    # Define a matriz 5x5
    #led_matrixa = evalA(Aa)
    
    
    # Verifica se o botão B foi pressionado
    if button_b.value() == 1:
        b += 1
        if b > 12:
            b = 0
        print("B: {}".format(b))
        time.sleep_ms(200) # Aguarda um pequeno intervalo para evitar múltiplas contagens

    Bb = "B" + str(b)
    
    # Perform bitwise OR operation on each LED tuple
    result_tuples = [(0, 0, 0) for i in range(len(led_tuples))]
    for i in range(len(led_tuples)):
        for j in range(3):
            result_tuples[i] = (
                result_tuples[i][0] | led_tuples[i][0],
                result_tuples[i][1] | led_tuples[i][1],
                result_tuples[i][2] | led_tuples[i][2],
            )

    # Return the result as a 2D list of tuples
    return [result_tuples[i:i+5] for i in range(0, len(result_tuples), 5)]
    
    
    
    
    # Define a matriz 5x5
    led_matrix = eval(c)
  
    # Exibe a matriz nos LEDs
    for i in range(5):
        for j in range(5):
            # Obtém o índice do LED correspondente às coordenadas da matriz
            led_index = matrix_to_led_index[(i, j)]
            # Define a cor do LED na posição correspondente
            np[led_index] = led_matrixA[i][j]

    np.write()

    # Aguarda 1 segundo
    time.sleep(1)





