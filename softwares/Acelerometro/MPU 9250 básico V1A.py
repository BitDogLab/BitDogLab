from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from mpu9250 import MPU9250
import time
from neopixel import NeoPixel
from machine import Pin

# Inicializar o I2C para o OLED (I2C0)
i2c_oled = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c_oled)

# Inicializar o I2C para o MPU (I2C1)
i2c_mpu = SoftI2C(scl=Pin(3), sda=Pin(2))
mpu = MPU9250(i2c_mpu)

# Limpar o display OLED
oled.fill(0)
oled.show()

# Inicialize o NeoPixel (supondo que você tenha 25 LEDs e eles estão conectados ao pino GPIO7)
NUM_LEDS = 25
np = NeoPixel(Pin(7), NUM_LEDS)

# Função para limpar a matriz de LEDs
def clear_matrix(np):
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()
    
# Chamada à função para limpar a matriz de LEDs
clear_matrix(np)
    
    

while True:
    # Limpar o display OLED
    oled.fill(0)
    
    # Ler dados de aceleração
    accel = mpu.acceleration
    ax, ay, az = accel[0], accel[1], accel[2]

    # Exibir dados de aceleração no OLED
    oled.text("Accel (m/s^2):", 0, 0)
    oled.text("AX: {:.2f}".format(ax), 0, 20)
    oled.text("AY: {:.2f}".format(ay), 0, 30)
    oled.text("AZ: {:.2f}".format(az), 0, 40)
    
    # Atualizar o display
    oled.show()

    # Esperar um pouco antes de atualizar
    time.sleep(0.1)
