from machine import Pin, I2C
from utime import sleep
from ssd1306 import SSD1306_I2C
import time
from machine import Pin, SoftI2C, ADC

from bh1750 import BH1750

i2c0_sda = Pin(2)
i2c0_scl = Pin(3)
i2c0 = I2C(1, sda=i2c0_sda, scl=i2c0_scl)

bh1750 = BH1750(0x23, i2c0)

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

while True:
    luminosity = bh1750.measurement
    luminosity = round(luminosity, 1)  # Arredonda para uma casa decimal
    print(luminosity)
    sleep(.2)

    for measurement in bh1750.measurements():
        measurement = round(measurement, 1)  # Arredonda para uma casa decimal
        print(measurement)
       
        oled.fill(0)  # Limpar display
        oled.text("Luminosidade:", 0, 0)
        oled.text(str(measurement), 40, 30)
        oled.show()

