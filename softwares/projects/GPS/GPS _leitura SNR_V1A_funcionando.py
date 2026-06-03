import machine
from machine import UART, Pin
import micropyGPS
import time

# Configurar UART para comunicação com o módulo NEO6M
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Instanciar o objeto micropyGPS com fuso horário (se suportado)
gps = micropyGPS.MicropyGPS()  # O fuso horário pode ser ajustado mais tarde, se necessário

while True:
    if gps_module.any():
        # Ler dados do GPS como bytes
        stat = gps_module.readline()

        # Tente decodificar para uma string
        try:
            stat = stat.decode('utf-8')
        except Exception as e:
            print("Erro na decodificação dos dados:", e)
            continue

        # Alimentar dados para o parser micropyGPS
        for char in stat:
            gps.update(char)

        # Adicionar um atraso para evitar sobrecarga
        time.sleep(0.1)

        # Imprimir dados de SNR
        if gps.satellite_data_updated():
            print("Dados SNR dos Satélites:")
            for sv_id, sv_data in gps.satellite_data.items():
                # sv_data é uma tupla (elevação, azimute, snr)
                print(f"Satélite {sv_id}: Elevação={sv_data[0]}, Azimute={sv_data[1]}, SNR={sv_data[2]}")
            gps.unset_satellite_data_updated()

