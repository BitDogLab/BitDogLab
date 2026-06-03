from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import time

x = ADC(Pin(27))
y = ADC(Pin(26))
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    # Inverte os eixos para o ponteiro seguir a mao.
    px = 127 - (x.read_u16() * 127 // 65535)
    py = 63 - (y.read_u16() * 63 // 65535)
    oled.fill(0)
    oled.text("+", px, py)
    oled.show()
    time.sleep_ms(50)
