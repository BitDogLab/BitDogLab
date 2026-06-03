from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Display OLED I2C: SCL no GPIO3 e SDA no GPIO2.
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text("Ola mundo", 25, 20)
oled.text("BitDogLab", 22, 35)
oled.show()
