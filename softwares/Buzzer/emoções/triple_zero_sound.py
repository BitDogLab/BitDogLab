import time
from machine import Pin, PWM, neopixel
import random

# Configuração do NeoPixel
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

def light_random_led():
    """ Acende um LED aleatório """
    # Desliga todos os LEDs
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)

    # Acende um LED aleatório
    led_index = random.randint(0, 24)
    np[led_index] = (255, 0, 0)
    np.write()

def l3_37_effect():
    buzzer = PWM(Pin(21))
    
    # Sequência inicial metódica
    for freq in [440, 392, 440, 392]:  # Notas: A, G
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        light_random_led()
        time.sleep(0.1)

    # Toque rebelde e imprevisível
    for freq in [587, 493, 587, 523]:  # Notas: D, B, D, C
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        light_random_led()
        time.sleep(0.15)
    
    # Desliga o buzzer ao final
    buzzer.duty_u16(0)

    # Desliga todos os LEDs ao final
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

# Teste
l3_37_effect()


