import time
from machine import Pin, PWM
import neopixel
import random

# Configuração do buzzer e NeoPixel
buzzer = PWM(Pin(21))
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

def random_color(dim_factor=1):
    """Gera uma cor aleatória."""
    return (int(random.randint(0, 255) * dim_factor), 
            int(random.randint(0, 255) * dim_factor), 
            int(random.randint(0, 255) * dim_factor))

def l3_37_sound_and_lights():
    border_heart_leds = [2, 6, 14, 15, 23, 17, 21, 19, 10, 8]
    inner_heart_leds = [7, 13, 12, 11, 16, 18]
    already_illuminated = []

    # Sequência inicial metódica
    for freq in [440, 392, 440, 392]:  # Notas: A, G
        # Acende um LED do coração de forma aleatória com cor aleatória
        random_led = random.choice([led for led in border_heart_leds + inner_heart_leds if led not in already_illuminated])
        already_illuminated.append(random_led)
        color_intensity = 0.5 if random_led in inner_heart_leds else 1  # Diminui a intensidade se for LED interno
        np[random_led] = random_color(color_intensity)
        np.write()
        
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.1)

    # Toque rebelde e imprevisível
    for freq in [587, 493, 587, 523]:  # Notas: D, B, D, C
        # Acende um LED do coração de forma aleatória com cor aleatória
        random_led = random.choice([led for led in border_heart_leds + inner_heart_leds if led not in already_illuminated])
        already_illuminated.append(random_led)
        color_intensity = 0.5 if random_led in inner_heart_leds else 1  # Diminui a intensidade se for LED interno
        np[random_led] = random_color(color_intensity)
        np.write()
        
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.15)

    # Continua acendendo os LEDs restantes do coração após a sequência
    for led in [l for l in border_heart_leds + inner_heart_leds if l not in already_illuminated]:
        color_intensity = 0.5 if led in inner_heart_leds else 1  # Diminui a intensidade se for LED interno
        np[led] = random_color(color_intensity)
        np.write()
        time.sleep(0.1)

    buzzer.duty_u16(0)  # Desliga o buzzer ao final

# Testando a função
l3_37_sound_and_lights()
