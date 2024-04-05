import time
from machine import Pin, PWM

BUZZER_A = Pin(21, Pin.OUT)
buzzer_pwm = PWM(BUZZER_A)
buzzer_pwm.freq(1000)  # Definir uma frequência inicial válida
buzzer_pwm.duty_u16(0)  # Amplitude inicial é 0 para ficar silencioso

def sad():
    # Notas da melodia (em Hz)
    D5 = 587
    C5 = 523
    A4 = 440
    G4 = 392

    melody = [D5, C5, A4, G4]
    durations = [0.25, 0.25, 0.25, 0.5]  # Cada nota dura um quarto de segundo

    for note, duration in zip(melody, durations):
        buzzer_pwm.freq(note)
        buzzer_pwm.duty_u16(3000)  # Amplitude
        time.sleep(duration)
        buzzer_pwm.duty_u16(0)  # Silenciar entre notas
        time.sleep(0.05)  # Pausa entre notas

sad()



