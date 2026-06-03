import time
from machine import PWM, Pin
import neopixel
import random

# Configuração do NeoPixel
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Configuração do Buzzer
buzzer = PWM(Pin(21))
buzzer_freq = 1000  # Frequência para o beep

def beep(duration=0.2):
    ''' Toca um beep com a duração especificada '''
    buzzer.freq(buzzer_freq)
    buzzer.duty_u16(5000)  # Intensidade média
    time.sleep(duration)
    buzzer.duty_u16(0)  # Desliga o buzzer

def dim_leds(led_sequence, current_index):
    dim_factor = 255 // (len(led_sequence) - current_index)
    for idx, led in enumerate(led_sequence):
        if idx < current_index:
            r, g, b = np[led]
            r = max(r - dim_factor, 0)
            np[led] = (r, g, b)

def turn_off_all_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def heartbeat_effect():
    sequence = [14, 6, 12, 21, 10]
    initial_delay = 0.3
    decrement = 0.05
    turn_off_all_leds()

    for idx, led in enumerate(sequence):
        np[led] = (255, 0, 0)
        dim_leds(sequence, idx)
        np.write()
        time.sleep(initial_delay - idx * decrement)

    beep()
    time.sleep(0.5)
    turn_off_all_leds()

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def l3_37_sound_and_lights():
    for freq in [440, 392, 440, 392]:
        random_led = random.randint(0, NUM_LEDS - 1)
        np[random_led] = random_color()
        np.write()
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.1)
        np[random_led] = (0, 0, 0)
        np.write()

    for freq in [587, 493, 587, 523]:
        random_led = random.randint(0, NUM_LEDS - 1)
        np[random_led] = random_color()
        np.write()
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.15)
        np[random_led] = (0, 0, 0)
        np.write()

    buzzer.duty_u16(0)

# Executando as funções
num_repetitions = 5
for _ in range(num_repetitions):
    heartbeat_effect()

l3_37_sound_and_lights()

