from machine import Pin, ADC, PWM, I2C
import neopixel
import ssd1306
import time

# Inicializa o LED RGB
led_red = PWM(Pin(12))
led_green = PWM(Pin(13))
led_blue = PWM(Pin(11))
led_red.freq(1000)
led_green.freq(1000)
led_blue.freq(1000)

# Inicializa os botões
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Inicializa os buzzers
buzzer_a = PWM(Pin(21))
buzzer_b = PWM(Pin(4))

# Inicializa a matriz de LEDs RGB
neopixel_pin = Pin(7)
num_leds = 25
chain = neopixel.NeoPixel(neopixel_pin, num_leds)

# Inicializa o joystick
adc_x = ADC(Pin(26))
adc_y = ADC(Pin(27))
joystick_button = Pin(22, Pin.IN, Pin.PULL_UP)

# Inicializa o display OLED
i2c = I2C(0, sda=Pin(14), scl=Pin(15))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Define as cores para o LED RGB
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)

# Define as intensidades iniciais dos LEDs RGB
led_red_intensity = 0
led_green_intensity = 0
led_blue_intensity = 0

# Define os valores mínimo e máximo para as intensidades
intensity_min = 0
intensity_max = 1023

# Define a cor inicial do LED RGB
current_color = COLOR_BLUE

# Define a intensidade inicial dos buzzers
buzzer_a_intensity = 0
buzzer_b_intensity = 0

# Define os valores mínimo e máximo para as intensidades dos buzzers
buzzer_intensity_min = 0
buzzer_intensity_max = 1023

# Define a posição inicial do joystick
x = 2
y = 2

# Define os valores mínimos e máximos dos conversores AD do joystick
adc_min = 300
adc_max = 65535

# Função para mapear um valor de ADC para uma posição na matriz de LEDs
def map_adc_to_position(adc_value, adc_min, adc_max, matrix_size):
    position = int((adc_value - adc_min) / (adc_max - adc_min + 1) * matrix_size)
    return min(max(position, 0), matrix_size - 1)

while True:
    # Lê a posição do joystick
    adc_value_x = adc_x.read_u16()
    adc_value_y = adc_y.read_u16()

    # Mapeia os valores dos conversores AD para as posições x e y
    x = map_adc_to_position(adc_value_x, adc_min, adc_max, 5)
    y = map_adc_to_position(adc_value_y, adc_min, adc_max, 5)

    # Lê o estado atual dos botões A, B e do joystick
    button_a_state = button_a.value()
    button_b_state = button_b.value()
    joystick_button_state = joystick_button.value()

    # Verifica se o botão A foi pressionado
    if button_a_state == 0:
        # Diminui a intensidade dos LEDs RGB
        if led_red_intensity > intensity_min:
            led_red_intensity -= 20
        if led_green_intensity > intensity_min:
            led_green_intensity -= 20
        if led_blue_intensity > intensity_min:
            led_blue_intensity -= 20

    # Verifica se o botão B foi pressionado
    if button_b_state == 0:
        # Aumenta a intensidade dos LEDs RGB
        if led_red_intensity < intensity_max:
            led_red_intensity += 20
        if led_green_intensity < intensity_max:
            led_green_intensity += 20
        if led_blue_intensity < intensity_max:
            led_blue_intensity += 20

    # Verifica se o botão do joystick foi pressionado
    if joystick_button_state == 0:
        # Altera a cor do LED RGB
        if current_color == COLOR_BLUE:
            current_color = COLOR_RED
        elif current_color == COLOR_RED:
            current_color = COLOR_GREEN
        elif current_color == COLOR_GREEN:
            current_color = COLOR_BLUE

    # Define as intensidades dos LEDs RGB
    led_red.duty_u16(led_red_intensity)
    led_green.duty_u16(led_green_intensity)
    led_blue.duty_u16(led_blue_intensity)

    # Define a cor da matriz de LEDs RGB
    chain.fill(current_color)

    # Verifica se o botão do joystick foi pressionado
    if joystick_button_state == 0:
        # Altera a intensidade dos buzzers
        if buzzer_a_intensity < buzzer_intensity_max:
            buzzer_a_intensity += 20
        if buzzer_b_intensity < buzzer_intensity_max:
            buzzer_b_intensity += 20

    # Define as intensidades dos buzzers
    buzzer_a.duty_u16(buzzer_a_intensity)
    buzzer_b.duty_u16(buzzer_b_intensity)

    # Atualiza o display OLED com as posições x e y
    display.fill(0)  # Limpa o display
    display.text("x: {}".format(x), 0, 0, 1)
    display.text("y: {}".format(y), 0, 10, 1)
    display.show()

    # Aguarda um pouco antes da próxima leitura
    time.sleep(0.1)
