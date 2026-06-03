from machine import Pin, PWM

botao = Pin(5, Pin.IN, Pin.PULL_UP)#botao A
led = PWM(Pin(13), freq=1000)

while True:
    led.duty_u16(65535 if botao.value() == 0 else 0)
