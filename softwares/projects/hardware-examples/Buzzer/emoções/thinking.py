from machine import PWM, Pin
import neopixel
import time
import random

# Configuração do NeoPixel
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Configuração do Buzzer
buzzer = PWM(Pin(21))

def play_note(note, duration):
    ''' Toca uma única nota '''
    notes = {
        'C4': 261.63,
        'D4': 293.66,
        'E4': 329.63,
        'F4': 349.23,
        'G4': 392.00,
        'A4': 440.00,
        'B4': 493.88
    }
    buzzer.freq(int(notes[note]))
    buzzer.duty_u16(5000)
    time.sleep(duration)
    buzzer.duty_u16(0)

def random_led_flash(duration):
    ''' Piscar um LED aleatório por uma duração específica '''
    led_index = random.randint(0, 24)
    np[led_index] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    np.write()
    time.sleep(duration)
    np[led_index] = (0, 0, 0)

def party_effect():
    melody = [('E4', 0.2), ('D4', 0.2), ('C4', 0.2), ('D4', 0.2), ('E4', 0.2), ('E4', 0.2), ('E4', 0.4)]
    
    for note, duration in melody:
        play_note(note, duration/2)  # Toca metade da duração da nota
        random_led_flash(duration/2)  # Pisca o LED na outra metade da duração

# Teste
party_effect()





