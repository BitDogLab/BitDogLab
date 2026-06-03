import time
from machine import UART, Pin, I2C, PWM
import neopixel
import random
from ssd1306 import SSD1306_I2C
from micropyGPS import MicropyGPS
import time

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicialização do I2C, OLED e GPS
i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
gps_module = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
gps = MicropyGPS()



# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

LED = {
    0: 24, 1: 23, 2: 22, 3: 21, 4: 20,
    5: 15, 6: 16, 7: 17, 8: 18, 9: 19,
    10: 14, 11: 13, 12: 12, 13: 11, 14: 10,
    15: 5, 16: 6, 17: 7, 18: 8, 19: 9,
    20: 4, 21: 3, 22: 2, 23: 1, 24: 0
}

# Função para acender cada LED em sequência de 0 a 24
def cycle_matrix():
    for i in range(NUM_LEDS):
        # Gerar cores aleatórias para R, G, B
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        np[LED[i]] = (r, g, b)  # Acende o LED com a cor aleatória
        np.write()  # Atualiza o estado da matriz
        time.sleep(1)  # Mantém o LED aceso por 1 segundo
        #np[LED[i]] = (0, 0, 0)  # Desliga o LED
        np.write()  # Atualiza o estado da matriz
        
        
# Função para apagar todos os LEDs
def clear_matrix():
    for i in range(NUM_LEDS):
        np[LED[i]] = (0, 0, 0)  # Desliga o LED
    np.write()  # Atualiza o estado da matriz

# Executa a função para acender os LEDs em sequência
clear_matrix()

# Função para atualizar o display OLED com a contagem regressiva para meia-noite
def update_oled_countdown():
    current_time = time.localtime()
    seconds_until_midnight = (24 - current_time[3] - 1) * 3600 + (60 - current_time[4] - 1) * 60 + (60 - current_time[5])
    hours = seconds_until_midnight // 3600
    minutes = (seconds_until_midnight % 3600) // 60
    seconds = seconds_until_midnight % 60
    countdown_text = ":\n{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    oled.fill(0)  # Limpa o display
    oled.text(countdown_text, 0, 0)  # Exibe a contagem regressiva no display
    oled.show()  # Atualiza o display
    
# Função para reconhecer meia-noite
def meia_noite_callback(p):
    current_time = time.localtime()
    if current_time[3] == 0 and current_time[4] == 0:
        # É meia-noite, execute as ações desejadas aqui
        print("É meia-noite!")
        # Executa a função
        cycle_matrix()
        for i in range(NUM_LEDS):
            np[LED[i]] = (0, 0, 0)  # Desliga o LED
    else:
        # Atualiza o display com a contagem regressiva para meia-noite
        update_oled_countdown()

# Inicialização do pino de interrupção para reconhecer meia-noite
button_a = Pin(5, Pin.IN, Pin.PULL_UP)
button_a.irq(trigger=Pin.IRQ_RISING, handler=meia_noite_callback)

# Loop principal
while True:
    meia_noite_callback(None)  # Chama a função para atualizar o display dentro do loop

