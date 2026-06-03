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

def color_gradient(percentage):
    if percentage < 0.5:
        # De azul para verde
        r = 0
        g = int(510 * percentage)
        b = 255 - g
    else:
        # De verde para vermelho
        g = 255 - int(510 * (percentage - 0.5))
        r = 255 - g
        b = 0
    return (r, g, b)

def set_pixel(x, y, r, g, b):
    index = (NUM_ROWS - 1 - y) * NUM_COLS + x
    np[index] = (r, g, b)

def update_display():
    np.write()

def vu_meter(adc_value, last_value):
    volume = max(0, (adc_value - OFFSET)*2)  # Subtrai o offset e garante que o valor seja positivo
    volume_ratio = volume / 65536.0
    num_leds_lit = int(NUM_LEDS * (math.log10(1 + 9 * volume_ratio)))
    
    if num_leds_lit != last_value:
        np.fill((0, 0, 0))
        for i in range(num_leds_lit):
            x = i % NUM_COLS
            y = i // NUM_COLS
            r, g, b = color_gradient(i / (NUM_LEDS - 1))
            set_pixel(x, y, r, g, b)
        update_display()
    
    return num_leds_lit

last_value = 0
while True:
    adc_value = adc.read_u16()
    last_value = vu_meter(adc_value, last_value)
    time.sleep(0.01)
