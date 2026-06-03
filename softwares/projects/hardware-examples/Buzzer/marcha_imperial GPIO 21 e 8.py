from machine import Pin, PWM
import time


# Configuração dos pinos dos buzzers
buzzer_A_pin = 21
buzzer_B_pin = 8  # Ajuste conforme sua configuração

# Inicialização dos buzzers como saídas PWM
buzzer_A = PWM(Pin(buzzer_A_pin))
buzzer_B = PWM(Pin(buzzer_B_pin))

# Função para tocar uma nota, com verificação de frequência
def tocar_nota(buzzer, frequencia, duracao):
    if frequencia >= 0:  # Certifica-se de que a frequência é positiva
        buzzer.freq(max(frequencia, 1))  # Evita freq too small, min freq = 1Hz
        buzzer.duty_u16(32768)  # 50% duty cycle, para gerar som
        time.sleep(duracao)
        buzzer.duty_u16(0)  # Desliga o som
    else:
        # Para frequências inválidas, apenas faz uma pausa
        time.sleep(duracao)

# Função para tocar harmonias (notas simultâneas em buzzers diferentes)
def tocar_harmonia(frequencia_A, frequencia_B, duracao):
    buzzer_A.freq(max(frequencia_A, 1))
    buzzer_B.freq(max(frequencia_B, 1))
    buzzer_A.duty_u16(32768)
    buzzer_B.duty_u16(32768)
    time.sleep(duracao)
    buzzer_A.duty_u16(0)
    buzzer_B.duty_u16(0)

# Sequência expandida com harmonias
notas = [
    (392, 0.2),  # G
    (392, 392, 0.2),  # Harmonia G em ambos, para reforço
    (392, 0.2),  # G
    (311, 0.15), # Eb
    (466, 0.1),  # Bb
    (392, 0.2),  # G
    (311, 311, 0.15), # Harmonia Eb em ambos, para reforço
    (466, 0.1),  # Bb
    (392, 0.4),  # G
    # Adicionando mais notas com harmonia
    (587, 0.2),  # D
    (587, 587, 0.2), # Harmonia D em ambos
    (587, 0.2),  # D
    (622, 0.15), # Eb
    (466, 0.1),  # Bb
    (369, 0.2),  # G#
    (311, 311, 0.15), # Harmonia Eb em ambos, para reforço
    (466, 0.1),  # Bb
    (392, 392, 0.4)   # Harmonia G em ambos, para finalizar
]

# Tocando a melodia com harmonias
for nota in notas:
    if len(nota) == 3:
        # Notas com harmonia
        frequencia_A, frequencia_B, duracao = nota
        tocar_harmonia(frequencia_A, frequencia_B, duracao)
    else:
        # Notas únicas
        frequencia, duracao = nota
        tocar_nota(buzzer_A, frequencia, duracao)  # Poderia alternar entre A e B aqui

# Desliga os buzzers
buzzer_A.deinit()
buzzer_B.deinit()
