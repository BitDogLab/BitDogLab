from machine import Pin, PWM
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)
led = PWM(Pin(13), freq=1000)
ligado = False
antes = 1

while True:
    agora = botao.value()
    if antes == 1 and agora == 0:
        ligado = not ligado
        led.duty_u16(65535 if ligado else 0)
        time.sleep_ms(200)
    antes = agora
