import machine
import ssd1306
#from PIL import Image

# Configura o pino SDA e SCL do Raspberry Pi Pico
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=200000)

# Configura o display OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Abre a imagem desejada (no formato .jpg)
imagem = Image.open('exemplo.jpg')

# Redimensiona a imagem para caber no display OLED
imagem = imagem.resize((oled.width, oled.height))

# Converte a imagem para preto e branco
imagem = imagem.convert('1')

# Exibe a imagem no display OLED
oled.fill(0)
oled.show()
oled.image(imagem)
oled.show()
