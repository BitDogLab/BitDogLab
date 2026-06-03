from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
n = 0

while True:
    oled.fill(0)
    oled.text("Contador", 28, 15)
    oled.text(str(n), 58, 35)
    oled.show()
    n += 1
    time.sleep(1)
