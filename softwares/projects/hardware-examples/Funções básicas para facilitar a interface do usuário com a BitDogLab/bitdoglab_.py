# Importação das Bibliotecas: Importa as bibliotecas Pin e neopixel necessárias para controlar os LEDs
import neopixel
from machine import Pin

# Configuração inicial
NUM_LEDS = 25 # define que é uma matriz com 25 LEDs
ledsPIN = 7
np = neopixel.NeoPixel(Pin(ledsPIN), NUM_LEDS)

#define a posição dos LEDs na matriz da BotDogLab
LED_MATRIX = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

def leds(ledsx, ledsy, ledsr=10, ledsg=10, ledsb=10): # os valores r=g=b=10 são assumidos por padrão se não forem atribuidos
    
    if 0 <= ledsx <= 4 and 0 <= ledsy <= 4: # verifica se os valores de x e y estão den6tro do range
        led_index = LED_MATRIX[4-ledsy][ledsx]
        np[led_index] = (ledsr, ledsg, ledsb)
        np.write()
    else:
        print("Invalid coordinates.")
        
# Examplo de uso

#leds(2, 2)


#FIM leds

def apaga(r=0, g=0, b=0):
    posicao_x_y_LED_aceso = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas   


def coracao(r=25, g=0, b=0):
    posicao_x_y_LED_aceso = [(2, 0), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (3, 4)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas     
#         bdl.leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas

def coracao_pequeno(r=25, g=0, b=0):
    posicao_x_y_LED_aceso = [(2, 1), (1, 2), (2, 2), (3, 2), (1, 3), (3, 3)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas
         
def sorriso(r=0, g=0, b=25):
    posicao_x_y_LED_aceso = [(1, 0), (2, 0), (3, 0), (0, 1), (4, 1), (1, 3), (3, 3)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas       

def triste(r=0, g=25, b=25):
    posicao_x_y_LED_aceso =  [(0, 0), (4, 0), (1, 1), (2, 1), (3, 1), (1, 3), (3, 3)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas

def X(r=0, g=25, b=25):
    posicao_x_y_LED_aceso =  [(0, 0), (4, 0), (1, 1), (3, 1), (2, 2), (1, 3), (3, 3), (0, 4), (4, 4)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas

def x(r=0, g=25, b=25):
    posicao_x_y_LED_aceso =  [(1, 1), (3, 1), (2, 2), (1, 3), (3, 3)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas

def girafa(r=20, g=20, b=0): 
    posicao_x_y_LED_aceso =  [(1, 0), (3, 0), (1, 1), (2, 1), (3, 1), (1, 2), (1, 3), (0, 4), (1, 4)]
    for x, y in posicao_x_y_LED_aceso:
         leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas


# Exemplo de uso
#sorriso()  # Acende o coração com as cores padrão (r=25, g=0, b=0)
apaga()  # Acende o coração na cor branca

#FIM coracao

