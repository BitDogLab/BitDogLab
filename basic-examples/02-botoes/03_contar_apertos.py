from machine import Pin
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)#botao A
contador = 0
antes = 1

while True:
    agora = botao.value()
    if antes == 1 and agora == 0:
        contador += 1
        print("apertos:", contador)
        time.sleep_ms(180)
    antes = agora
