from machine import Pin, PWM
import time

# Conecte o alto-falante ou buzzer passivo ao pino GP4
alto_falante = PWM(Pin(4))

# Frequências das notas musicais
notas = {
    'C4': 261,
    'D4': 294,
    'E4': 329,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523,
}

# Música "O Natal dos Animais"
musica = [
    ('C4', 1), ('D4', 1), ('E4', 1), ('F4', 1), ('G4', 1), ('A4', 1), ('B4', 1),
    ('C5', 1), ('C4', 1), ('D4', 1), ('E4', 1), ('F4', 1), ('G4', 1), ('A4', 1),
    ('B4', 1), ('C5', 1), ('G4', 1), ('F4', 1), ('E4', 1), ('D4', 1), ('C4', 1),
    ('C4', 1), ('D4', 1), ('E4', 1), ('F4', 1), ('G4', 1), ('A4', 1), ('B4', 1),
    ('C5', 1), ('C4', 1), ('D4', 1), ('E4', 1), ('F4', 1), ('G4', 1), ('A4', 1),
    ('B4', 1), ('C5', 1), ('G4', 1), ('F4', 1), ('E4', 1), ('D4', 1), ('C4', 1),
    ('C4', 1), ('D4', 1), ('E4', 1), ('F4', 1), ('G4', 1), ('A4', 1), ('B4', 1),
    ('C5', 1), ('C4', 1), ('D4', 1), ('E4', 1), ('F4', 1), ('G4', 1), ('A4', 1),
    ('B4', 1), ('C5', 1), ('G4', 1), ('F4', 1), ('E4', 1), ('D4', 1), ('C4', 1),
]

# Função para tocar a música
def tocar_musica():
    for nota, duracao in musica:
        freq = notas[nota]
        alto_falante.freq(freq)
        alto_falante.duty_u16(32768)
        time.sleep_ms(400 * duracao)
        alto_falante.duty_u16(0)

while True:
    tocar_musica()
    time.sleep(5)
