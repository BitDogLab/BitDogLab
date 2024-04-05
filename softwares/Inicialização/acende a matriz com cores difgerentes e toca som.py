import time
from machine import Pin, PWM
import neopixel
import random

# Configuração do buzzer e NeoPixel
buzzer = PWM(Pin(21))
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

def random_color():
    """Gera uma cor aleatória."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def l3_37_sound_and_lights():
    specific_leds = [7, 13, 12, 11, 16, 18]

    # Sequência inicial metódica
    for freq in [440, 392, 440, 392]:  # Notas: A, G
        # Acende um LED específico aleatório com cor aleatória
        random_led = random.choice(specific_leds)
        np[random_led] = random_color()
        np.write()
        
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.1)
        
        np[random_led] = (0, 0, 0)  # Apaga o LED
        np.write()

    # Toque rebelde e imprevisível
    for freq in [587, 493, 587, 523]:  # Notas: D, B, D, C
        # Acende um LED específico aleatório com cor aleatória
        random_led = random.choice(specific_leds)
        np[random_led] = random_color()
        np.write()
        
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.15)
        
        np[random_led] = (0, 0, 0)  # Apaga o LED
        np.write()

    buzzer.duty_u16(0)  # Desliga o buzzer ao final

# Testando a função
l3_37_sound_and_lights()


