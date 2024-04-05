import time
from machine import Pin, PWM

def bb8_sound():
    buzzer = PWM(Pin(21))
    
    # Sequência de notas
    melody = [600, 1200, 900, 1100, 700, 1300, 800]
    
    # Ritmo para cada nota
    tempo = [70, 100, 80, 60, 90, 50, 80]  # tempo em milissegundos
    
    # Reprodução das notas
    for i in range(len(melody)):
        buzzer.freq(melody[i])
        buzzer.duty_u16(30000)
        time.sleep(tempo[i] / 1000)
        buzzer.duty_u16(0)
        time.sleep(30 / 1000)  # pausa breve entre as notas
    
bb8_sound()


