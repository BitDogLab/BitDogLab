from machine import Pin, PWM
import time

# Configuração do Buzzer
buzzer_pin = Pin(21, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)

# Notas musicais para a música tema de Star Wars
star_wars_notes = [
    330, 330, 330, 262, 392, 523, 330, 262,
    392, 523, 330, 659, 659, 659, 698, 523,
    415, 349, 330, 262, 392, 523, 330, 262,
    392, 523, 330, 659, 659, 659, 698, 523,
    415, 349, 330, 523, 494, 440, 392, 330,
    659, 784, 659, 523, 494, 440, 392, 330,
    659, 659, 330, 784, 880, 698, 784, 659,
    523, 494, 440, 392, 659, 784, 659, 523,
    494, 440, 392, 330, 659, 523, 659, 262,
    330, 294, 247, 262, 220, 262, 330, 262,
    330, 294, 247, 262, 330, 392, 523, 440,
    349, 330, 659, 784, 659, 523, 494, 440,
    392, 659, 784, 659, 523, 494, 440, 392
]

# Tempo para cada nota (em milissegundos)
note_duration = [
    500, 500, 500, 350, 150, 300, 500, 350,
    150, 300, 500, 500, 500, 500, 350, 150,
    300, 500, 500, 350, 150, 300, 500, 350,
    150, 300, 650, 500, 150, 300, 500, 350,
    150, 300, 500, 150, 300, 500, 350, 150,
    300, 650, 500, 350, 150, 300, 500, 350,
    150, 300, 500, 500, 500, 500, 350, 150,
    300, 500, 500, 350, 150, 300, 500, 350,
    150, 300, 500, 350, 150, 300, 500, 500,
    350, 150, 300, 500, 500, 350, 150, 300,
]

# Função para tocar a música tema de Star Wars
def play_star_wars():
    for i, note in enumerate(star_wars_notes):
        if note == 0:
            buzzer_pwm.duty_u16(0)
        else:
            buzzer_pwm.freq(note)
            buzzer_pwm.duty_u16(32768)  # 50% de duty cycle
        time.sleep_ms(note_duration[i])

try:
    play_star_wars()  # Chama a função para tocar a música tema de Star Wars
finally:
    buzzer_pwm.deinit()  # Desliga o PWM do buzzer quando o programa terminar

