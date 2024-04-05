from machine import Pin, SoftI2C
import neopixel
import time
from ssd1306 import SSD1306_I2C

# Configuração OLED com bit-banging
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Configuração dos Buzzer
buzzer_a = Pin(21, Pin.OUT)
buzzer_b = Pin(4, Pin.OUT)

# Configuração da matriz de LEDs
np = neopixel.NeoPixel(Pin(7), 25)

heart_on = [
    0, 0, 45, 0, 0,
    0, 45, 45, 45, 0,
    45, 45, 45, 45, 45,
    45, 45, 45, 45, 45,
    0, 45, 0, 45, 0
]

heart_off = [
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 0, 0, 0
]

# Configuração do LED RGB
led_r = Pin(12, Pin.OUT)
led_g = Pin(13, Pin.OUT)
led_b = Pin(11, Pin.OUT)

def display_heart(state):
    for i in range(25):
        if state[i]:
            np[i] = (45, 0, 0)
        else:
            np[i] = (0, 0, 0)
    np.write()
    
def set_rgb_color(r, g, b):
    led_r.value(r)
    led_g.value(g)
    led_b.value(b)

# Função para mostrar mensagem no OLED
def display_message():
    oled.fill(0)
    oled.text("Hello,", 0, 10)
    oled.text("I Love You!", 0, 30)
    oled.show()

# Display inicial
display_message()

while True:
    # Alternar buzzer
    buzzer_a.value(1)
    buzzer_b.value(0)
    display_heart(heart_on)
    time.sleep(0.5)
    
    buzzer_a.value(0)
    buzzer_b.value(1)
    display_heart(heart_off)
    
    set_rgb_color(0, 1, 1)
    time.sleep(0.5)
    set_rgb_color(0, 0, 0)
