from machine import Pin, ADC
import time
import math

# Definição dos pinos
pin_input = Pin(18, Pin.IN) #define variável para o sinal de entrada do sensor de proximidade
led_r = Pin(12, Pin.OUT) #sinal do LED
led_g = Pin(13, Pin.OUT)
led_b = Pin(11, Pin.OUT)

"""Define função a cor do LED RGB."""
def set_rgb_color(r, g, b):
    led_r.value(r)
    led_g.value(g)
    led_b.value(b)
    
"""Define função para cáculo da aceleração da gravidade."""
def calculate_gravity(T, L):
    """Calcula a aceleração da gravidade com base no período e comprimento."""
    g = (4 * math.pi**2 * L) / T**2
    return g

# Solicita ao usuário o comprimento do pêndulo
L_cm = float(input("Digite o comprimento do pêndulo em cm: "))
L = L_cm / 100  # Converte para metros

#zera os contadores
last_state = 0
start_time = None
pulse_count = 0

while True:
    current_state = pin_input.value()
    
    # Atualiza LED RGB com base no estado de pin_input
    set_rgb_color(current_state, current_state, current_state)
    
    # Detecta transição de baixo para alto
    if current_state and not last_state:
        current_time = time.ticks_ms()
        pulse_count += 1
        
        if pulse_count == 1:
            # Captura o tempo do primeiro pulso
            start_time = current_time
        elif pulse_count == 3:
            # Calcula o período com base no tempo do primeiro pulso e do terceiro pulso
            period = (current_time - start_time) / 1000
            print(f"Período: {period:.2f} s")
            
            # Cálculo da aceleração da gravidade
            g = calculate_gravity(period, L)
            print(f"Aceleração da Gravidade (g) calculada: {g:.2f} m/s^2")
            
            start_time = None  # Reseta para capturar o próximo período completo
            pulse_count = 0  # Reseta a contagem de pulsos
    
    last_state = current_state
    time.sleep(0.0001)  # Evita leituras muito rápidas


    