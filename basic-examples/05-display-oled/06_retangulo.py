from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.rect(20, 15, 88, 34, 1)
oled.fill_rect(25, 20, 30, 24, 1)
oled.show()
