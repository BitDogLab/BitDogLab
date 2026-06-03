from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import time

mic = ADC(Pin(28))
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
centro = 32768

while True:
    pico = 0
    for _ in range(50):
        valor = abs(mic.read_u16() - centro)
        if valor > pico:
            pico = valor
    largura = min(120, pico // 250)
    oled.fill(0)
    oled.text("Microfone", 25, 8)
    oled.rect(4, 35, 120, 12, 1)
    oled.fill_rect(4, 35, largura, 12, 1)
    oled.show()
    time.sleep_ms(80)
