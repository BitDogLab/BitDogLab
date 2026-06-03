import time
from machine import Pin, PWM

def triple_zero_sound():
    buzzer = PWM(Pin(21))
    
    # Sequência inicial educada
    for freq in [440, 554, 660]:  # Notas: A, C#, E
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.2)

    # Transição sinistra e abrupta
    for freq in range(660, 880, 5):
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.005)
    
    # Parada súbita
    buzzer.freq(880)
    time.sleep(0.3)

    # Desliga o buzzer ao final
    buzzer.duty_u16(0)



triple_zero_sound()


