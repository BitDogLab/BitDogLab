from machine import Pin, ADC
import time

# Microfone analogico no GPIO28.
mic = ADC(Pin(28))

while True:
    print(mic.read_u16())
    time.sleep_ms(100)
