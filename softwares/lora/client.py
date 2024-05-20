from machine import Pin
from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig

verde = Pin(11, Pin.OUT) # verde
azul = Pin(12, Pin.OUT) # azul
vermelho = Pin(13, Pin.OUT) #vermelho

# Lora Parameters
RFM95_RST = 28
RFM95_SPIBUS = SPIConfig.rp2_0
RFM95_CS = 17
RFM95_INT = 20
RF95_FREQ = 868.0
RF95_POW = 10
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(RFM95_SPIBUS, RFM95_INT, CLIENT_ADDRESS, RFM95_CS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)

azul.on()
x=0

def msg(text=''):
    lora.send_to_wait(f"{text}", SERVER_ADDRESS)
# loop and send data
# while True:
#     x = msg('oii2', x)
#     sleep(10)
    
