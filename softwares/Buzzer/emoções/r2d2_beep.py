import time
from machine import Pin, PWM

def imperial_march():
    buzzer = PWM(Pin(21))
    
    # Definição das notas
    a, f, cH, eH, gS, gHS, b, cHS, fHS, fH, gH = 440, 349, 523, 659, 415, 830, 466, 554, 740, 698, 784
    eHS, aH, aHS, dHS, dH, b = 622, 880, 1244, 1244, 587, 466
    gHS, gH, dHS = 830, 784, 622
    r = 0  # r significa pausa
    
    # Sequência de notas
    melody = [
        a, eH, a,
        eH, fH, cHS, a, b, eH, gHS, gH, eH,
        r, fHS, fH, cHS, a, b, eH, a, aH,
        eH, eH, eH, fH, cHS, a, b, eH, gHS, gH, eH,
        r, fHS, fH, cHS, eH, dHS, dHS, dH,
        cHS, b, a, gHS, aH, a, gHS, a,
        r, dHS, fHS, fH, cHS, eH, dHS, dHS, dH,
        cHS, b, a, a, gHS, aH, a, gHS, a
    ]
    
    # Ritmo para cada nota
    tempo = [
        500, 500, 500,
        350, 150, 500, 350, 150, 500, 150, 500,
        500, 500, 500, 350, 150, 500, 350, 150, 650,
        500, 500, 500, 150, 500, 350, 150, 500, 150, 500,
        500, 500, 500, 350, 150, 500, 350, 150, 650,
        500, 500, 500, 150, 500, 350, 150, 500, 150, 500,
        650, 500, 500, 500, 150, 500, 350, 150, 500,
        150, 500, 500, 500, 500, 500, 500, 500, 500
    ]
    
    # Reprodução das notas
    for i in range(len(melody)):
        if melody[i] != r:
            buzzer.freq(melody[i])
            buzzer.duty_u16(30000)
        time.sleep(tempo[i] / 1000)
        buzzer.duty_u16(0)
        time.sleep(50 / 1000)  # pausa breve entre as notas



imperial_march()


