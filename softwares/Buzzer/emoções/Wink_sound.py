import time
from machine import Pin, PWM

def wink_sound():
    buzzer = PWM(Pin(21))
    
    # Sequência de notas
    melody = [1000, 1200]
    
    # Ritmo para cada nota
    tempo = [50, 50, 50, 50]  # tempo em milissegundos
    
    # Reprodução das notas
    for i in range(len(melody)):
        buzzer.freq(melody[i])
        buzzer.duty_u16(20000)
        time.sleep(tempo[i] / 1000)
        buzzer.duty_u16(0)
        time.sleep(10 / 1000)  # pausa breve entre as notas

wink_sound()


