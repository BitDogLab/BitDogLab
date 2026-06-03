from machine import Pin, ADC
import neopixel
import utime

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

ponto = []
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)
joystick_button = Pin(22, Pin.IN, Pin.PULL_UP)
# Define o estado atual dos botões A, B e do joystick
button_a_state = 1
button_b_state = 1
joystick_button_state = 1

COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_YELLOW = (255, 255, 0)
# Define a cor atual do LED
current_color = COLOR_BLUE

# Define a intensidade inicial dos LEDs
intensity = 155

# Define os valores mínimo e máximo para a intensidade
intensity_min = 20
intensity_max = 255

while True:
    # Lê a posição do joystick
    adc_value_x = adc_x.read_u16()
    adc_value_y = adc_y.read_u16()

    # Mapeia os valores dos conversores AD para as posições x e y
    x = map_adc_to_position_x(adc_value_x, adc_min, adc_max, matrix_width)
    y = map_adc_to_position_y(adc_value_y, adc_min, adc_max, matrix_height)

    # Limpa o display
    chain.fill((0,0,0))
    # for i in range(25):
    #     chain[i] = (0, 0, 0)

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
    chain[index] = tuple([int(color * intensity / 255) for color in current_color])

    # Atualiza o display
    chain.write()

    # Imprime os valores de x e y lado a lado na saída serial
    print(adc_value_x)

    button_a_state = button_a.value()
    button_b_state = button_b.value()
    joystick_button_state = joystick_button.value()
    # Verifica se o botão do joystick foi pressionado
    if joystick_button_state == 0 and not joystick_button_pressed:
        joystick_button_pressed = True

        # Alterna entre as cores do LED
        if current_color == COLOR_BLUE:
            current_color = COLOR_RED
        elif current_color == COLOR_RED:
            current_color = COLOR_YELLOW
        else:
            current_color = COLOR_BLUE

        # Define a posição para o centro
        x = 2
        y = 2

    # Verifica se o botão do joystick foi solto
    if joystick_button_state == 1:
        joystick_button_pressed = False
    
    if button_a_state == 0:
        # Diminui a intensidade em 20 até o valor mínimo
        if intensity > intensity_min:
            intensity -= 20

    # Verifica se o botão B foi pressionado
    if button_b_state == 0:
        # Aumenta a intensidade em 20 até o valor máximo
        if intensity < intensity_max:
            intensity += 20

    # Aguarda um pouco antes da próxima leitura
    utime.sleep(0.2)

