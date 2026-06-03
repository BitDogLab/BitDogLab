from machine import Pin
import time

botao = Pin(22, Pin.IN, Pin.PULL_UP) #botao do joystick

while True:
    print("joystick pressionado" if botao.value() == 0 else "joystick solto")
    time.sleep_ms(300)
