import time
from machine import Pin, PWM

BUZZER_A = Pin(21, Pin.OUT)
buzzer_pwm = PWM(BUZZER_A)
buzzer_pwm.freq(10)  # Inicialmente, desligado

def sleeping():
    durations = [0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2]
    frequencies = [440, 415, 392, 370, 349, 329, 311]

    for freq, dur in zip(frequencies, durations):
        buzzer_pwm.freq(freq)
        buzzer_pwm.duty_u16(2000)  # Amplitude
        time.sleep(dur)
        
        # Diminuir a amplitude gradualmente
        for i in range(2000, 0, -200):
            buzzer_pwm.duty_u16(i)
            time.sleep(0.02)

    buzzer_pwm.duty_u16(0)  # Silencia o buzzer no final

sleeping()

