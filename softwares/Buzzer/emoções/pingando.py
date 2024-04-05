import time
from machine import Pin, PWM

BUZZER_A = Pin(21, Pin.OUT)
buzzer_pwm = PWM(BUZZER_A)
buzzer_pwm.freq(1000)  # Definir uma frequência inicial válida
buzzer_pwm.duty_u16(0)  # Amplitude inicial é 0 para ficar silencioso

def alert():
    # Frequência de alerta
    freq = 1000  # 1kHz é uma frequência comum para bips de alerta

    for _ in range(5):  # 5 bips
        buzzer_pwm.freq(freq)
        buzzer_pwm.duty_u16(4000)  # Amplitude
        time.sleep(0.1)  # Duração do bip
        buzzer_pwm.duty_u16(0)  # Silenciar entre bips
        time.sleep(0.1)  # Pausa entre bips

alert()



