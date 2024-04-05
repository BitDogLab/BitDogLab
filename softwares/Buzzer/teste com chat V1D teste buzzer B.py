from machine import Pin, PWM
import utime

# Configura os pinos dos botões como entradas com resistores de pull-up internos
button_A = Pin(5, Pin.IN, Pin.PULL_UP)
button_B = Pin(6, Pin.IN, Pin.PULL_UP)

# Configura os pinos dos LEDs como saídas PWM
red = PWM(Pin(12))
green = PWM(Pin(13))
blue = PWM(Pin(11))

# Configura os pinos dos buzzers como saídas PWM
buzzer1 = PWM(Pin(4))
buzzer2 = PWM(Pin(21))

# Frequência para os LEDs e buzzers
FREQUENCY = 1000

# Define a frequência para todos os LEDs e buzzers
red.freq(FREQUENCY)
green.freq(FREQUENCY)
blue.freq(FREQUENCY)
buzzer1.freq(FREQUENCY)
buzzer2.freq(FREQUENCY)

while True:
    if not button_A.value():  # Botão A pressionado
        # Muda o LED para vermelho e toca o buzzer 1
        red.duty_u16(65025)
        green.duty_u16(0)
        blue.duty_u16(0)
        buzzer1.duty_u16(32768)
        utime.sleep(0.2)  # Debouncing
        buzzer1.duty_u16(0)  # Silencia o buzzer 1

    if not button_B.value():  # Botão B pressionado
        # Muda o LED para azul e toca o buzzer 2
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(65025)
        buzzer2.duty_u16(32768)
        utime.sleep(0.2)  # Debouncing
        buzzer2.duty_u16(0)  # Silencia o buzzer 2






