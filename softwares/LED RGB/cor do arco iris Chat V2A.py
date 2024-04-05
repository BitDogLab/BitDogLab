from machine import Pin, PWM
import utime

# Frequência para o controle PWM
FREQUENCY = 1000

# Cores do arco-íris (vermelho, laranja, amarelo, verde, azul, anil, violeta)
# Os valores são ajustados para um LED RGB de cátodo comum
rainbow_colors = [(1023, 0, 0), (1023, 165, 0), (1023, 1023, 0), (0, 1023, 0), (0, 0, 1023), (75, 0, 130), (238, 130, 238)]

# Inicializa os pinos do LED RGB como saídas PWM
blue = PWM(Pin(11))
red = PWM(Pin(12))
green = PWM(Pin(13))

# Define a frequência para todos os LEDs
blue.freq(FREQUENCY)
red.freq(FREQUENCY)
green.freq(FREQUENCY)

# Função para transição suave entre as cores
def transition(color_from, color_to, transition_time):
    steps = 100  # Quantidade de passos na transição
    sleep_time = transition_time / steps  # Tempo entre cada passo
    for i in range(steps):
        red.duty_u16(int(color_from[0] + i * (color_to[0] - color_from[0]) / steps))
        green.duty_u16(int(color_from[1] + i * (color_to[1] - color_from[1]) / steps))
        blue.duty_u16(int(color_from[2] + i * (color_to[2] - color_from[2]) / steps))
        utime.sleep(sleep_time)

for i in range(len(rainbow_colors)):
    # Acende a cor atual do arco-íris
    red.duty_u16(rainbow_colors[i][0])
    green.duty_u16(rainbow_colors[i][1])
    blue.duty_u16(rainbow_colors[i][2])
    utime.sleep(3)  # Mantém a cor por 3 segundos

    # Faz a transição para a próxima cor do arco-íris
    if i < len(rainbow_colors) - 1:
        transition(rainbow_colors[i], rainbow_colors[i + 1], 2)

# Desliga os LEDs ao final da demonstração
red.duty_u16(0)
green.duty_u16(0)
blue.duty_u16(0)
