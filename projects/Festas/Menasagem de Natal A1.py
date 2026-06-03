from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from machine import Pin, PWM
import time


# Define os pinos dos Buzzers
buzzer1 = PWM(Pin(21))
buzzer2 = PWM(Pin(4))



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



# Define as notas da música
notas = [
    (69, 100),  # C
    (72, 100),  # D
    (74, 100),  # E
    (76, 100),  # F
    (79, 100),  # G
    (81, 100),  # A
    (83, 100),  # B
    (76, 100),  # F
    (79, 100),  # G
    (81, 100),  # A
    (79, 100),  # G
    (76, 100),  # F
    (72, 100),  # D
    (69, 100),  # C
    (69, 100),  # C
    (72, 100),  # D
    (74, 100),  # E
    (76, 100),  # F
    (79, 100),  # G
    (81, 100),  # A
    (83, 100),  # B
    (76, 100),  # F
    (79, 100),  # G
    (81, 100),  # A
    (79, 100),  # G
    (76, 100),  # F
    (72, 100),  # D
    (69, 100),  # C
    (69, 100),  # C
    (72, 100),  # D
    (74, 100),  # E
    (76, 100),  # F
    (79, 100),  # G
    (81, 100),  # A
    (83, 100),  # B
    (76, 100),  # F
    (79, 100),  # G
    (81, 100),  # A
    (79, 100),  # G
    (76, 100),  # F
    (72, 100),  # D
    (69, 100),  # C
]


# programa funcional




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
        buzzer1.freq(freq)
        buzzer1.duty_u16(32768 if freq > 0 else 0)
        led_red.duty_u16(cor[0]*254)
        led_green.duty_u16(cor[1]*254)
        led_blue.duty_u16(cor[2]*254)
        time.sleep_ms(400 * duracao)
        buzzer1.duty_u16(0)
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





