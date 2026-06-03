from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.rect(0, 0, 128, 64, 1)
oled.text("Borda", 43, 28)
oled.show()
