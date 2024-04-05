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
time.sleep(1.5)

# Primeiro, desligamos todos os LEDs para garantir que começa "limpo"
turn_off_all_leds()
time.sleep(1.5)

# definir cores para os LEDs
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# acender cada LED do rostinhoem uma cor diferente
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(1)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLACK
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

def door_swish():
    buzzer = PWM(Pin(21))
    
    for freq in range(1000, 2000, 50):
        buzzer.freq(freq)
        buzzer.duty_u16(40000)
        time.sleep(0.005)
    for freq in range(2000, 1000, -50):
        buzzer.freq(freq)
        buzzer.duty_u16(40000)
        time.sleep(0.005)
    buzzer.duty_u16(0)
    
# Testar o efeito
door_swish()

# aguardar 1 segundo
time.sleep(.7)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(3)

#define função de som sincronizada com o led da boca piscando
def r2d2_beep():
    buzzer = PWM(Pin(21))
    
    # Primeiro bipe
    buzzer.freq(4000)
    buzzer.duty_u16(30000)
    time.sleep(0.1)
    buzzer.duty_u16(0)
    np[2] = RED
    np.write()
    time.sleep(0.2)
    
    # Segundo bipe
    buzzer.freq(5000)
    buzzer.duty_u16(30000)
    time.sleep(0.15)
    buzzer.duty_u16(0)
    np[2] = CYAN
    np[3] = CYAN
    np[1] = CYAN
    np.write()
    time.sleep(0.2)
    
    # Terceiro bipe
    buzzer.freq(4500)
    buzzer.duty_u16(30000)
    time.sleep(0.12)
    buzzer.duty_u16(0)
    np[2] = RED
    np[3] = RED
    np[1] = RED
    np.write()
    time.sleep(0.2)


r2d2_beep()

np[2] = BLUE
np[3] = BLUE
np[1] = BLUE
np.write()

time.sleep(2.2)



def triple_zero_sound():
    buzzer = PWM(Pin(21))
    
    # Sequência inicial educada
    for freq in [440, 554, 660]:  # Notas: A, C#, E
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.1)
        
        np[16] = BLACK
        np[18] = BLACK
        np.write()

    # Transição sinistra e abrupta
    for freq in range(660, 880, 5):
        buzzer.freq(freq)
        buzzer.duty_u16(5000)
        time.sleep(0.005)
    
    # Parada súbita
    buzzer.freq(880)
    time.sleep(0.3)
    
    np[16] = CYAN 
    np[18] = CYAN
    np.write()

    # Desliga o buzzer ao final
    buzzer.duty_u16(0)

triple_zero_sound()

time.sleep(7)


# apagar todos os LEDs
for i in range(len(np)):
    np[i] = BLACK
np.write()

def seta_Direita():
    np[5] = BLACK
    np[6] = BLACK
    np[7] = BLACK
    np[8] = YELLOW
    np[9] = BLACK
    np[0] = BLACK
    np[1] = BLACK
    np[2] = YELLOW
    np[3] = BLACK
    np[4] = BLACK
    np[10] = YELLOW
    np[11] = YELLOW
    np[12] = YELLOW
    np[13] = YELLOW
    np[14] = YELLOW
    np[15] = BLACK
    np[16] = BLACK
    np[17] = BLACK
    np[18] = YELLOW
    np[19] = BLACK
    np[20] = BLACK
    np[21] = BLACK
    np[22] = YELLOW
    np[23] = BLACK
    np[24] = BLACK
    np.write()

seta_Direita()