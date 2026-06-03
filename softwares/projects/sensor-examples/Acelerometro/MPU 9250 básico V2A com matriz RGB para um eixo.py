from machine import Pin, SoftI2C
from neopixel import NeoPixel
from mpu9250 import MPU9250
import time
import math

# Inicializar o I2C para o MPU (I2C1)
i2c_mpu = SoftI2C(scl=Pin(3), sda=Pin(2))
mpu = MPU9250(i2c_mpu)

# Inicializar a matriz NeoPixel no GPIO7
NUM_LEDS = 25
np = NeoPixel(Pin(7), NUM_LEDS)

# Definindo a matriz de LEDs (5x5)
LED_MATRIX = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

# Função para limpar a matriz de LEDs
def clear_matrix(np):
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

# Inicializar posição do LED
x, y = 2, 2

while True:
    # Limpar a matriz
    clear_matrix(np)

    # Ler dados de aceleração
    accel = mpu.acceleration
    ax, ay, az = accel

    # Atualizar posição do LED com base em AX
    x = int(2 + ax)  # Mapear aceleração para posição na matriz (2 é o centro)
    x = max(0, min(4, x))  # Garantir que a posição esteja dentro da matriz 5x5

    # Definir a cor do LED com base na aceleração (usando valor absoluto para cores mais brilhantes)
    r, g, b = int(abs(ax) * 25), int(abs(ay) * 25), int(abs(az) * 25)

    # Acender o LED na posição atual
    np[LED_MATRIX[x][y]] = (r, g, b)
    np.write()

    # Esperar antes da próxima atualização
    time.sleep(0.1)
