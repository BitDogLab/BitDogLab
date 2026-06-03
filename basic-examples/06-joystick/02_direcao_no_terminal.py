from machine import Pin, ADC
import time

x = ADC(Pin(27))
y = ADC(Pin(26))

while True:
    vx = x.read_u16()
    vy = y.read_u16()
    # Na BitDogLab este joystick fica invertido nesses eixos.
    if vx < 20000:
        print("direita")
    elif vx > 45000:
        print("esquerda")
    elif vy < 20000:
        print("cima")
    elif vy > 45000:
        print("baixo")
    else:
        print("centro")
    time.sleep_ms(250)
