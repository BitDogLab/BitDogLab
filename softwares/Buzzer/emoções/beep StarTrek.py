import time
from machine import Pin, PWM

def door_swish():
    buzzer = PWM(Pin(21))
    
    for freq in range(1000, 2000, 50):
        buzzer.freq(freq)
        buzzer.duty_u16(40000)
        time.sleep(0.005)
    for freq in range(2000, 1000, -50):
        buzzer.freq(freq)
        buzzer.duty_u16(40000)
        time.sleep(0.005)
    buzzer.duty_u16(0)
    
# Testar o efeito
door_swish()





