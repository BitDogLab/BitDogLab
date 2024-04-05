from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import utime

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Teste OLED
oled.fill(0)  # Limpar display
oled.text("BitDogLab", 0, 0)
oled.text("Unicamp 4.0", 0, 10)
oled.show()



