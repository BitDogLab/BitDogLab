# programa funcional

from machine import Pin, PWM
import time

# Conecte o alto-falante ou buzzer passivo ao pino GP4
alto_falante = PWM(Pin(4))

# Conecte o LED RGB aos pinos GP13, GP12 e GP14
led_red = PWM(Pin(11))
led_green = PWM(Pin(12))
led_blue = PWM(Pin(13))

# Frequências das notas musicais
notas = {
    'C4': {'freq': 261, 'cor': (255, 0, 0)},
    'D4': {'freq': 294, 'cor': (255, 127, 0)},
    'E4': {'freq': 329, 'cor': (255, 255, 0)},
    'F4': {'freq': 349, 'cor': (0, 255, 0)},
    'G4': {'freq': 392, 'cor': (0, 0, 255)},
    'A4': {'freq': 440, 'cor': (75, 0, 130)},
    'B4': {'freq': 494, 'cor': (143, 0, 255)},
    'C5': {'freq': 523, 'cor': (255, 0, 255)},
    'PAUSA': {'freq': 0, 'cor': (0, 0, 0)}
}

# Música "Brilha, Brilha, Estrelinha"
musica = [
    ('C4', 1), ('C4', 1), ('G4', 1), ('G4', 1), ('A4', 1), ('A4', 1), ('G4', 2),
    ('F4', 1), ('F4', 1), ('E4', 1), ('E4', 1), ('D4', 1), ('D4', 1), ('C4', 2),
    ('G4', 1), ('G4', 1), ('F4', 1), ('F4', 1), ('E4', 1), ('E4', 1), ('D4', 2),
    ('G4', 1), ('G4', 1), ('F4', 1), ('F4', 1), ('E4', 1), ('E4', 1), ('D4', 2),
    ('C4', 1), ('C4', 1), ('G4', 1), ('G4', 1), ('A4', 1), ('A4', 1), ('G4', 2),
    ('F4', 1), ('F4', 1), ('E4', 1), ('E4', 1), ('D4', 1), ('D4', 1), ('C4', 2),
]

def tocar_musica():
    for nota, duracao in musica:
        freq = notas[nota]['freq']
        cor = notas[nota]['cor']
        alto_falante.freq(freq)
        alto_falante.duty_u16(32768 if freq > 0 else 0)
        led_red.duty_u16(cor[0]*254)
        led_green.duty_u16(cor[1]*254)
        led_blue.duty_u16(cor[2]*254)
        time.sleep_ms(400 * duracao)
        alto_falante.duty_u16(0)
        led_red.duty_u16(0)
        led_green.duty_u16(0)
        led_blue.duty_u16(0)
        time.sleep_ms(70)
        
        # esse comando mostra o valor do Duth Cycle do LED RGB
        print(cor[0]*254)
        print(cor[1]*254)
        print(cor[2]*254)  
        print()


while True:
    tocar_musica()
    time.sleep(5)

