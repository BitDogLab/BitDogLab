from machine import PWM, Pin
import neopixel
import time
import random
from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C

# Configuração do OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)


def update_oled(message):
    oled.fill(0)
    oled.text(message, 25, 25)
    oled.show()

# Configurando o LED RGB
led_r = PWM(Pin(12))
led_g = PWM(Pin(13))
led_b = PWM(Pin(11))

led_r.freq(1000)
led_g.freq(1000)
led_b.freq(1000)

# Configuração do NeoPixel
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Configuração dos botões
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# definir cores para os LEDs
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuração do Buzzer
buzzer = PWM(Pin(21))
buzzer.freq(50)  # Frequência inicial grave

def gradual_light_sound(duration=2):
    step_duration = duration / 100
    for i in range(101):
        duty_cycle = (i * 65535) // 200  # Calcular o ciclo de trabalho atual

        # Ajustar o LED para a intensidade atual
        led_r.duty_u16(duty_cycle)
        led_g.duty_u16(duty_cycle)
        led_b.duty_u16(duty_cycle)

        # Ajustar a frequência do buzzer
        buzzer.freq(50 + i * 2)  # Ajustar a frequência do buzzer
        
        # Ajustar o volume do buzzer
        buzzer.duty_u16(duty_cycle // 4)  # Reduzir o volume para 25% do máximo
        
        time.sleep(step_duration)

    # Desligar o LED e o buzzer no final
    led_r.duty_u16(0)
    led_g.duty_u16(0)
    led_b.duty_u16(0)
    buzzer.duty_u16(0)

def beep(freq=1000, duration=0.2):
    ''' Toca um beep com a frequência e duração especificadas '''
    buzzer.freq(freq)
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

    
# apagar todos os LEDs
def clear_all():
    for i in range(len(np)):
        np[i] = BLACK
    np.write()

def heartbeat_effect(sequence):
    initial_delay = 0.3  # tempo inicial entre LEDs
    decrement = 0.05  # valor a ser decrementado a cada LED
    
    # Limpa todos os LEDs
    clear_all()

    for idx, led in enumerate(sequence):
        np[led] = (255, 0, 0)  # Acende o LED vermelho
        dim_leds(sequence, idx)  # Diminui o brilho dos LEDs na sequência
        np.write()
        time.sleep(initial_delay - idx * decrement)
        
    # Toca o beep no buzzer
    beep()
    
    # Aguarda um pouco e depois desliga todos os LEDs
    time.sleep(0.3)
    clear_all()

def heart():
    """Acende um coração grande na matriz de LEDs."""
    # Primeiro, desligamos todos os LEDs para garantir que começa "limpo"
    clear_all()
    
    # Lista dos LEDs que devem ser acesos para o coração
    heart_leds = [2, 6, 14, 15, 23, 17, 21, 19, 10, 8]
    
    # Acendendo os LEDs em vermelho
    for led in heart_leds:
        np[led] = (255, 0, 0)  # RED
    
    np.write()
    
# Define O CÓDIGO DE ACENDER OS LEDs DO CORAÇÃO ALEATORIAMENTE
def random_color(dim_factor=1):
    """Gera uma cor aleatória."""
    return (int(random.randint(0, 255) * dim_factor), 
            int(random.randint(0, 255) * dim_factor), 
            int(random.randint(0, 255) * dim_factor))

#efeito de som usada na piscadinha direita
def door_swish():
    for freq in range(1000, 2000, 50):
        buzzer.freq(freq)
        buzzer.duty_u16(40000)
        time.sleep(0.005)
    for freq in range(2000, 1000, -50):
        buzzer.freq(freq)
        buzzer.duty_u16(40000)
        time.sleep(0.005)
    buzzer.duty_u16(0)

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

def smile_face():
    # Definindo a sequência de cores
    colors = [
        BLACK, BLUE, BLUE, BLUE, BLACK,
        BLUE, BLACK, BLACK, BLACK, BLUE,
        BLACK, BLACK, BLACK, BLACK, BLACK,
        BLACK, CYAN, BLACK, CYAN, BLACK,
        BLACK, BLACK, BLACK, BLACK, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
def blink_right_eye():
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
    np[16] = CYAN
    np[17] = BLACK
    np[18] = BLACK
    np[19] = BLACK
    np[20] = BLACK
    np[21] = BLACK
    np[22] = BLACK
    np[23] = BLACK
    np[24] = BLACK

    np.write()
    door_swish()

    # aguardar e retorna a cor azul do olho direito
    time.sleep(.2)
    np[18] = CYAN
    np.write()
    
#define função de som sincronizada com o led da boca piscando
def colour_mouth():


    def r2d2_beep():
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
    
def triple_zero_sound():
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
    
def seta_Direita():
    np[0] = BLACK
    np[1] = BLACK
    np[2] = YELLOW
    np[3] = BLACK
    np[4] = BLACK
    np[5] = BLACK
    np[6] = BLACK
    np[7] = BLACK
    np[8] = YELLOW
    np[9] = BLACK
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
    # Desliga o buzzer ao final
    buzzer.duty_u16(0)
    
def seta_Esquerda():
    np[0] = BLACK
    np[1] = BLACK
    np[2] = YELLOW
    np[3] = BLACK
    np[4] = BLACK
    np[5] = BLACK
    np[6] = YELLOW
    np[7] = BLACK
    np[8] = BLACK
    np[9] = BLACK
    np[10] = YELLOW
    np[11] = YELLOW
    np[12] = YELLOW
    np[13] = YELLOW
    np[14] = YELLOW
    np[15] = BLACK
    np[16] = YELLOW
    np[17] = BLACK
    np[18] = BLACK
    np[19] = BLACK
    np[20] = BLACK
    np[21] = BLACK
    np[22] = YELLOW
    np[23] = BLACK
    np[24] = BLACK
    np.write()
    # Desliga o buzzer ao final
    buzzer.duty_u16(0)
    
    
def xplosion():
    # Definindo a sequência de cores
    colors = [
        BLACK, BLACK, BLACK, BLACK, BLACK,
        BLACK, BLACK, BLACK, BLACK, BLACK,
        BLACK, BLACK, RED, BLACK, BLACK,
        BLACK, BLACK, BLACK, BLACK, BLACK,
        BLACK, BLACK, BLACK, BLACK, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
    time.sleep(.1)
    
    # Som forte e abrupto
    for freq in range(2000, 50, -50):
        buzzer.freq(freq)
        buzzer.duty_u16(32767)  # 50% de duty cycle
        time.sleep(0.005)
    
    
    colors = [
        BLACK, BLACK, BLACK, BLACK, BLACK,
        BLACK, BLACK, RED, BLACK, BLACK,
        BLACK, RED, BLUE, RED, BLACK,
        BLACK, BLACK, RED, BLACK, BLACK,
        BLACK, BLACK, BLACK, BLACK, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
    time.sleep(.2)
    
        
    colors = [
        BLACK, BLACK, RED, BLACK, BLACK,
        BLACK, RED, BLUE, RED, BLACK,
        RED, BLUE, WHITE, BLUE, RED,
        BLACK, RED, BLUE, RED, BLACK,
        BLACK, BLACK, RED, BLACK, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
    time.sleep(.2)
    
    colors = [
        BLACK, RED, RED, RED, BLACK,
        RED, BLUE, WHITE, BLUE, RED,
        RED, WHITE, WHITE, WHITE, RED,
        RED, BLUE, WHITE, BLUE, RED,
        BLACK, RED, RED, RED, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
    time.sleep(.2)
    
    colors = [
        BLACK, WHITE, WHITE, WHITE, BLACK,
        WHITE, WHITE, WHITE, WHITE, WHITE,
        WHITE, WHITE, BLACK, WHITE, WHITE,
        WHITE, WHITE, WHITE, WHITE, WHITE,
        BLACK, WHITE, WHITE, WHITE, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
        
    time.sleep(.1)
    
    colors = [
        BLACK, WHITE, WHITE, WHITE, BLACK,
        WHITE, BLACK, BLACK, BLACK, WHITE,
        WHITE, BLACK, BLACK, BLACK, WHITE,
        WHITE, BLACK, BLACK, BLACK, WHITE,
        BLACK, WHITE, WHITE, WHITE, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
    time.sleep(.2)
    
    colors = [
        BLACK, WHITE, BLACK, WHITE, BLACK,
        WHITE, BLACK, BLACK, BLACK, WHITE,
        BLACK, BLACK, BLACK, BLACK, BLACK,
        WHITE, BLACK, BLACK, BLACK, WHITE,
        BLACK, WHITE, BLACK, WHITE, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
    
    clear_all()
    time.sleep(.2)
    
    colors = [
        BLACK, WHITE, BLACK, WHITE, BLACK,
        WHITE, BLACK, BLACK, BLACK, WHITE,
        BLACK, BLACK, BLACK, BLACK, BLACK,
        WHITE, BLACK, BLACK, BLACK, WHITE,
        BLACK, WHITE, BLACK, WHITE, BLACK
    ]
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    
    # Reverberações ou ecos mais suaves
    for _ in range(5):
        buzzer.duty_u16(16383)  # 25% de duty cycle
        time.sleep(0.1)
        buzzer.duty_u16(0)  # Desliga
        time.sleep(0.1)

    buzzer.duty_u16(0)  # Certifique-se de que o buzzer esteja desligado
    
        
#------------------------
clear_all()
# Chamar a função
gradual_light_sound()

# Sequência de LEDs para simular o pulso cardíaco
sequence = [14, 6, 12, 17, 21, 10]

# Especifica o número de repetições desejado
num_repetitions = 3
for _ in range(num_repetitions):
    heartbeat_effect(sequence)
    # Exibe o coração grande
    heart()
    time.sleep(0.2)

l3_37_sound_and_lights()
time.sleep(1.5)


update_oled("OLA HUMANO!")

# Primeiro, desligamos todos os LEDs para garantir que começa "limpo"
clear_all()
time.sleep(1.5)

smile_face()
time.sleep(1)

blink_right_eye()
time.sleep(1)

colour_mouth()
time.sleep(2.2)

triple_zero_sound()
time.sleep(2)

clear_all()


while True:
    seta_Esquerda()
    time.sleep(.5)
    clear_all()
    time.sleep(.2)
    seta_Esquerda()
    time.sleep(.3)
    clear_all()
    time.sleep(.3)
    seta_Esquerda()
    # Aguarde até o Botão A ser pressionado
    while button_a.value():
        time.sleep(0.1)  # Adicione um delay para debounce
    
    clear_all()
    xplosion()
    
    seta_Direita()
    # Aguarde até o Botão B ser pressionado
    while button_b.value():
        time.sleep(0.1)  # Adicione um delay para debounce
    
    clear_all()
    xplosion()



