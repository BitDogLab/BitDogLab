# aqui usamos o slot I2C0 conectando a um módulo GPS NEO 6 ou superior
# A conecção é: amarelo com o Tx do módulo GPS - Branco com o RX do módulo - Vermelho  com o VCC do módulo - preto com o GND
# Neste exemplo, map_snr_to_intensity converte o valor de SNR para uma intensidade de LED, e update_led_matrix atualiza a matriz de LEDs com essas intensidades.


from machine import Pin, UART, I2C
import neopixel
import utime
from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS


snr_values = []

# Initialize GPS module
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
time_zone = -3
gps = MicropyGPS(time_zone)  # Instancia do objeto GPS

# Initialize I2C and OLED display
i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Inicializa a matriz de NeoPixels no GPIO7
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

def clear_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)  # Define todas as cores para preto (apagado)
    np.write()  # Atualiza a matriz de LEDs com as novas cores

# Apaga todos os LEDs
clear_leds()

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

def test_led_matrix(np):
    for i in range(NUM_LEDS):
        np[i] = (255, 255, 255)  # Cor branca
    np.write()

test_led_matrix(np)


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
#clear_matrix(np)

def map_snr_to_intensity(snr):
    # Mapeia SNR para intensidade do LED (ajuste os valores conforme necessário)
    return int((snr / 50) * 255)

def update_led_matrix(np, snr_values):
    # Limpa a matriz antes de atualizar
    clear_matrix(np)  

    for col, snr in enumerate(snr_values[:5]):  # Limita a 5 valores
        intensity = map_snr_to_intensity(snr)
        # Calcula a altura da barra com base no SNR
        bar_height = int((snr / 50) * 5)  # Exemplo: SNR de 50 dá uma altura total (5)
        for row in range(5 - bar_height, 5):  # Preenche de baixo para cima
            np[row * 5 + col] = (intensity, intensity, intensity)  # Coloca a cor

    np.write()

def clear_matrix(np):
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()
    
""" teste
# Valores de SNR simulados para teste
snr_test_values = [10, 20, 30, 40, 50]  # Substitua por valores representativos
update_led_matrix(np, snr_test_values)

# Aguarde alguns segundos para visualizar a matriz de LEDs
utime.sleep(5)

# Limpar a matriz de LEDs após o teste
clear_leds()
"""  

while True:
    snr_values.clear()  # Limpa a lista de valores de SNR

    length = gps_module.any()
    if length > 0:
        data = gps_module.read(length)
        for byte in data:
            message = gps.update(chr(byte))

    latitude = convert_coordinates(gps.latitude)
    longitude = convert_coordinates(gps.longitude)

    if latitude is None or longitude is None:
        oled.fill(0)
        oled.text("Data unavailable", 35, 25)
        oled.text("No coordinates", 22, 40)
        oled.show()
        continue

    count = 0
    for sat_id, sat_info in gps.satellite_data.items():
        if count >= 5:
            break  # Limitar aos 5 primeiros satélites ativos

        if sat_info[0] and len(sat_info) > 3 and sat_info[3] is not None:
            snr = sat_info[3]  # SNR está na 4ª posição da tupla
            snr_values.append(snr)
            count += 1

    # Atualiza a matriz de LEDs
    update_led_matrix(np, snr_values)

    oled.fill(0)
    oled.text('Satellites: ' + str(gps.satellites_in_use), 10, 0)
    oled.text('Lat: ' + latitude, 0, 18)
    print('Lat: ' + latitude)
    oled.text('Lon: ' + longitude, 0, 36)
    print('Lon: ' + longitude)
    print("Valores reais de SNR:", snr_values)

    oled.show()
