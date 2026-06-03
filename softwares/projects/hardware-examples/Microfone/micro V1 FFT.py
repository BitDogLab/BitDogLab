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

# Valor médio do microfone
MIC_MEAN = 32500

# Limiar de sensibilidade
SENSITIVITY = 1000


def get_amplitude():
    samples = [adc.read_u16() for _ in range(50)]
    avg_value = sum(samples) / len(samples)
    deviation = abs(avg_value - MIC_MEAN)
    return deviation

def update_leds(amplitude):
    np.fill((0, 0, 0))  # Limpa os LEDs

    if amplitude > SENSITIVITY:
        num_leds_lit = int(NUM_LEDS * (amplitude / (MIC_MEAN * 0.5)))
        for i in range(num_leds_lit):
            np[i] = (0, 255, 0)  # Cor verde

    np.write()
    
def update_leds(amplitude):
    np.fill((0, 0, 0))  # Limpa os LEDs

    if amplitude > SENSITIVITY:
        num_leds_lit = int(NUM_LEDS * (amplitude / (MIC_MEAN * 0.5)))
        num_leds_lit = min(num_leds_lit, NUM_LEDS)  # Garante que não exceda o número de LEDs

        for i in range(num_leds_lit):
            np[i] = (0, 255, 0)  # Cor verde

    np.write()

while True:
    amplitude = get_amplitude()
    update_leds(amplitude)
    time.sleep(0.1)