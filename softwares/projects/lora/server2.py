from machine import Pin, SoftI2C
from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig
from ssd1306 import SSD1306_I2C

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Led
verde = Pin(11, Pin.OUT) # verde
azul = Pin(12, Pin.OUT) # azul
vermelho = Pin(13, Pin.OUT) #vermelho

botao_a = Pin(5, Pin.IN, Pin.PULL_UP)
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)

# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

    oled.fill(0)  # Limpar oled
    oled.text(f"Testando o lora", 20, 0, 1)
    oled.text(f"From: {payload.header_from}", 0, 10, 1)
    oled.text(f"Received: {payload.message}", 0, 20, 1)
    oled.text(f"{payload.message}", 0, 30, 2)
    oled.text(f"RSSI: {payload.rssi}", 0, 40, 1)
    oled.text(f"SNR: {type(payload.message)}", 0, 50, 1)
    # oled.text(f"{time.gmtime()[0:3]}", 0, 30, 1)
    # oled.text(f"{time.gmtime()[3:7]}", 0, 50, 1)
    oled.show()

    if payload.message == b'1':
        vermelho.on()
        verde.off()
        azul.off()

    if payload.message == b'2':
        vermelho.off()
        verde.on()
        azul.off()
    
    if payload.message == b'3':
        vermelho.off()
        verde.off()
        azul.on()
    
    if payload.message == b'4':
        vermelho.off()
        verde.off()
        azul.off()
    
    if payload.message == b'5':
        vermelho.toggle()
        verde.off()
        azul.off()

# Lora Parameters
RFM95_RST = 28
RFM95_SPIBUS = SPIConfig.rp2_0
RFM95_CS = 17
RFM95_INT = 20
RF95_FREQ = 868.0
RF95_POW = 14
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(RFM95_SPIBUS, RFM95_INT, SERVER_ADDRESS, RFM95_CS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)

# set callback
lora.on_recv = on_recv

# set to listen continuously
lora.set_mode_rx()
verde.on()
# loop and wait for data
while True:
    sleep(0.1)
