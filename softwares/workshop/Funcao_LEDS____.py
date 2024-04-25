# Este programa permite acender qualquer LED da matrix na cor definida pelo o usuário e também apagar todos os LEDs da matriz,
# usando duas funções para serem escritas diretamento no shell

# Função que define o controle de acendimento da posição e da cor de cada LED da Matriz
# Uso: leds(x, y, r, g, b)
# x, y: Coordenadas do LED na matriz, variando de 0 a 4
# r, g, b: Valores das cores Vermelho, Verde e Azul (0 a 225)
# Exemplo de uso:
# Acende o LED na posição central (2,2) da matriz na cor amarela (50 de vermelho, 50 de verde, 0 de azul).

# Função para desligar todos os LEDs
# Exwemplo de uso: apaga()
# Esta função passa por todas as coordenadas da matriz e define todos os LEDs para preto (desligados)

# Exemplo de uso:
# Acende o LED na posição central (2,2) da matriz na cor amarela (50 de vermelho, 50 de verde, 0 de azul).
#Digite no shell: leds(2, 2, 50, 50, 0)

# Apaga todos os LEDs da matriz
#Digite no shell: apaga()

from machine import Pin
import neopixel
import time

# Configurações iniciais
NUM_LEDS = 25  # Número total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Mapeamento da matriz de LEDs com a origem no canto inferior esquerdo
LED_MATRIX = [
    [24, 23, 22, 21, 20],    
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]


# Função que define o controle de acendimento da posição e da dor de cada LED da Matriz do BitDogLab
def leds(x, y, r, g, b):
    if 0 <= x <= 4 and 0 <= y <= 4:
        led_index = LED_MATRIX[4-y][x]
        np[led_index] = (r, g, b)
        np.write()
    else:
        print("Coordenadas inválidas.")
        
        

def apaga():
    for y in range(5):
        for x in range(5):
            leds(x, y, 0, 0, 0)
    np.write()  # Forçar atualização dos LEDs
    time.sleep(0.1)  # Pequeno atraso para garantir a aplicação da atualização
    np.write()  # Segunda escrita para garantir que o buffer é atualizado

def jogo_da_velha():
    apaga()  # Garante que todos os LEDs estão apagados inicialmente
    print("Acendendo LED em (1, 0)")
    leds(1, 0, 15, 15, 15)  # Aumentando a intensidade para testar
    time.sleep(0.5)  # Adiciona um atraso de 0.5 segundos para observar a mudança

    print("Acendendo LED em (1, 1)")
    leds(1, 1, 15, 15, 15)
    time.sleep(0.5)

    print("Acendendo LED em (1, 2)")
    leds(1, 2, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (1, 3)")
    leds(1, 3, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (1, 4)")
    leds(1, 4, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (3, 0)")
    leds(3, 0, 15, 15, 15)  # Aumentando a intensidade para testar
    time.sleep(0.5)  # Adiciona um atraso de 0.5 segundos para observar a mudança

    print("Acendendo LED em (3, 1)")
    leds(3, 1, 15, 15, 15)
    time.sleep(0.5)

    print("Acendendo LED em (3, 2)")
    leds(3, 2, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (3, 3)")
    leds(3, 3, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (3, 4)")
    leds(3, 4, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (0, 1)")
    leds(0, 1, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (1, 1)")
    leds(1, 1, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (2, 1)")
    leds(2, 1, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (4, 1)")
    leds(4, 1, 15, 15, 15)
    time.sleep(0.5)


    print("Acendendo LED em (0, 3)")
    leds(0, 3, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (1, 3)")
    leds(1, 3, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (2, 3)")
    leds(2, 3, 15, 15, 15)
    time.sleep(0.5)
    
    print("Acendendo LED em (4, 3)")
    leds(4, 3, 15, 15, 15)
    time.sleep(0.5)
    
# Exemplo de uso
leds(2, 2, 50, 0, 0)  # Acende o LED no canto inferior esquerdo em azul
