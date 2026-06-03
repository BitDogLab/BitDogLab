import time
from machine import Pin, PWM

def phaser():
    buzzer = PWM(Pin(21))
    
    for freq in range(1000, 3000, 50):
        buzzer.freq(freq)
        buzzer.duty_u16(40000)
        time.sleep(0.005)
    buzzer.duty_u16(0)

    
# Testar o efeito
phaser()





