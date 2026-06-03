import machine
import neopixel
import time
import math

# Configuração da matriz
NUM_COLS = 5
NUM_ROWS = 5
NUM_LEDS = NUM_COLS * NUM_ROWS
PIN_NUM = 7  # GPIO7 para Neopixel

# Inicialização do Neopixel e ADC para o microfone
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_LEDS)
adc = machine.ADC(machine.Pin(28))  # GP28 para o microfone

OFFSET = int(1.65 / 3.3 * 65536)  # Valor ADC correspondente a 1,65V

def get_volume_ratio(adc_value):
    volume = max(0, (adc_value - OFFSET)*2)  # Subtrai o offset e garante que o valor seja positivo
    return volume / 65536.0

def acender_leds(patamar, cor):
    for i in range(NUM_LEDS):
        if i in patamar:
            np[i] = cor
        else:
            np[i] = (0, 0, 0)  # LED desligado
    np.write()

# Aqui, sua função acender_por_valor() adaptada
def acender_por_valor(volume_ratio):
    # Converta a intensidade do volume para um valor entre 0 e 15
    index = int(volume_ratio * 15)
    index = max(0, min(index, 15))
    
    if index <= 7:
        acender_leds(patamares[index], (0, 0, 55))  # Azul
    else:
        acender_leds(patamares[index - 8], (55, 0, 0))  # Vermelho

while True:
    adc_value = adc.read_u16()
    volume_ratio = get_volume_ratio(adc_value)
    
    acender_por_valor(volume_ratio)
    
    time.sleep(0.01)

