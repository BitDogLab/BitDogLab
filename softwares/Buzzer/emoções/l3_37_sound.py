import time
from machine import Pin, PWM

def millennium_falcon_sound():
    buzzer = PWM(Pin(21))
    
    # Começa com um zumbido baixo como os motores ligando
    for freq in range(100, 300, 10):
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.01)
    
    # Aumenta a frequência abruptamente para simular o pulo para o hiperespaço
    for freq in range(300, 1500, 50):
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.01)
    
    # Desliga o buzzer ao final
    buzzer.duty_u16(0)



millennium_falcon_sound()


