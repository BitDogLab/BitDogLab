from machine import Pin, PWM

botao = Pin(5, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(21))
buzzer.freq(900)

while True:
    buzzer.duty_u16(9000 if botao.value() == 0 else 0)
