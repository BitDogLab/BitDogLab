# aqui usamos o slot I2C0 conectando a um módulo GPS NEO 6 ou superior
# A conecção é: amarelo com o Tx do módulo GPS - Branco com o RX do módulo - Vermelho  com o VCC do módulo - preto com o GND

from machine import Pin, UART, I2C, neopixel
import utime
from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS

# Initialize I2C and OLED display
i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

#inicializa matriz de leds

np = neopixel.NeoPixel(machine.Pin(7), 25)

it=100# intensidade do LED, pode variar de 1 a 255

# definir cores para os LEDs
BLU = (0, 0, 1*it)# BLUE
GRE = (0, 1*it, 0)# GREEN
RED = (1*it, 0, 0)
YEL = (1*it, 1*it, 0)# YELLOW
MAGE = (1*it, 0, 1*it)# MANGENTA
CYA = (0, 1*it, 1*it)# CYAN
WHI = (1*it, 1*it, 1*it)# WHIE
BLA = (0, 0, 0)# BLACK

# Initialize GPS module
#gps_module = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
time_zone = -3
gps = MicropyGPS(time_zone)

def convert_coordinates(sections):
    if sections[0] == 0:  # sections[0] contains the degrees
        return None

    # sections[1] contains the minutes
    data = sections[0] + (sections[1] / 60.0)

    # sections[2] contains 'E', 'W', 'N', 'S'
    if sections[2] == 'S':
        data = -data
    if sections[2] == 'W':
        data = -data

    data = '{0:.6f}'.format(data)  # 6 decimal places
    return str(data)

def clear_matrix(np):
    # Cria uma matriz 5x5 com todas as cores definidas como preto (desligadas)
    off_matrix = [[(0, 0, 0) for _ in range(5)] for _ in range(5)]

    # Inverte a matriz
    inverted_matrix = off_matrix[::-1]

    # Exibe a matriz invertida nos LEDs
    for i in range(5):
        for j in range(5):
            np[i*5+j] = inverted_matrix[i][j]

    np.write()
    
# Apaga a matriz
clear_matrix(np)


while True:
    length = gps_module.any()
    if length > 0:
        data = gps_module.read(length)
        for byte in data:
            message = gps.update(chr(byte))

    latitude = convert_c oordinates(gps.latitude)
    longitude = convert_coordinates(gps.longitude)

    if latitude is None or longitude is None:
        oled.fill(0)
        oled.text("Data unavailable", 35, 25)
        oled.text("No coordinates", 22, 40)
        oled.show()
        continue

    
    oled.fill(0)
    oled.text('Satellites: ' + str(gps.satellites_in_use), 10, 0)
    oled.text('Lat: ' + latitude, 0, 18)
    print('Lat: ' + latitude)
    oled.text('Lon: ' + longitude, 0, 36)
    print('Lon: ' + longitude)

    oled.show()