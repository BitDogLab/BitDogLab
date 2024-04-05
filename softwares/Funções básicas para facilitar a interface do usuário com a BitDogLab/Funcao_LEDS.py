# Importação das Bibliotecas: Importa as bibliotecas Pin e neopixel necessárias para controlar os LEDs
import neopixel
from machine import Pin

def leds(ledsx, ledsy, ledsr=10, ledsg=10, ledsb=10): # os valores r=g=b=10 são assumidos por padrão se não forem atribuidos
    NUM_LEDS = 25 # define que é uma matriz com 25 LEDs
    ledsPIN = 7
    np = neopixel.NeoPixel(Pin(ledsPIN), NUM_LEDS) # passa o parâmetro inicial para a biblioteca neopixel
    
    #define a posição dos LEDs na matriz da BotDogLab
    LED_MATRIX = [
        [24, 23, 22, 21, 20],    
        [15, 16, 17, 18, 19],
        [14, 13, 12, 11, 10],
        [5, 6, 7, 8, 9],
        [4, 3, 2, 1, 0]
    ]
    
    if 0 <= ledsx <= 4 and 0 <= ledsy <= 4: # verifica se os valores de x e y estão den6tro do range
        led_index = LED_MATRIX[4-ledsy][ledsx]
        np[led_index] = (ledsr, ledsg, ledsb)
        np.write()
    else:
        print("Invalid coordinates.")
        
#FIM

# Examplo de uso
#leds(2, 2)  # Acende o LED do centro da matriz na cor branca (red=10, green=10 e blue=10)

