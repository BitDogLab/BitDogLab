#=================================================================
# Project : OLED 128x64 (SSD1306) I2C
#         : 
# Date    : 2021-02-01
# Version : 1.0
#
# Note:
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY : without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE
#
# Board : Raspberry Pi Pico
#
#=================================================================
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
import utime

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)       # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
oled.fill(0)
oled.show()
utime.sleep_ms(3000)
oled.text("Raspberry Pi", 10,10)
oled.text("Pico", 10,30)
oled.text("SSD1306:I2C", 10, 50)
oled.show()
utime.sleep_ms(3000)
oled.fill(0)

while(True):
    
    oled.rect(0,0,WIDTH, HEIGHT,1)
    for y in range(0,HEIGHT,8):
        oled.hline(0,y,WIDTH,1)
        oled.show()
        utime.sleep_ms(10)
    
    utime.sleep_ms(1000)
    oled.fill(0)
    
    oled.rect(0,0,WIDTH, HEIGHT,1)
    for x in range(0,WIDTH,8):
        oled.vline(x,0,HEIGHT,1)
        oled.show()
        utime.sleep_ms(10)

