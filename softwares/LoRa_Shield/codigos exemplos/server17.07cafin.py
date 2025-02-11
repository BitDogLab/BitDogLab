from machine import Pin, SoftI2C,PWM
from time import sleep
from ulora import LoRa, ModemConfig, SPIConfig
from ssd1306 import SSD1306_I2C
import os
import time
#configuração do OLED
i2c = SoftI2C(scl = Pin(15),sda = Pin(14))
oled = SSD1306_I2C(128,64,i2c)

#LoRa parameters
RFM95_RST = 28 # pino reset lora
RFM95_SPIBUS = SPIConfig.rp2_0 # pinagem LoRa RM95 e Pico
RFM95_CS = 17 # Chip select
RFM95_INT = 20 # DIO0
RF95_FREQ = 915.0 # Frequencia de transmissao
RF95_POW = 20 # Potencia de transmissao
CLIENT_ADDRESS = 1 # endereço cliente
SERVER_ADDRESS =2 # endereço server
#função para receber os dados da comunicação LoRa
#arquivo para salvar as informações
verde = Pin(11, Pin.OUT) # verde
azul = Pin(12, Pin.OUT) # azul
vermelho = Pin(13, Pin.OUT) #vermelho

buzzer_pin = Pin(21, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)
ex_notes = [
    330, 262, 523]
note_duration = [
    100, 100, 100]
# Função para tocar a música tema de Star Wars
def play_ex_notes():
    for i, note in enumerate(ex_notes):
        if note == 0:
            buzzer_pwm.duty_u16(0)
        else:
            buzzer_pwm.freq(note)
            buzzer_pwm.duty_u16(32768)  # 50% de duty cycle
        time.sleep_ms(note_duration[i])

try:
    play_ex_notes()  # Chama a função para tocar a música tema de Star Wars
finally:
    buzzer_pwm.deinit()  # Desliga o PWM do buzzer quando o programa terminar
    
def on_recv(payload):
    print("From: ",payload.header_from)
    print("Received: ",payload.message)
    print("RSSI: {}, SNR: {}".format(payload.rssi, payload.snr))
    #message = payload.message.decode('utf-8')
    oled.fill(0)  # Limpar oled
    oled.text(f"Testando o lora", 20, 0, 1)
    oled.text(f"From: {payload.header_from}", 0, 10, 1)
    oled.text(f"Received: {payload.message}", 0, 20, 1)
    oled.text(f"{payload.message}", 0, 30, 2)
    oled.text(f"RSSI: {payload.rssi}", 0, 40, 1)
    oled.text(f"SNR: {type(payload.message)}", 0, 50, 1)
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
        play_ex_notes()
    
    if payload.message == b'4':
        vermelho.off()
        verde.off()
        azul.off()
        
        buzzer_pwm.duty_u16(0)



# initialize radio LoRa
lora = LoRa(RFM95_SPIBUS,RFM95_INT,SERVER_ADDRESS,RFM95_CS,reset_pin = RFM95_RST,freq =RF95_FREQ, tx_power =RF95_POW,acks = True)
lora.on_recv = on_recv
lora.set_mode_rx() # modo de recebimento continuo

#Botoes
botao_a = Pin(5,Pin.IN, Pin.PULL_UP)
botao_b = Pin(6,Pin.IN, Pin.PULL_UP)


oled.text("BitDogLab",0,0,1)
oled.show()


while True:
    sleep(0.1)


