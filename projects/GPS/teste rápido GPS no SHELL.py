from machine import UART, Pin
import utime

# Inicializa a UART para comunicação com o módulo GPS
# Certifique-se de que os pinos TX e RX estejam corretos
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

while True:
    if gps_module.any():
        # Lê os dados disponíveis na UART
        data = gps_module.read()
        print(data)

        # Pausa por um curto período para evitar sobrecarga do console
        utime.sleep(0.5)
