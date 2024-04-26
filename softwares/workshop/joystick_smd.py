from machine import Pin, ADC
import neopixel
import time

# Inicializa o display
chain = neopixel.NeoPixel(Pin(7), 25)

# Inicializa o joystick
adc_x = ADC(Pin(27))
adc_y = ADC(Pin(26))

# Define a posição inicial (no centro do display)
x = 2
y = 2

# Define os valores mínimos e máximos dos conversores AD
adc_min = 300
adc_max = 65535

# Define as dimensões da matriz de LEDs
matrix_width = 5
matrix_height = 5

LED_MATRIX = [
    [24, 23, 22, 21, 20],    
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [ 5,  6,  7,  8,  9],
    [ 4,  3,  2,  1,  0]
]

# Define a função de mapeamento para o eixo x
def map_adc_to_position_x(value, adc_min, adc_max, matrix_size):
    position = int((value - adc_min) / (adc_max - adc_min + 1) * matrix_size)
    return min(max(position, 0), matrix_size - 1)

# Define a função de mapeamento para o eixo y
def map_adc_to_position_y(value, adc_max, adc_min, matrix_size):
    position = int((value - adc_min) / (adc_max - adc_min + 1) * matrix_size)
    return matrix_size - 1 - min(max(position, 0), matrix_size - 1)

while True:
    # Lê a posição do joystick
    adc_value_x = adc_x.read_u16()
    adc_value_y = adc_y.read_u16()

    # Mapeia os valores dos conversores AD para as posições x e y
    x = map_adc_to_position_x(adc_value_x, adc_min, adc_max, matrix_width)
    y = map_adc_to_position_y(adc_value_y, adc_min, adc_max, matrix_height)

    # Limpa o display
    for i in range(25):
        chain[i] = (0, 0, 0)

    # Calcula o índice do LED na matriz unidimensional
    # if((y % 2) == 0): 
    #     index = y * matrix_width + x
    # else:
    #     index = y * matrix_width + x
    # if((x,y) == (0,0)):
    #     index = 4
    # elif((x,y) == (0,0)):
    #     index = 
    index = LED_MATRIX[4-y][x]
    # Acende o LED na nova posição com a cor azul
    chain[index] = (110, 0, 0)

    # Atualiza o display
    chain.write()

    # Imprime os valores de x e y lado a lado na saída serial
    print("x: ", x, " y: ", y)

    # Aguarda um pouco antes da próxima leitura
    time.sleep(0.2)

