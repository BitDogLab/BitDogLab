from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
from neopixel import NeoPixel
import time

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Teste OLED
oled.fill(0)  # Limpar display
oled.text("BitDogLab", 0, 0)
oled.text("Unicamp 4.0", 0, 10)
oled.show()

# Configuração Neopixel
NUM_LEDS = 25
np = NeoPixel(Pin(7), NUM_LEDS)

# Teste Neopixel
for i in range(NUM_LEDS):
    np[i] = (255, 0, 0)
    np.write()
    time.sleep(0.1)
    np[i] = (0, 0, 0)

# Teste LED RGB
led_r = Pin(12, Pin.OUT)
led_g = Pin(13, Pin.OUT)
led_b = Pin(11, Pin.OUT)
led_r.value(1)
time.sleep(1)
led_g.value(1)
time.sleep(1)
led_b.value(1)
time.sleep(1)
led_r.value(0)
led_g.value(0)
led_b.value(0)

# Teste Buzzer
buzzer_a = Pin(21, Pin.OUT)
buzzer_b = Pin(4, Pin.OUT)
buzzer_a.value(1)
buzzer_b.value(1)
time.sleep(1)
buzzer_a.value(0)
buzzer_b.value(0)

# Joystick e botões podem ser testados em loops, 
# verificando sua entrada e exibindo os valores no OLED ou acendendo LEDs conforme sua posição/pressão.

