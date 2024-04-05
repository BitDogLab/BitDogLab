import time
from machine import Pin, PWM

def chewbacca_sound():
    buzzer = PWM(Pin(21))
    
    # Iniciar com uma frequência mais alta e diminuir para simular o rugido descendente
    start_freq = 300
    end_freq = 60
    step = -5

    for freq in range(start_freq, end_freq, step):
        buzzer.freq(freq)
        buzzer.duty_u16(30000)
        time.sleep(0.01)
        buzzer.duty_u16(0)
        time.sleep(0.005)

    # Uma pequena pausa antes de repetir ou seguir
    time.sleep(0.2)

    
chewbacca_sound()


