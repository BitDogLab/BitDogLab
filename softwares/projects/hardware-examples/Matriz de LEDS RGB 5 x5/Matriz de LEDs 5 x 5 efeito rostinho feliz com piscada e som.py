
import machine, neopixel, time
import pin



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
    ('C4', 1)
    ]


np = neopixel.NeoPixel(machine.Pin(7), 25)

# definir cores para os LEDs
#RED = (255, 0, 0)
RED = (0, 0, 255)#na verdade este é o BLUE
GREEN = (0, 255, 0)
#BLUE = (0, 0, 255)
BLUE = (80, 0, 0)#na verdade este é o RED
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# acender cada LED em uma cor diferente
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(1)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = RED
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

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
# aguardar 1 segundo
time.sleep(1)

while True:
    tocar_musica()
# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(5)


# apagar todos os LEDs
for i in range(len(np)):
    np[i] = BLACK
np.write()

