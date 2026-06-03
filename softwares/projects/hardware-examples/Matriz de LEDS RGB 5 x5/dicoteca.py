from machine import Pin, PWM
import utime
import urandom

# Frequência para o controle PWM
FREQUENCY = 1000

# Inicializa os pinos do LED RGB como saídas PWM
blue = PWM(Pin(11))
red = PWM(Pin(12))
green = PWM(Pin(13))

# Define a frequência para todos os LEDs
blue.freq(FREQUENCY)
red.freq(FREQUENCY)
green.freq(FREQUENCY)

# Tempo de início da "discoteca"
start_time = utime.ticks_ms()

# Função para gerar uma cor aleatória
def random_color():
    return (urandom.randint(0, 1023), urandom.randint(0, 1023), urandom.randint(0, 1023))

while utime.ticks_diff(utime.ticks_ms(), start_time) < 30 * 1000:
    # Gera uma cor aleatória
    color = random_color()

    # Ajusta os LEDs para a cor aleatória
    red.duty_u16(color[0])
    green.duty_u16(color[1])
    blue.duty_u16(color[2])

    # Aguarda um pouco antes de mudar para a próxima cor
    utime.sleep_ms(100)

# Desliga os LEDs ao final da "discoteca"
red.duty_u16(0)
green.duty_u16(0)
blue.duty_u16(0)
