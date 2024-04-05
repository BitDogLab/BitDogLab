import time
from machine import Pin, PWM

def bt1_sound():
    buzzer = PWM(Pin(21))
    
    # Inicia com uma sequência de tons crescentes
    for freq in range(200, 1000, 100):
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.03)
        
    # Um "bip" agudo para acentuar
    buzzer.freq(3000)
    buzzer.duty_u16(5000)
    time.sleep(0.1)
    
    # Diminui a frequência para um tom mais grave
    for freq in range(1000, 200, -100):
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.03)

    # Desliga o buzzer ao final
    buzzer.duty_u16(0)



bt1_sound()


