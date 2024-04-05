from machine import I2C, Pin, PWM
import ssd1306
import neopixel
import time
import random

# Configuração do OLED
i2c = I2C(1, sda=Pin(14), scl=Pin(15))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configuração dos Neopixels
np = neopixel.NeoPixel(Pin(7), 25)

def welcome_message():
    oled.fill(0)  # Limpa o display
    oled.text("Ola!", 0, 0)
    oled.text("sou a BitDogLab,", 0, 10)
    oled.text(" ", 0, 20)
    oled.text("Aperte o ", 0, 30)
    oled.text("Botao B", 0, 40)
    oled.show()
    #time.sleep(5)  # Exibe a mensagem por 5 segundos
        
    # Aguarda até que um dos botões seja pressionado
    while button_a.value() and button_b.value():
        time.sleep(0.1)
    
    display_numbers(user_number)  # Volta para o display padrão após um botão ser pressionado

def random_neopixel_blink():
    led_num = random.randint(0, 24)
    np.fill((0, 0, 0))
    np[led_num] = random_rgb()
    np.write()
    return led_num + 1  # Adiciona 1 para começar a contagem em 1

def random_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Número sequencial escolhido pelo usuário
user_number = 1

def display_numbers(user_num, random_num=None):
    oled.fill(0)
    oled.text("SORTEIO MALUCO", 1, 0)
    oled.text("Escolha: " + str(user_num), 10, 18)
    if random_num:
        oled.text("Sorteio: " + str(random_num), 10, 36)
    oled.show()
    
# Configuração do LED RGB
pwm_led_r = PWM(Pin(12))
led_g = Pin(11, Pin.OUT)
led_b = Pin(13, Pin.OUT)

def set_rgb_intensity(r_intensity, g_intensity=0, b_intensity=0):
    pwm_led_r.duty_u16(int(65535 * r_intensity))  # Intensidade do vermelho com PWM
    led_g.value(g_intensity)
    led_b.value(b_intensity)
    
def set_rgb_violet(state):
    """Define o LED RGB para a cor violeta ou o desliga."""
    if state:
        pwm_led_r.duty_u16(65535)  # Ligar vermelho
        led_g.value(0)             # Desligar verde
        led_b.value(10000)             # Ligar azul
    else:
        pwm_led_r.duty_u16(0)      # Desligar vermelho
        led_g.value(0)             # Desligar verde
        led_b.value(0)             # Desligar azul

# Define a intensidade padrão e aumentada
DEFAULT_INTENSITY = int(0.015 * 65535)  # Cerca de 1.5% do valor máximo
INCREASED_INTENSITY = int(DEFAULT_INTENSITY * 1.25)  # 25% a mais  

# Configuração dos Buzzers e músicas
buzzer_a = PWM(Pin(21))
buzzer_b = PWM(Pin(4))

def play_happy_song():
    
  # Melodia e ritmo propostos
    melody = [(262, 100), (294, 100), (330, 100), (349, 100),
              (392, 100), (440, 100), (494, 100), (523, 100),
              (494, 100), (440, 100), (392, 200)]

    for i, note in enumerate(melody):
        freq, duration = note

        # Piscar o LED RGB na cor violeta a cada nota
        set_rgb_violet(True)
        
        if i % 3 == 0:  # Se a nota estiver na posição múltipla de 3, toque nos dois buzzers
            buzzer_a.freq(freq)
            buzzer_b.freq(freq)
            buzzer_a.duty_u16(INCREASED_INTENSITY)
            buzzer_b.duty_u16(INCREASED_INTENSITY)
        elif i % 2 == 0:  # Se a nota estiver na posição par, toque no buzzer A
            buzzer_a.freq(freq)
            buzzer_a.duty_u16(INCREASED_INTENSITY)
            buzzer_b.duty_u16(0)
        else:  # Se a nota estiver na posição ímpar, toque no buzzer B
            buzzer_b.freq(freq)
            buzzer_b.duty_u16(INCREASED_INTENSITY)
            buzzer_a.duty_u16(0)
            
        time.sleep_ms(duration)

        # Desligar ambos os buzzers e o LED após cada nota
        buzzer_a.duty_u16(0)
        buzzer_b.duty_u16(0)
        set_rgb_violet(False)
        
        time.sleep_ms(50)  # Uma pequena pausa entre as notas para clareza
 
    
    
    play_melody(melody)

def play_sad_song():
    melody = [(330, 500), (294, 500), (262, 500)]
    intensities = [0.8, 0.3, 0.02]  # Intensidades de 100%, 50% e 25%

    for i, note in enumerate(melody):
        # Define a intensidade do LED RGB de acordo com a nota
        set_rgb_intensity(intensities[i])
        buzzer_a.freq(note[0])
        buzzer_b.freq(note[0])
        buzzer_a.duty_u16(1000)
        buzzer_b.duty_u16(1000)
        time.sleep_ms(note[1])
        buzzer_a.duty_u16(0)
        buzzer_b.duty_u16(0)
        set_rgb_intensity(0)  # Desliga o LED após cada nota
        time.sleep_ms(100)
        
def play_melody(melody):
    for note in melody:
        buzzer_a.freq(note[0])
        buzzer_b.freq(note[0])
        buzzer_a.duty_u16(1000)
        buzzer_b.duty_u16(1000)
        time.sleep_ms(note[1])
        buzzer_a.duty_u16(0)
        buzzer_b.duty_u16(0)
        time.sleep_ms(200)

# Configuração dos botões
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Início do Programa
welcome_message()

while button_a.value() and button_b.value():
        time.sleep(0.1)  # Adiciona um pequeno delay para não sobrecarregar o loop
        ###
        
while True: 
    
    
    led_num = random_neopixel_blink()
    time.sleep(0.01)

    if not button_a.value():
        display_numbers(user_number, led_num)
        time.sleep(1)  # Mostra os números por um segundo
        #if user_number == led_num:   #Pode ser comentado apenas para teste da rotida ne acerto
        if user_number == user_number: #Pode ser ativado para teste da rotina de acerto
            
            play_happy_song()
        else:
            play_sad_song()
            user_number = 1  # Reinicia a contagem
            display_numbers(user_number)

    if not button_b.value():
        user_number += 1
        if user_number > 25:  # Se o user_number exceder 25, redefina para 1
            user_number = 1
        display_numbers(user_number)
        time.sleep(0.1)  # Evita que o botão seja lido várias vezes
