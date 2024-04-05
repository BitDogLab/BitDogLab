from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from machine import Pin, PWM
import time


# Define os pinos dos Buzzers
buzzer1 = PWM(Pin(21))
buzzer2 = PWM(Pin(4))

# Conecte o alto-falante ou buzzer passivo ao pino GP4
alto_falante = PWM(Pin(4))
np=25

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
   ]

# Função para tocar a música
def tocar_musica():
    for nota, duracao in musica:
        freq = notas[nota]
        alto_falante.freq(freq)
        #alto_falante.duty_u16(32768)
        alto_falante.duty_u16(10000)
        time.sleep_ms(200 * duracao)
        alto_falante.duty_u16(0)

# Conecte o LED RGB aos pinos GP13, GP12 e GP14
led_red = PWM(Pin(11))
led_green = PWM(Pin(12))
led_blue = PWM(Pin(13))

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Teste OLED
oled.fill(0)  # Limpar display
oled.text("Feliz Natal!", 0, 0)
oled.text("aos colegas do", 0, 25)
oled.text("     D E E B", 0, 50)
oled.show()

time.sleep(0)

#funcionando
import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(7), 25)

# definir cores para os LEDs
#RED = (255, 0, 0)
RED = (0, 0, 10)
GREEN = (0, 25, 0)
#BLUE = (0, 0, 255)
BLUE = (10, 0, 0)
YELLOW = (25, 25, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# apagar todos os LEDs
for i in range(25):
    np[i] = BLACK
    np.write()
'''# acender cada LED em uma cor diferente
np[5] = BLACK
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLACK
np[0] = BLACK
np[1] = BLACK
np[2] = BLACK
np[3] = BLACK
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLACK
np[17] = BLACK
np[18] = BLACK
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK
np.write()
'''

# aguardar 1 segundo
time.sleep(1.5)




while True:
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
    tocar_musica()
    time.sleep(.3)
    
    

    # aguardar 1 segundo
    time.sleep(.2)

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

    # aguardar 1 segundo
    time.sleep(1)

    # Define colors as constants
    BLUE = 'blue'
    BLACK = 'black'

    # Define ranges as constants
    RANGE_1 = slice(0, 5)
    RANGE_2 = slice(5, 10)
    RANGE_3 = slice(10, 20)
    RANGE_4 = slice(20, 25)

    # Define color patterns
    PATTERN_1 = [BLACK, BLUE, BLUE, BLUE, BLACK]
    PATTERN_2 = [BLUE, BLACK, BLACK, BLACK, BLUE]
    PATTERN_3 = [BLACK] * 11
    PATTERN_4 = [BLACK] * 5

    # Assign color patterns to ranges
    np[RANGE_1] = PATTERN_1
    np[RANGE_2] = PATTERN_2
    np[RANGE_3] = PATTERN_3
    np[RANGE_4] = PATTERN_4

    # Write changes
    np.write()


    # apagar todos os LEDs
    for i in range(len(np)):
        np[i] = BLACK
    np.write()

    time.sleep(2)

    np.write()
    
    # apagar todos os LEDs
    for i in range(len(np)):
        np[i] = BLACK
    np.write()
    
    time.sleep(2)


