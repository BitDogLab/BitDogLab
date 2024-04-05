from machine import Pin, ADC
import neopixel
import time

# Inicializa o display
chain = neopixel.NeoPixel(Pin(7), 25)

# Inicializa o joystick
adc_x = ADC(Pin(27))
adc_y = ADC(Pin(26))
joystick_button = Pin(22, Pin.IN, Pin.PULL_UP)
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Define a posição inicial (no centro do display)
x = 2
y = 2

# Define os valores mínimos e máximos dos conversores AD
adc_min = 300
adc_max = 65535

# Define as dimensões da matriz de LEDs
matrix_width = 5
matrix_height = 5

# Define as cores para os LEDs
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

# Define a cor atual do LED
current_color = COLOR_BLUE

# Define a intensidade inicial do LED
intensity = 110

# Define os valores mínimo e máximo para a intensidade
intensity_min = 10
intensity_max = 250

# Define o estado atual do botão do joystick
joystick_button_pressed = False

def map_adc_to_position(adc_value, adc_min, adc_max, matrix_size):
    position = int((adc_value - adc_min) / (adc_max - adc_min + 1) * matrix_size)
    return min(max(position, 0), matrix_size - 1)

while True:
    # Lê a posição do joystick
    adc_value_x = adc_x.read_u16()
    adc_value_y = adc_y.read_u16()

    # Mapeia os valores dos conversores AD para as posições x e y
    x = map_adc_to_position(adc_value_x, adc_min, adc_max, matrix_width)
    y = matrix_height - 1 - map_adc_to_position(adc_value_y, adc_min, adc_max, matrix_height)

    # Lê o estado atual dos botões A, B e do joystick
    button_a_state = button_a.value()
    button_b_state = button_b.value()
    joystick_button_state = joystick_button.value()

    # Verifica se o botão do joystick foi pressionado
    if joystick_button_state == 0 and not joystick_button_pressed:
        joystick_button_pressed = True

        # Altera a cor do LED
        if current_color == COLOR_BLUE:
            current_color = COLOR_RED
        elif current_color == COLOR_RED:
            current_color = COLOR_GREEN
        elif current_color == COLOR_GREEN:
            current_color = COLOR_BLUE

    # Verifica se o botão do joystick foi solto
    if joystick_button_state == 1:
        joystick_button_pressed = False

    # Verifica se o botão A foi pressionado
    if button_a_state == 0:
        # Diminui a intensidade em 20 até o valor mínimo
        if intensity > intensity_min:
            intensity -= 20

    # Verifica se o botão B foi pressionado
    if button_b_state == 0:
        # Aumenta a intensidade em 20 até o valor máximo
        if intensity < intensity_max:
            intensity += 20

    # Limpa o display
    for i in range(25):
        chain[i] = (0, 0, 0)

    # Calcula o índice do LED na matriz unidimensional
    index = y * matrix_width + x

    # Define a cor do LED na nova posição com a intensidade atual
    chain[index] = tuple([int(color * intensity / 255) for color in current_color])

    # Atualiza o display
    chain.write()

    # Imprime os valores de x e y lado a lado na saída serial
    print("x: ", x, " y: ", y, "cor ( RED   GREEN   BLUE ):", current_color, "intensity:", intensity)

    # Aguarda um pouco antes da próxima leitura
    time.sleep(0.2)

