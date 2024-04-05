from machine import Pin, PWM
import time

def awakening():
    buzzer = PWM(Pin(21))
    
    # Começar com uma baixa frequência e aumentar lentamente
    for freq in range(200, 800, 10):
        buzzer.freq(freq)
        buzzer.duty_u16(32768)  # 50% de duty cycle
        time.sleep(0.01)
    
    # Pequena pausa
    time.sleep(0.1)
    
    # Tocar 3 tons curtos e rápidos, como um "Oi!"
    for _ in range(3):
        buzzer.freq(1000)
        buzzer.duty_u16(32768)
        time.sleep(0.05)
        buzzer.duty_u16(0)  # Silenciar
        time.sleep(0.05)

    buzzer.deinit()

awakening()
