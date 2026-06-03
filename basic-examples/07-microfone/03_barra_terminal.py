from machine import Pin, ADC
import time

mic = ADC(Pin(28))
centro = 32768

while True:
    pico = 0
    for _ in range(40):
        valor = abs(mic.read_u16() - centro)
        if valor > pico:
            pico = valor
    nivel = min(20, pico // 1200)
    print("#" * nivel)
    time.sleep_ms(120)
