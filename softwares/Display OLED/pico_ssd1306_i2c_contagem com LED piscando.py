from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

WIDTH = 128  # oled display width
HEIGHT = 64  # oled display height
i = 0

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
print("I2C Address      : " + hex(i2c.scan()[0]).upper())  # Display device address
print("I2C Configuration: " + str(i2c))  # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)  # Init oled display
oled.fill(0)
oled.show()
utime.sleep_ms(3000)
oled.text("Raspberry Pi", 10, 10)
oled.text("Pico", 10, 30)
oled.text("SSD1306:I2C", 10, 50)
oled.show()
utime.sleep_ms(3000)
oled.fill(0)


def on_forever():
    global i
    oled.fill(0)
    oled.text("Counter: " + str(i), 10, 10)
    oled.show()
    i += 1
    utime.sleep(1)


while True:
    on_forever()
