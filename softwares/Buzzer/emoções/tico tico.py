import time
from machine import Pin, PWM

buzzer = PWM(Pin(21))

# Definição das notas básicas
C5 = 523.25
D5 = 587.33
E5 = 659.25
F5 = 698.46
G5 = 783.99
A5 = 880

# Melodia e ritmo para o trecho condensado de "Tico-Tico no Fubá"
melody = [
    E5, D5, E5, F5, E5, D5, E5, A5
]

rhythm = [
    0.1, 0.1, 0.1, 0.4, 0.1, 0.1, 0.1, 0.4  # A nota A5 tem uma duração maior para representar "lá"
]

# Função para tocar a melodia
def play_melody():
    for i in range(len(melody)):
        buzzer.freq(int(melody[i]))
        buzzer.duty_u16(32768)  # metade da faixa máxima
        time.sleep(rhythm[i])
        buzzer.duty_u16(0)
        time.sleep(0.02)  # pequena pausa entre as notas

play_melody()


