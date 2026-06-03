from machine import Pin
import time

botao_c = Pin(10, Pin.IN, Pin.PULL_UP)

while True:
    if botao_c.value() == 0:
        print("Botao C")
    time.sleep_ms(150)
