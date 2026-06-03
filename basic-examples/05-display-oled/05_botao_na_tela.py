from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    oled.fill(0)
    oled.text("Botao A", 35, 15)
    oled.text("apertado" if botao.value() == 0 else "solto", 32, 35)
    oled.show()
    time.sleep_ms(100)
