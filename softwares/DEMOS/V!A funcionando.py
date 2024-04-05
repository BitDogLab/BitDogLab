from machine import I2C, Pin, PWM
import ssd1306
import neopixel
import time
import random

# Configuração do OLED
i2c = I2C(1, sda=Pin(14), scl=Pin(15))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def display_message():
    oled.fill(0)
    oled.text("Bem vindo ao", 0, 20)
    oled.text("BitDogLab!", 20, 36)
    oled.show()

# Configuração dos Neopixels
np = neopixel.NeoPixel(Pin(7), 25) 

def random_neopixel_blink():
    np.fill((0, 0, 0))
    np[random.randint(0, 24)] = random_rgb()
    np.write()

def random_rgb():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Configuração do LED RGB
led_r = Pin(12, Pin.OUT)
led_g = Pin(13, Pin.OUT)
led_b = Pin(11, Pin.OUT)

def led_rgb_on():
    led_r.value(1)
    led_g.value(1)
    led_b.value(1)

def led_rgb_off():
    led_r.value(0)
    led_g.value(0)
    led_b.value(0)

# Configuração dos Buzzers
buzzer_a = PWM(Pin(21))
buzzer_b = PWM(Pin(4))

# Melodia mais suave
def play_melody():
    melody = [(262, 700), (294, 700), (330, 700)]  # Dó, Ré, Mi

    for note in melody:
        if not button_b.value():  # Se o botão B for pressionado, interrompe a melodia
            break
        buzzer_a.freq(note[0])
        buzzer_b.freq(note[0])
        buzzer_a.duty_u16(1000)
        buzzer_b.duty_u16(1000)
        led_rgb_on()
        time.sleep_ms(note[1])
        buzzer_a.duty_u16(0)
        buzzer_b.duty_u16(0)
        led_rgb_off()
        time.sleep_ms(200)  # Aumento do intervalo entre as notas

# Configuração dos botões
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Início do Programa
display_message()
while True:
    random_neopixel_blink()
    
    # Toca a melodia se o botão A for pressionado
    if not button_a.value(): 
        play_melody()

