from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import time
import math

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)


# Definição dos pinos
pin_input = Pin(18, Pin.IN)     # GP18 configurado como entrada
led_r = Pin(12, Pin.OUT)        # LED vermelho
led_g = Pin(13, Pin.OUT)        # LED verde
led_b = Pin(11, Pin.OUT)        # LED azul

# Variáveis globais
last_state = 0
last_time = 0
periods = []
L = 0.25  # Comprimento do pêndulo em metros

def set_rgb_color(r, g, b):
    """Define a cor do LED RGB."""
    led_r.value(r)
    led_g.value(g)
    led_b.value(b)

def display_on_oled(message):
    oled.fill(0)
    oled.text(message, 0, 0)
    oled.show()

update_counter = 0

while True:    
    current_state = pin_input.value()
    
    # Atualiza LED RGB com base no estado de pin_input
    set_rgb_color(current_state, current_state, current_state)
    
    # Detecta transição de baixo para alto
    if current_state and not last_state:
        current_time = time.ticks_ms()
        
        # Calcula período (considerando dois sinais altos consecutivos)
        period = (current_time - last_time) / 2.0
        
        last_time = current_time
        
        # Armazena os últimos 10 períodos
        if len(periods) >= 10:
            periods.pop(0)
        periods.append(period)
    
    # Calcula a média dos períodos
    avg_period = sum(periods) / len(periods) if periods else 0
    
    # Calcula a aceleração da gravidade
    if avg_period != 0:
        g = (4 * math.pi**2 * L) / (avg_period / 1000)**2
    else:
        g = 0
    
    # Mostra o valor de g no OLED a cada 100 iterações (para evitar atualizações frequentes)
    if update_counter >= 100:
        display_on_oled("g: {:.2f} m/s^2".format(g))
        update_counter = 0
    
    last_state = current_state
    update_counter += 1
    time.sleep(0.01)  # Evita leituras muito rápidas
