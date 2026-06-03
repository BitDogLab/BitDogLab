from machine import Pin
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)#Botao A

while True:
    print("A apertado" if botao.value() == 0 else "A solto")
    time.sleep_ms(300)
