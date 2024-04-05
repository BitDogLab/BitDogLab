from machine import Pin, I2C
import time
import math
from ssd1306 import SSD1306_I2C

# Definição dos pinos
pin_input = Pin(18, Pin.IN)
led_r = Pin(12, Pin.OUT)
led_g = Pin(13, Pin.OUT)
led_b = Pin(11, Pin.OUT)

WIDTH = 128
HEIGHT = 64
i2c = I2C(1, scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

def set_rgb_color(r, g, b):
    led_r.value(r)
    led_g.value(g)
    led_b.value(b)

def calculate_gravity(T, L):
    g = (4 * math.pi**2 * L) / T**2
    return g

def update_oled(L, period, g):
    oled.fill(0)
    oled.text(f"L: {L*100:.0f} cm", 0, 0)
    oled.text(f"Periodo: {period:.2f} s", 0, 25)
    oled.text(f"g: {g:.2f} m/s^2", 0, 50)
    oled.show()

L = 0.25
last_state = 0
start_time = None
pulse_count = 0

while True:
    current_state = pin_input.value()
    set_rgb_color(current_state, current_state, current_state)
    
    if current_state and not last_state:
        current_time = time.ticks_ms()
        pulse_count += 1
        
        if pulse_count == 1:
            start_time = current_time
        elif pulse_count == 3:
            period = (current_time - start_time) / 1000
            
            g = calculate_gravity(period, L)
            
            print(f"Período: {period:.2f} s")
            print(f"Aceleração da Gravidade (g) calculada: {g:.2f} m/s^2")
            
            update_oled(L, period, g)  # Atualiza o display OLED
            
            start_time = None
            pulse_count = 0
    
    last_state = current_state
    time.sleep(0.0001)

    