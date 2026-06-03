from machine import Pin
from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig
from ssd1306 import SSD1306_I2C
from machine import Pin, SoftI2C

verde = Pin(11, Pin.OUT) # verde
azul = Pin(12, Pin.OUT) # azul
vermelho = Pin(13, Pin.OUT) #vermelho
led_teste = Pin(15, Pin.OUT) #vermelho
# Lora Parameters
RFM95_RST = 28
RFM95_SPIBUS = SPIConfig.rp2_0
RFM95_CS = 17
RFM95_INT = 20
RF95_FREQ = 868.0
RF95_POW = 10
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)
# initialise radio
lora = LoRa(RFM95_SPIBUS, RFM95_INT, CLIENT_ADDRESS, RFM95_CS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)

azul.on()
x=0

botao_a = Pin(5, Pin.IN, Pin.PULL_UP)
botao_b = Pin(6,Pin.IN,Pin.PULL_UP)

led_teste.off()
def msg(text=''):
    lora.send_to_wait(f"{text}", SERVER_ADDRESS)
# loop and send data
while True:
    oled.fill(0)  # Limpar oled
    oled.text(f"Bit DogLab", 0, 0, 1)
    oled.text(f"Testando o lora", 0, 20, 1)
    oled.text(f"From: {SERVER_ADDRESS}", 0, 30, 1)
    oled.show()
    
    if botao_a.value() == 0:
        
        oled.text(f"CMD enviado : 3", 0, 50, 1)
        oled.show()
        msg('3')

    if botao_b.value()==0:
        
        oled.text(f"CMD enviado : 4", 0, 50, 1)
        oled.show()
        msg('4')
