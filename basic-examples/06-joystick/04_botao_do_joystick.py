from machine import Pin
import time

botao = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    if botao.value() == 0:
        print("clicou")
    time.sleep_ms(150)
