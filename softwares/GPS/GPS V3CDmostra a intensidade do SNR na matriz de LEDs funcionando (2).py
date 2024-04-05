# aqui usamos o slot I2C0 conectando a um módulo GPS NEO 6 ou superior
# A conecção é: amarelo com o Tx do módulo GPS - Branco com o RX do módulo - Vermelho  com o VCC do módulo - preto com o GND
# Neste exemplo, map_snr_to_intensity converte o valor de SNR para uma intensidade de LED, e update_led_matrix atualiza a matriz de LEDs com essas intensidades.
'''
Passo a passo do código:

Colete os dados de SNR dos satélites conforme você leu do módulo GPS.
Armazene esses dados em uma lista.
Ordene a lista e pegue os 5 maiores valores.
Use esses valores para atualizar a matriz de LEDs.
'''

import machine
from machine import UART, Pin, I2C
import neopixel
from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS

# Inicialização do I2C e OLED
i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Inicialização do GPS
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
gps = MicropyGPS()

# Definição da matriz de LEDs
NUM_LEDS = 25  # Número total de LEDs
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)
LED_MATRIX = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

def clear_matrix():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def update_led_matrix(snr_values):
    #clear_matrix()
    sorted_snr_values = sorted(snr_values, reverse=True)[:5]
    for col, snr in enumerate(sorted_snr_values):
        led_height = map_snr_to_led_height(snr)
        for row in range(led_height):
            led_index = LED_MATRIX[row][col]
            np[led_index] = (0, 25, 25)  # Ajuste a cor conforme necessário
    np.write()
    
def map_snr_to_led_height(snr):
    # Mapeia o valor de SNR para a altura da coluna de LEDs
    # com uma resolução melhor
    if snr <= 8:
        return 1  # Acende 1 LED
    elif snr <= 17:
        return 2  # Acende 2 LEDs
    elif snr <= 24:
        return 3  # Acende 3 LEDs
    elif snr <= 40:
        return 4  # Acende 4 LEDs
    else:
        return 5  # Acende 5 LEDs (toda a coluna)


def convert_coordinates(sections):
    if sections[0] == 0:
        return None
    data = sections[0] + (sections[1] / 60.0)
    if sections[2] in ['S', 'W']:
        data = -data
    return '{0:.6f}'.format(data)

while True:
    snr_values = []

    if gps_module.any():
        stat = gps_module.readline()
        try:
            stat = stat.decode('utf-8')
        except Exception:
            continue

        for char in stat:
            gps.update(char)

        if gps.satellite_data_updated():
            for sv_id, sv_data in gps.satellite_data.items():
                if sv_data[2] is not None:
                    snr_values.append(sv_data[2])
            gps.unset_satellite_data_updated()

        latitude = convert_coordinates(gps.latitude)
        longitude = convert_coordinates(gps.longitude)

        oled.fill(0)
        if latitude and longitude:
            oled.text('Satelites: ' + str(gps.satellites_in_use), 0, 0)
            oled.text('Lat: ' + latitude, 0, 20)
            oled.text('Lon: ' + longitude, 0, 40)
           
        else:
            oled.fill(0)
            oled.text("No coordinates", 0, 0)
        
        oled.show()

        update_led_matrix(snr_values)

        print("Dados SNR dos Satélites:")
        for sv_id, sv_data in gps.satellite_data.items():
            print(f"Satélite {sv_id}: Elevação={sv_data[0]}, Azimute={sv_data[1]}, SNR={sv_data[2]}")

            gps.unset_satellite_data_updated()

