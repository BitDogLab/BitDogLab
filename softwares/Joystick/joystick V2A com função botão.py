from machine import Pin, ADC
import neopixel
import time

# Inicializa o display
chain = neopixel.NeoPixel(Pin(7), 25)

# Inicializa o joystick
adc_x = ADC(Pin(27))
adc_y = ADC(Pin(26))
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)
joystick_button = Pin(22, Pin.IN, Pin.PULL_UP)

# Define a posição inicial (no centro do display)
x = 2
y = 2

# Define um limiar para determinar uma "grande" mudança
threshold = 50

# Armazena o último valor ADC de x e y
last_adc_value_x = adc_x.read_u16()
last_adc_value_y = adc_y.read_u16()

# Define as cores para os LEDs
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

# Define o estado atual dos botões A, B e do joystick
button_a_state = 1
button_b_state = 1
joystick_button_state = 1

# Define o estado atual do botão do joystick (para mudança de cor)
joystick_button_pressed = False

while True:
    # Lê a posição do joystick
    adc_value_x = adc_x.read_u16()
    adc_value_y = adc_y.read_u16()

    # Lê o estado atual dos botões A, B e do joystick
    button_a_state = button_a.value()
    button_b_state = button_b.value()
    joystick_button_state = joystick_button.value()

    # Limpa o display
    for i in range(25):
        chain[i] = (0, 0, 0)

    # Verifica se houve uma grande mudança no valor ADC de x
    if abs(adc_value_x - last_adc_value_x) > threshold:
        if adc_value_x > 40000 and x < 4:
            x += 1
            print("x: ", x, " y: ", y, "adx:", adc_value_x, "ady:", adc_value_y, "intensity:", intensity)
        elif adc_value_x < 20000 and x > 0:
            x -= 1
            print("x: ", x, " y: ", y, "adx:", adc_value_x, "ady:", adc_value_y, "intensity:", intensity)
            
    # Verifica se houve uma grande mudança no valor ADC de y
    if abs(adc_value_y - last_adc_value_y) > threshold:
        if adc_value_y > 40000  and y > 0:
            y -= 1
        elif adc_value_y < 20000 and y < 4:
            y += 1

    # Atualiza os últimos valores ADC de x e y
    last_adc_value_x = adc_value_x
    last_adc_value_y = adc_value_y

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

    # Calcula o índice do LED na matriz unidimensional
    index = y * 5 + x

    # Define a cor do LED na nova posição com a intensidade atual
    chain[index] = tuple([int(color * intensity / 255) for color in current_color])

    # Atualiza o display
    chain.write()

    # Imprime os valores de x e y lado a lado na saída serial
    print("x: ", x, " y: ", y, "adx:", adc_value_x, "ady:", adc_value_y, "intensity:", intensity)
   
    
    # Aguarda um pouco antes da próxima leitura
    time.sleep(0.1)




