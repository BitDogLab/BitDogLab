from machine import PWM, Pin
import neopixel
import time
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
    # Define o fator de diminuição de intensidade baseado no índice atual do LED
    dim_factor = 255 // (len(led_sequence) - current_index)
    for idx, led in enumerate(led_sequence):
        if idx < current_index:
            r, g, b = np[led]
            r = max(r - dim_factor, 0)
            np[led] = (r, g, b)

def turn_off_all_leds():
    ''' Desliga todos os LEDs '''
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def heartbeat_effect(sequence):
    initial_delay = 0.3  # tempo inicial entre LEDs
    decrement = 0.05  # valor a ser decrementado a cada LED
    
    # Limpa todos os LEDs
    turn_off_all_leds()

    for idx, led in enumerate(sequence):
        np[led] = (255, 0, 0)  # Acende o LED vermelho
        dim_leds(sequence, idx)  # Diminui o brilho dos LEDs na sequência
        np.write()
        time.sleep(initial_delay - idx * decrement)
        
    # Toca o beep no buzzer
    beep()
    
    # Aguarda um pouco e depois desliga todos os LEDs
    time.sleep(0.3)
    turn_off_all_leds()

def heart():
    """Acende um coração grande na matriz de LEDs."""
    # Primeiro, desligamos todos os LEDs para garantir que começa "limpo"
    turn_off_all_leds()
    
    # Lista dos LEDs que devem ser acesos para o coração
    heart_leds = [2, 6, 14, 15, 23, 17, 21, 19, 10, 8]
    
    # Acendendo os LEDs em vermelho
    for led in heart_leds:
        np[led] = (255, 0, 0)  # RED
    
    np.write()

# Sequência de LEDs para simular o pulso cardíaco
sequence = [14, 6, 12, 17, 21, 10]

# Especifica o número de repetições desejado
num_repetitions = 3
for _ in range(num_repetitions):
    heartbeat_effect(sequence)
    # Exibe o coração grande
    heart()
    time.sleep(0.2)

# AQUI COMEÇA O CÓDIGO DE ACENDER OS LEDs DO CORAÇÃO ALEATORIAMENTE
def random_color(dim_factor=1):
    """Gera uma cor aleatória."""
    return (int(random.randint(0, 255) * dim_factor), 
            int(random.randint(0, 255) * dim_factor), 
            int(random.randint(0, 255) * dim_factor))

def l3_37_sound_and_lights():
    border_heart_leds = [2, 6, 14, 15, 23, 17, 21, 19, 10, 8]
    inner_heart_leds = [7, 13, 12, 11, 16, 18]
    already_illuminated = []

    for freq in [440, 392, 440, 392]:  # Notas: A, G
        random_led = random.choice([led for led in border_heart_leds + inner_heart_leds if led not in already_illuminated])
        already_illuminated.append(random_led)
        color_intensity = 0.5 if random_led in inner_heart_leds else 1  
        np[random_led] = random_color(color_intensity)
        np.write()
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.1)

    for freq in [587, 493, 587, 523]:  # Notas: D, B, D, C
        random_led = random.choice([led for led in border_heart_leds + inner_heart_leds if led not in already_illuminated])
        already_illuminated.append(random_led)
        color_intensity = 0.5 if random_led in inner_heart_leds else 1  
        np[random_led] = random_color(color_intensity)
        np.write()
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.10)

    for led in [l for l in border_heart_leds + inner_heart_leds if l not in already_illuminated]:
        color_intensity = 0.5 if led in inner_heart_leds else 1 
        np[led] = random_color(color_intensity)
        np.write()
        time.sleep(0.1)

    buzzer.duty_u16(0)

l3_37_sound_and_lights()
