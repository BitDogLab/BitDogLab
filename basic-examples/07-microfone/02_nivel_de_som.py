from machine import Pin, ADC
import time

mic = ADC(Pin(28))
centro = 32768

while True:
    maior = 0
    for _ in range(40):
        valor = abs(mic.read_u16() - centro)
        if valor > maior:
            maior = valor

    # Nivel simples, so para acompanhar no terminal.
    nivel = min(10, maior // 2500)
    print("nivel:", nivel)
    time.sleep_ms(150)
