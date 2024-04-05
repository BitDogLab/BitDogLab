from machine import Pin, PWM
import utime

# Duração da demonstração em segundos
DEMO_TIME = 30

# Frequência para o controle PWM
FREQUENCY = 1000

# Inicializa os pinos do LED RGB como saídas PWM
# blue = PWM(Pin(11))
red = PWM(Pin(12))
# green = PWM(Pin(13))

# Define a frequência para todos os LEDs
#blue.freq(FREQUENCY)
red.freq(FREQUENCY)
#green.freq(FREQUENCY)

# Tempo de início da demonstração
start_time = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(), start_time) < DEMO_TIME * 1000:
    # Varia a intensidade de cada cor do LED ao longo do tempo
    for i in range(0, 1024):
        #blue.duty_u16(i**2)
        red.duty_u16((1023 - i)**2)
        #green.duty_u16((i if i < 512 else 1023 - i)**2)
        utime.sleep_ms(1)

# Desliga os LEDs ao final da demonstração
blue.duty_u16(0)
red.duty_u16(0)
green.duty_u16(0)
 