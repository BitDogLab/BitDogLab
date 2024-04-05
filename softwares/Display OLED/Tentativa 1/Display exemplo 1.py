'''
Demonstração do uso de display OLED com o Raspberry Pi Pico
'''
from machine import I2C
from time import sleep
from random import randrange
import framebuf
import ssd1306
 
# Usa a configuração padrão do I2C
i2c = I2C(0)
 
# Inicia o display
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.text( "Ola, PiPico!", 0, 0)
display.show()
 
# Carrega imagem
def loadPBM(arq, tamX, tamY):
    with open(arq, 'rb') as f:
        f.readline() # Magic number
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())
    return framebuf.FrameBuffer(data, tamX, tamY, framebuf.MONO_HLSB)
 
fbuf = loadPBM('MakerHero.pbm', 128, 39)
 
# Mostra a imagem no display
display.blit(fbuf, 0, 16)
display.show()
sleep(5)
 
# Limpa a imagem
display.fill_rect(0, 16, 128, 48, 0)
 
# Vamos fazer um gráfico de barras aleatórias
while True:
    for x in range(0, 128, 16):
        y = randrange (10, 50)
        display.fill_rect(x, 10, 12, 54, 0)
        display.fill_rect(x, y, 12, 64-y, 1)
    display.show()
    sleep(1)