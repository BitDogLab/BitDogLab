from machine import Pin
import time

# Configuração do LED RGB
led_r = Pin(13, Pin.OUT)
led_g = Pin(12, Pin.OUT)
led_b = Pin(11, Pin.OUT)

def set_rgb_color(r, g, b):
    led_r.value(r)
    led_g.value(g)
    led_b.value(b)

# Função para testar o LED RGB
def test_rgb():
    print("Red ON")
    set_rgb_color(1, 0, 0)
    time.sleep(2)

    print("Green ON")
    set_rgb_color(0, 1, 0)
    time.sleep(2)
    
    print("Blue ON")
    set_rgb_color(0, 0, 1)
    time.sleep(2)
    
    print("All OFF")
    set_rgb_color(0, 0, 0)
    time.sleep(2)

# Chama a função de teste
test_rgb()
