import time
from machine import Pin, PWM

BUZZER_A = Pin(21, Pin.OUT)
buzzer_pwm = PWM(BUZZER_A)
buzzer_pwm.freq(1000)  # Definir uma frequência inicial válida
buzzer_pwm.duty_u16(0)  # Amplitude inicial é 0 para ficar silencioso

def thinking():
    start_freq = 400  # Frequência de partida
    end_freq = 800  # Frequência final
    step = 50  # Quanto aumentar a cada etapa
    duration = 0.05  # Duração de cada tom

    # Ascendendo
    for freq in range(start_freq, end_freq, step):
        buzzer_pwm.freq(freq)
        buzzer_pwm.duty_u16(5000)  # Definir amplitude
        time.sleep(duration)

    # Descendendo
    for freq in range(end_freq, start_freq, -step):
        buzzer_pwm.freq(freq)
        buzzer_pwm.duty_u16(5000)  # Definir amplitude
        time.sleep(duration)

    buzzer_pwm.duty_u16(0)  # Desligar o buzzer no final

thinking()






