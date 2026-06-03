import time
from machine import Pin, PWM

def chewbacca_sound():
    buzzer = PWM(Pin(21))
    buzzer = PWM(Pin(8))

    # Uma sequência de frequências para simular o rugido
    freq_sequence = [300, 280, 260, 250, 240, 230, 220, 210, 180, 160, 140, 120, 100, 80, 60]
    duty_sequence = [5000, 10000, 15000, 20000, 25000, 30000, 25000, 20000, 15000, 10000, 5000, 3000, 2000, 1000, 500]

    for freq, duty in zip(freq_sequence, duty_sequence):
        buzzer.freq(freq)
        buzzer.duty_u16(duty)
        time.sleep(0.03)
        
    # Desligar o buzzer ao final
    buzzer.duty_u16(0)

    # Uma pequena pausa antes de repetir ou seguir
    time.sleep(0.2)


    
chewbacca_sound()


