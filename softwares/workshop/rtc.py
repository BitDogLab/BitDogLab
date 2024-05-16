# Basic functions:

# oled.poweroff()     # power off the oled, pixels persist in memory
# oled.poweron()      # power on the oled, pixels redrawn
# oled.contrast(0)    # dim
# oled.contrast(255)  # bright
# oled.invert(1)      # oled inverted
# oled.invert(0)      # oled normal
# oled.rotate(True)   # rotate 180 degrees
# oled.rotate(False)  # rotate 0 degrees
# oled.show()         # write the contents of the FrameBuffer to oled memory
# Subclassing FrameBuffer provides support for graphics primitives:

# oled.fill(0)                         # fill entire screen with colour=0
# oled.pixel(0, 10)                    # get pixel at x=0, y=10
# oled.pixel(0, 10, 1)                 # set pixel at x=0, y=10 to colour=1
# oled.hline(0, 8, 4, 1)               # draw horizontal line x=0, y=8, width=4, colour=1
# oled.vline(0, 8, 4, 1)               # draw vertical line x=0, y=8, height=4, colour=1
# oled.line(0, 0, 127, 63, 1)          # draw a line from 0,0 to 127,63
# oled.rect(10, 10, 107, 43, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
# oled.fill_rect(10, 10, 107, 43, 1)   # draw a solid rectangle 10,10 to 117,53, colour=1
# oled.text('Hello World', 0, 0, 1)    # draw some text at x=0, y=0, colour=1
# oled.scroll(20, 0)                   # scroll 20 pixels to the right

from machine import Pin, SoftI2C, RTC
from ssd1306 import SSD1306_I2C
import utime
from sys import stdin
from select import select

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# leds
green = Pin(11, Pin.OUT) # verde
blue = Pin(12, Pin.OUT) # azul
red = Pin(13, Pin.OUT) #vermelho

#configurações RTC
rtc = RTC()


data = {
    'ano' : 2025,
    'mes' : 5,
    'dia' : 13,
    'horas' : 19,
    'minutos' : 53,
    'segundos' : 30 
    
}

rtc.datetime((
    data['ano'], 
    data['mes'], 
    data['dia'], 
    0, 
    data['horas'], 
    data['minutos'], 
    data['segundos'], 
    0
    ))

while True:

    ano = rtc.datetime()[0]
    mes = rtc.datetime()[1]
    dia = rtc.datetime()[2]
    horas = rtc.datetime()[4]
    minutos = rtc.datetime()[5]
    segundos = rtc.datetime()[6]

    oled.fill(0)  # Limpar oled
    oled.text(f"{dia}/{mes}/{ano}", 30, 0, 1)
    oled.text(f"{horas}:{minutos}:{segundos}", 0, 10, 1)
    # oled.text(f"{time.gmtime()[0:3]}", 0, 30, 1)
    # oled.text(f"{time.gmtime()[3:7]}", 0, 50, 1)
    oled.show()

    
    if (segundos % 3) == 0:
        red.toggle()
        utime.sleep(1)
    
    # if (segundos % 7) == 0:
    #     green.toggle()
    #     utime.sleep(1)

    # if (segundos % 10) == 0:
    #     blue.toggle()
    #     utime.sleep(1)

    