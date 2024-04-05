from machine import PWM, Pin
import neopixel
import time
import random
from machine import Pin, SoftI2C, ADC
from ssd1306 import SSD1306_I2C
import math

# Configuração do OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

joystick_button = Pin(22, Pin.IN, Pin.PULL_UP) 
#______________________________________________



# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Definindo a matriz de LEDs
LED_MATRIX = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

# Inicializar ADC para os pinos VRx (GPIO26) e VRy (GPIO27)
adc_vrx = ADC(Pin(26))
adc_vry = ADC(Pin(27))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min




#_______________________________________________
def update_oled(lines):
    oled.fill(0)
    for i, line in enumerate(lines):
        oled.text(line, 0, i * 8)
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
RED = (155, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 0, 155)
YELLOW = (100, 100, 0)
MAGENTA = (155, 0, 155)
CYAN = (0, 155, 155)
WHITE = (100, 100, 100)
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
    
def star_trek_beep():
    buzzer = PWM(Pin(21))  # Buzzer A conectado ao GPIO21
    
    # Primeiro tom
    buzzer.freq(1000)
    buzzer.duty_u16(40000)
    time.sleep(0.1)
    buzzer.duty_u16(0)
    
    # Pequena pausa
    time.sleep(0.05)
    
    # Segundo tom
    buzzer.freq(1500)
    buzzer.duty_u16(40000)
    time.sleep(0.1)
    buzzer.duty_u16(0)

    # Pequena pausa
    time.sleep(0.05)

    # Terceiro tom
    buzzer.freq(2000)
    buzzer.duty_u16(40000)
    time.sleep(0.1)
    buzzer.duty_u16(0)



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
    
# Inicialização do Neopixel e ADC para o microfone
#np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_LEDS)
adc = machine.ADC(machine.Pin(28))  # GP28 para o microfone

OFFSET = int(1.65 / 3.3 * 65536)  # Valor ADC correspondente a 1,65V

# Definição dos patamares
patamares = [
    [2],
    [1, 2, 3],
    [7, 1, 2, 3],
    [12, 6, 7, 8, 0, 1, 2, 3, 4],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14, 15, 19],
    [12, 6, 7, 8, 0, 1, 2, 3, 4, 11, 13, 17, 5, 9, 22, 16, 18, 10, 14, 15, 19, 20, 21, 23, 24]
] * 2

def determinar_cor(patamar_index):
    if patamar_index < len(patamares) / 3.5:
        return (0, 0, 85)  # Azul
    else:
        return (105, 0, 0)  # Vermelho

def acender_leds(patamar_index):
    cor = determinar_cor(patamar_index)
    
    # Primeiro, desligamos todos os LEDs
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)

    # Depois, acendemos os LEDs do patamar atual
    for i in patamares[patamar_index]:
        np[i] = cor
        
    np.write()

def acender_por_valor(ratio):
    max_patamares = len(patamares)
    patamar_index = int(ratio * max_patamares)
    patamar_index = min(patamar_index, max_patamares - 1)  # Evitar índices fora da faixa

    # Se o ratio estiver abaixo de um limiar, desliga todos os LEDs
    if ratio < 0.05:
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
        np.write()
    else:
        acender_leds(patamar_index)


def vu_meter(adc_value):
    volume = max(0, (adc_value - OFFSET)*2)  # Subtrai o offset e garante que o valor seja positivo
    volume_ratio = volume / 65536.0
    normalized_ratio = math.pow(volume_ratio, 0.5)  # Ajustando a sensibilidade

    acender_por_valor(normalized_ratio)

    
        
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


#update_oled("OLA UIANES!")
messages = [
    "           ",
    "           ",
    "  OLA  UIANES!",
    "           ",
    "           ",
    "           ",
    "           ",
    "           "
]
update_oled(messages)


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


# Defina as cores que você deseja alternar
cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # vermelho, verde, azul
indice_cor = 0  # Índice da cor atual na lista de cores

while True:
    # Primeira parte: Seta esquerda e espera pelo botão A
    seta_Esquerda()
    time.sleep(.5)
    clear_all()
    time.sleep(.2)
    seta_Esquerda()
    time.sleep(.3)
    clear_all()
    time.sleep(.3)
    seta_Esquerda()
    

    
    messages = [
    "           ",
    "           ",
    "    APERTE  ",
    "           ",
    "       A     ",
    "           ",
    "           ",
    "           "
    ]
    update_oled(messages)
    
    # Aguarde até o Botão A ser pressionado
    while button_a.value():
        time.sleep(0.1)  # Adicione um delay para debounce
    
    clear_all()
    xplosion()
    
    # Segunda parte: Seta direita e espera pelo botão B
    seta_Direita()
    time.sleep(.5)
    clear_all()
    time.sleep(.2)
    seta_Direita()
    time.sleep(.3)
    clear_all()
    time.sleep(.3)
    seta_Direita()
       

    messages = [
    "           ",
    "           ",
    "    APERTE  ",
    "           ",
    "       B     ",
    "           ",
    "           ",
    "           "
    ]
    update_oled(messages)
    
    # Aguarde até o Botão B ser pressionado
    while button_b.value():
        time.sleep(0.1)  # Adicione um delay para debounce
    
    clear_all()
    xplosion()
    
    update_oled("             ")
    update_oled("Mova Joystick")
    
    messages = [
    "           ",
    " Mova Joystick ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    ]
    update_oled(messages)
    
    time.sleep(1)   
    colors = [
        GREEN, GREEN, GREEN, GREEN, BLACK,
        BLACK, GREEN, GREEN, BLACK, BLACK,
        BLACK, BLACK,  GREEN, GREEN, BLACK,
        BLACK, GREEN, BLACK, GREEN, BLACK,
        GREEN, BLACK, BLACK, GREEN, BLACK
    ]
    
    
    # Atribuindo as cores à matriz np
    for i, color in enumerate(colors):
        np[i] = color
    
    np.write()
    time.sleep(2)
    

    messages = [
    "           ",
    " Mova Joystick ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    "           ",
    ]
    update_oled(messages)
    
    # Agora entre no modo de controle do joystick
    while True:
        vrx_value = adc_vrx.read_u16()
        vry_value = adc_vry.read_u16()
    
        messages = [
            "           ",
            "           ",
            "   APERTE  ",
            "           ",
            "     B     ",
            "      para   ",
            "           ",
            "    SAIR   ",
        ]
        update_oled(messages)
    
        offsetx = 0
        offsety = 400
        row = map_value(vrx_value - offsetx, 240, 65279, 0, 4)
        col = map_value(vry_value - offsety, 65278, 240, 0, 4)
        
        for i in range(NUM_LEDS):
            np[i] = (0, 0, 0)
        
        led_index = LED_MATRIX[row][col]
        #beep(50, 4000)  # Toca um beep rápido
        np[led_index] = cores[indice_cor]  # Use a cor atual
        np.write()
        
        # Verifica se o botão do joystick está pressionado
        if not joystick_button.value():
            indice_cor = (indice_cor + 1) % len(cores)  # Atualiza o índice da cor
            star_trek_beep()
            print("Botão do joystick pressionado. Mudando a cor.")
        
        # Verifica se o botão B está pressionado
        if not button_b.value():
            print("Botão B pressionado. Saindo do modo de controle do joystick.")
            update_oled("                ")
            break  # Sai do loop se o botão B estiver pressionado
        
        time.sleep(0.1)

    
    
   

    # Aguarde até que o botão B seja liberado
    while not button_b.value():
        time.sleep(0.1)
       
    update_oled("             ")
    update_oled("Escutando")
    
    messages = [
    "  Escutando ",
    "           ",
    "   APERTE  ",
    "           ",
    "     B     ",
    "      para   ",
    "           ",
    "    SAIR     ",
    ]
    update_oled(messages)
    
      

    # Modo VU Meter 
    while True:  
        if button_b.value():
            adc_value = adc.read_u16()  # Lendo o valor do ADC do microfone
            vu_meter(adc_value)  # Atualizando o VU meter com base no valor do ADC
            time.sleep(0.02)  # Um pequeno atraso para tornar o loop manejável
        else:
            print("Botão B pressionado. Saindo do modo VU Meter.")
            break  # Sai do loop se o botão B estiver pressionado
            update_oled("             ")
            update_oled(" OLA UIANES")
                
            messages = [
            "           ",
            "           ",
            "   OLA UIANES  ",
            "           ",
            "           ",
            "           ",
            "           ",
            "           ",
            ]
            update_oled(messages)
    
            

time.sleep(0.1)