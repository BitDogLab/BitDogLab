from machine import Pin
from machine import Pin, PWM
import time

# Configurar o pino GPIO 0 como entrada
entrada_gpio = Pin(0, Pin.IN)

# Configurar o pino do buzzer B
buzzer = PWM(Pin(21))

while True:
    # Ler o estado do GPIO 0
    estado_gpio = entrada_gpio.value()

    # Se o sinal for detectado (estado LOW), ativar o buzzer B
    if estado_gpio == 1:
        buzzer.freq(1000)
        buzzer.duty_u16(32768)
        time.sleep(0.05)
        buzzer.duty_u16(0)  # Silenciar
        time.sleep(0.05)
    else:
        buzzer.duty_u16(0)

    # Aguardar um curto período de tempo para evitar leituras rápidas
    time.sleep(0.1)