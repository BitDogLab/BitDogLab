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

# Configuração dos Buzzers e músicas
buzzer_a = PWM(Pin(21))
buzzer_b = PWM(Pin(4))

def play_happy_song():
    melody = [(262, 500), (294, 500), (330, 500)]
    play_melody(melody)

def play_sad_song():
    melody = [(330, 500), (294, 500), (262, 500)]
    play_melody(melody)

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
display_numbers(user_number)

while True:
    led_num = random_neopixel_blink()
    time.sleep(0.01)

    if not button_a.value():
        display_numbers(user_number, led_num)
        time.sleep(1)  # Mostra os números por um segundo
        if user_number == led_num:
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
