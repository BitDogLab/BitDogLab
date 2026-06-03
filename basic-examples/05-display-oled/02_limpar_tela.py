from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(1)
oled.show()
time.sleep(1)
oled.fill(0)
oled.show()
