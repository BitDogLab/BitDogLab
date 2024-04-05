import time
from machine import Pin, PWM

def red_alert():
    buzzer = PWM(Pin(21))
    
    for _ in range(3):  # Repita o padrão três vezes
        buzzer.freq(600)
        buzzer.duty_u16(40000)
        time.sleep(0.3)
        buzzer.duty_u16(0)
        time.sleep(0.2)

    
# Testar o efeito
red_alert()





