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

# Verifique se o OLED está funcionando
oled.fill(0)
oled.text('Teste OLED', 0, 0)
oled.show()

# Inicialização do GPS
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
gps = MicropyGPS()

# [Resto do código para LED_MATRIX, np, etc.]

def convert_coordinates(sections):
    if sections[0] == 0:  # sections[0] contém os graus
        return None

    # sections[1] contém os minutos
    data = sections[0] + (sections[1] / 60.0)

    # sections[2] contém 'E', 'W', 'N', 'S'
    if sections[2] == 'S' or sections[2] == 'W':
        data = -data

    data = '{0:.6f}'.format(data)  # 6 casas decimais
    return str(data)


while True:
    snr_values = []

    if gps_module.any():
        stat = gps_module.readline()
        try:
            stat = stat.decode('utf-8')
        except Exception as e:
            continue

        for char in stat:
            gps.update(char)

        if gps.satellite_data_updated():
            for sv_id, sv_data in gps.satellite_data.items():
                if sv_data[2] is not None:  # Verifica se SNR está disponível
                    snr = sv_data[2]  # SNR está na terceira posição da tupla
                    snr_values.append(snr)
            gps.unset_satellite_data_updated()


        latitude = convert_coordinates(gps.latitude)
        longitude = convert_coordinates(gps.longitude)

        print("Lat:", latitude, "Lon:", longitude)  # Debug: Imprimir coordenadas

        oled.fill(0)
        if latitude is not None and longitude is not None:
            oled.text('Lat: ' + latitude, 0, 20)
            oled.text('Lon: ' + longitude, 0, 40)
        else:
            oled.text("No coordinates", 0, 0)
        oled.text('Satelites: ' + str(gps.satellites_in_use), 0, 0)
        oled.show()

              


        # Atualiza a matriz de LEDs
        sorted_snr_values = sorted(snr_values, reverse=True)[:5]
        for col, snr in enumerate(sorted_snr_values):
            # [Código para atualizar a matriz de LEDs]

        # Imprimir dados de SNR dos satélites
            print("Dados SNR dos Satélites:")
        for sv_id, sv_data in gps.satellite_data.items():
            print(f"Satélite {sv_id}: Elevação={sv_data[0]}, Azimute={sv_data[1]}, SNR={sv_data[2]}")
        gps.unset_satellite_data_updated()

    # [Restante do loop while True]
