from machine import Pin, I2C
from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
from neopixel import NeoPixel
import time

x0 = 10
x1 = 10

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)


i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
i2c1 = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
devices0 = i2c0.scan()
devices1 = i2c1.scan()

print("Endereços dos dispositivos I2C conectados:")
print("I2C0:")
for device in devices0:
    print("   ",hex(device))
print("I2C1:")
for device in devices1:
    print("   ",hex(device))
    
# Teste OLED
oled.fill(0)  # Limpar display
oled.text("I2C0", 0, 0)
for device in devices0:
    oled.text(hex(device), x0, 10)
    x0=x0+10

oled.text("I2C1", 0, 30)
for device in devices1:
    oled.text(hex(device), x1, 40)
    x1=x1+10
    
   
oled.show()


