from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
from machine import ADC
import neopixel
import time

# Configuração OLED com bit-banging
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Configuração da matriz de LEDs
np = neopixel.NeoPixel(Pin(7), 25)

# Configuração dos botões A e B
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Configuração do Joystick
joystick_x = ADC(Pin(26))
joystick_y = ADC(Pin(27))
joystick_button = Pin(22, Pin.IN, Pin.PULL_UP)

def display_menu():
    oled.fill(0)
    oled.text("Escolha botoes:", 0, 0)
    oled.text("A.Progr. Aritmetica", 0, 20)
    oled.text("B.Progr. Geometrica", 0, 40 )
    oled.show()

def display_pa(a1, r):
    oled.fill(0)
    oled.text(f"a1 = {a1}", 0, 0)
    oled.text(f"r = {r}", 0, 10)
    oled.show()

def display_pg(a1, q):
    oled.fill(0)
    oled.text(f"a1 = {a1}", 0, 0)
    oled.text(f"q = {q}", 0, 10)
    oled.show()

def light_leds_for_sequence(seq):
    for idx, value in enumerate(seq):
        for i in range(value):
            np[idx * 5 + i] = (30, 30, 35)
        np.write()
        time.sleep(1)
        np.fill((0, 0, 0))
       
THRESHOLD_UP = 5000   # Um valor um pouco acima do mínimo para considerar uma margem
THRESHOLD_DOWN = 60000  # Um valor um pouco abaixo do máximo para considerar uma margem

while True:
    display_menu()
    # Lógica para selecionar opção com os botões A e B
    if button_a.value() == 0: # Se o botão A for pressionado
        # PA selecionada
        a1, r = 1, 1  # Valores ajustados para a1 = 1 e r = 1
        display_pa(a1, r)
        sequence = [a1 + i*r for i in range(5)]  # Gerando a sequência PA: 1, 2, 3, 4, 5
        light_leds_for_sequence(sequence)
        time.sleep(3) # Aguardar 3 segundos após mostrar a sequência PA
    elif button_b.value() == 0: # Se o botão B for pressionado
        # PG selecionada
        a1, q = 1, 2  # Valores padrão, a1 = 1 e q = 2
        display_pg(a1, q)
        sequence = [a1 * (q**i) for i in range(4)]  # Gerando a sequência PG: 1, 2, 4, 8
        light_leds_for_sequence(sequence)
        time.sleep(3) # Aguardar 3 segundos após mostrar a sequência PG
