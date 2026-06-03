from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    for largura in range(0, 101, 5):
        oled.fill(0)
        oled.text("Carregando", 22, 15)
        oled.rect(14, 35, 100, 10, 1)
        oled.fill_rect(14, 35, largura, 10, 1)
        oled.show()
        time.sleep_ms(120)
