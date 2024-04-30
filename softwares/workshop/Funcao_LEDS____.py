# Este programa permite acender qualquer LED da matrix na cor definida pelo o usuário e também apagar todos os LEDs da matriz,
# usando duas funções para serem escritas diretamento no shell

# Função que define o controle de acendimento da posição e da cor de cada LED da Matriz
# Uso: leds(x, y, r, g, b)
# x, y: Coordenadas do LED na matriz, variando de 0 a 4
# r, g, b: Valores das cores Vermelho, Verde e Azul (0 a 225)
# Exemplo de uso:
# Acende o LED na posição central (2,2) da matriz na cor amarela (50 de vermelho, 50 de verde, 0 de azul).

# Função para desligar todos os LEDs
# Exemplo de uso: apagar()
# Esta função passa por todas as coordenadas da matriz e define todos os LEDs para preto (desligados)

# Exemplo de uso:
# Acende o LED na posição central (2,2) da matriz na cor amarela (50 de vermelho, 50 de verde, 0 de azul).
#Digite no shell: leds(2, 2, 50, 50, 0)

# Apaga todos os LEDs da matriz
#Digite no shell: apagar()

# Função para gravar bitmap na memória
# gravar(id), onde id deve ser um inteiro de 0 a 24, caso não passe nenhum argumento na função id=0
# Exemplo de uso: gravar(4)

#Função para carregar bitmap gravado na memória
# carregar(id), onde id deve ser um inteiro de 0 a 24, caso não passe nenhum argumento na função id=0
# Exemplo de uso: carregar(22)
from machine import Pin
import neopixel
import utime

# Configurações iniciais
NUM_LEDS = 25  # Número total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)
desenhos = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

# Mapeamento da matriz de LEDs com a origem no canto inferior direito
LED_MATRIX = [
    [24, 23, 22, 21, 20],    
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

# Função que define o controle de acendimento da posição e da dor de cada LED da Matriz do BitDogLab
def leds(x, y, r=20, g=20, b=20):
    if 0 <= x <= 4 and 0 <= y <= 4 and r <= 255 and g <=255 and b <= 255:
        led_index = LED_MATRIX[4-y][x]
        np[led_index] = (r, g, b)
        np.write()
        return f'Posicao: (x={x},y={y}) na cor ({r},{g},{b})'
    elif x > 4:
        return f'Valor escolhido x={x} invalido, escolha um valor entre 0 e 4'
    elif y > 4:
        return f'Valor escolhido y={y} invalido, escolha um valor entre 0 e 4'
    elif r > 255 or g > 255 or b > 255:
        return f'Valor escolhido de cor ({r},{g},{b}) inválido, escolha um valor entre 0 e 255 para cada cor'
    else:
        return f'Coordenadas invalidas, escolha um valor x<=4 e y<=4 e valores para R G B <= 255.'


def apagar():
    np.fill((0,0,0))
    np.write()


def gravar(id=0):
    if(id <= 24):        
        for y in range(5):
            for x in range(5):
                led_index = LED_MATRIX[4-y][x]
                valor = np.__getitem__(led_index)
                desenhos[id].update({led_index : valor})
        apagar()
        return f'Bitmap gravado na posicao: {id}'
    else:
        return f'Escolha um valor entre 0 e 24'
    

def carregar(id=0):
    if(id <= 24):
        if bool(desenhos[id]):
            
            for teste in range(25):
                np[teste] = desenhos[id].get(teste)
            np.write()
            return f'Bitmap carregado da posicao: {id}'
            
        else:
            return f'Nao existe desenho gravado na posicao: {id}'
    else:
            return f'Escolha um valor entre 0 e 24'


def loop(tempo=1):
    while True:
        for id in range(len(desenhos)):
            if bool(desenhos[id]):
                carregar(id)
                utime.sleep(tempo)


def jogo_da_velha():
    apagar()  # Garante que todos os LEDs estão apagados inicialmente
    coordenadas = [(1,0), (1,1), (1,2), (1,3), (1,4),
                   (3,0), (3,1), (3,2), (3,3), (3,4),
                   (0,1), (1,1), (2,1), (4,1), (0,3),
                   (1,3), (2,3), (4,3) ]
    for cor in coordenadas:
        print(f'Acendendo LED em cor')
        leds(cor[0], cor[1], 15, 15, 15)
        utime.sleep(0.5)

    
# Exemplo de uso
leds(2, 2, 50, 0, 0)  # Acende o LED central em vermelho
