from machine import PWM, Pin
import time

def awakening_sound():
    buzzer = PWM(Pin(21))
    
    # Definimos frequências e durações para cada tom
    frequencies = [300, 600, 1200]
    durations = [0.5, 0.4, 0.3]
    
    for freq, duration in zip(frequencies, durations):
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(duration)
        buzzer.duty_u16(0)  # Desliga o buzzer
        time.sleep(0.1)     # Pequena pausa entre os tons
    
    buzzer.deinit()  # Desativa o buzzer no final

# Teste
awakening_sound()
