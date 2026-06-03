import time
from machine import Pin, PWM

def star_trek_beep():
    buzzer = PWM(Pin(21))  # Buzzer A conectado ao GPIO21
    
    # Primeiro tom
    buzzer.freq(1000)
    buzzer.duty_u16(40000)
    time.sleep(0.1)
    buzzer.duty_u16(0)
    
    # Pequena pausa
    time.sleep(0.05)
    
    # Segundo tom
    buzzer.freq(1500)
    buzzer.duty_u16(40000)
    time.sleep(0.1)
    buzzer.duty_u16(0)

    # Pequena pausa
    time.sleep(0.05)

    # Terceiro tom
    buzzer.freq(2000)
    buzzer.duty_u16(40000)
    time.sleep(0.1)
    buzzer.duty_u16(0)

# Testar o efeito
star_trek_beep()




