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
import time
from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS

# Configurar UART para comunicação com o módulo NEO6M
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Instanciar o objeto micropyGPS com fuso horário (se suportado)
gps = MicropyGPS()  # O fuso horário pode ser ajustado mais tarde, se necessário

def update_led_matrix(np, snr_values):
    # Limpa a matriz antes de atualizar
    clear_matrix(np)

    # Ordena os valores de SNR em ordem decrescente e pega os 5 maiores
    sorted_snr_values = sorted(snr_values, reverse=True)[:5]

    for col, snr in enumerate(sorted_snr_values):
        intensity = map_snr_to_intensity(snr)
        # Calcula a altura da barra com base no SNR
        bar_height = int((snr / 50) * 5)  # Exemplo: SNR de 50 dá uma altura total (5)
        for row in range(5 - bar_height, 5):  # Preenche de baixo para cima
            np[row * 5 + col] = (intensity, intensity, intensity)  # Coloca a cor

    np.write()

# Inicializa a matriz de NeoPixels no GPIO7
NUM_LEDS = 25  # Número de LEDs na sua matriz
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)  # Inicializa os NeoPixels

def clear_matrix(np):
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)  # Define todas as cores para preto (apagado)
    np.write()  # Atualiza a matriz de LEDs com as novas cores

# Função para mapear SNR para intensidade
def map_snr_to_intensity(snr):
    # Mapeia SNR para intensidade do LED (ajuste os valores conforme necessário)
    return int((snr / 50) * 255)

# Apaga a matriz de LEDs inicialmente
clear_matrix(np)

while True:
    snr_values = []  # Lista para armazenar valores de SNR

    if gps_module.any():
        stat = gps_module.readline()
        try:
            stat = stat.decode('utf-8')
        except Exception as e:
            continue

        for char in stat:
            gps.update(char)

        time.sleep(0.1)

        if gps.satellite_data_updated():
            for sv_id, sv_data in gps.satellite_data.items():
                # sv_data é uma tupla (elevação, azimute, snr)
                if sv_data[2] is not None:  # Verifica se SNR está disponível
                    snr_values.append(sv_data[2])
            gps.unset_satellite_data_updated()

    # Atualiza a matriz de LEDs com os 5 maiores valores de SNR
    if snr_values:
        update_led_matrix(np, snr_values)