from machine import Pin, PWM
import utime

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

# Inicializa os buzzers como saídas PWM
buzzer1 = PWM(Pin(4))
buzzer2 = PWM(Pin(5))

# Frequência inicial para os buzzers
frequency = 440

# Tempo de início do teste
start_time = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(), start_time) < 20 * 1000:
    # Faz o buzzer1 emitir um som
    buzzer1.freq(frequency)
    buzzer1.duty_u16(32768)  # 50% de duty cycle

    # Acende o LED RGB na cor ciano (verde e azul)
    red.duty_u16(0)
    green.duty_u16(1023)
    blue.duty_u16(1023)

    utime.sleep_ms(200)

    # Silencia o buzzer1 e desliga o LED RGB
    buzzer1.duty_u16(0)
    red.duty_u16(0)
    green.duty_u16(0)
    blue.duty_u16(0)

    # Faz o buzzer2 emitir um som
    buzzer2.freq(frequency)
    buzzer2.duty_u16(32768)  # 50% de duty cycle

    # Acende o LED RGB na cor vermelha
    red.duty_u16(1023)
    green.duty_u16(0)
    blue.duty_u16(0)

    utime.sleep_ms(200)

    # Silencia o buzzer2 e desliga o LED RGB
    buzzer2.duty_u16(0)
    red.duty_u16(0)
    green.duty_u16(0)
    blue.duty_u16(0)

    # Aumenta a frequência para o próximo ciclo
    frequency += 100

