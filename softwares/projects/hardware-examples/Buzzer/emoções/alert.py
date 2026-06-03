import time
from machine import Pin, PWM

def r2d2_beep():
    buzzer = PWM(Pin(21))
    
    # Primeiro bipe
    buzzer.freq(4000)
    buzzer.duty_u16(30000)
    time.sleep(0.1)
    buzzer.duty_u16(0)
    time.sleep(0.1)
    
    # Segundo bipe
    buzzer.freq(5000)
    buzzer.duty_u16(30000)
    time.sleep(0.15)
    buzzer.duty_u16(0)
    time.sleep(0.1)
    
    # Terceiro bipe
    buzzer.freq(4500)
    buzzer.duty_u16(30000)
    time.sleep(0.12)
    buzzer.duty_u16(0)


r2d2_beep()


