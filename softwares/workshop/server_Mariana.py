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
"""
carregar(id)
"""
# onde id deve ser um inteiro de 0 a 24, caso não passe nenhum argumento na função id=0
# Exemplo de uso: carregar(22)

#Função bitmaps facilita colorir a matriz de leds usando letras para aas cores de cada posição:
"""
bitmaps = [
[ g, g, g, g, g ],
[ m, m, r, m, m ],
[ m, m, m, m, m ],
[ g, m, m, m, g ],
[ g, g, m, g, g ]
]
"""
# onde as cores são defininas com os argumentos:
"""
b = (0, 0, 1*it) # BLUE
g = (0, 1*it, 0) # GREEN
r = (1*it, 0, 0) # RED
y = (1*it, 1*it, 0) # YELLOW
m = (1*it, 0, 1*it) # MAGENTA
c = (0, 1*it, 1*it) # CYAN
w = (1*it, 1*it, 1*it) # WHITE
o = (0, 0, 0) # BLACK
"""

#Função para mostrar na matriz de leds o bitmaps desenhado
"""
matriz(bitmaps)
"""

#PROGRAMA PRINCIPAL
from machine import Pin, SoftI2C
import neopixel
from utime import sleep
from time import time
from ulora import LoRa, ModemConfig, SPIConfig
from ssd1306 import SSD1306_I2C

# Configurações iniciais
NUM_LEDS = 25  # Número total de LEDs na matriz 5x5
PIN = 7  # Pino onde a matriz Neopixel está conectada
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)
desenhos = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

# define cores para os LEDs
it = 1
b = (0, 0, 1*it) # BLUE
g = (0, 1*it, 0) # GREEN
r = (1*it, 0, 0) # RED
y = (1*it, 1*it, 0) # YELLOW
m = (1*it, 0, 1*it) # MAGENTA
c = (0, 1*it, 1*it) # CYAN
w = (1*it, 1*it, 1*it) # WHITE
o = (0, 0, 0) # BLACK

# Mapeamento da matriz de LEDs com a origem no canto inferior direito
LED_MATRIX = [
    [24, 23, 22, 21, 20],    
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

# Botões
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)

# Led rgb
verde = Pin(11, Pin.OUT) # verde
azul = Pin(12, Pin.OUT) # azul
vermelho = Pin(13, Pin.OUT) #vermelho

# Função que define o controle de acendimento da posição e da dor de cada LED da Matriz do BitDogLab
def leds(x, y, r=20, g=20, b=20):
    if 0 <= x <= 4 and 0 <= y <= 4 and r <= 255 and g <=255 and b <= 255:
        led_index = LED_MATRIX[4-y][x]
        np[led_index] = (r, g, b)
        np.write()
        return f'Posicao: (x={x},y={y}) na cor: ({r},{g},{b})'
    elif x > 4:
        return f'Valor escolhido x={x} invalido, escolha um valor entre 0 e 4'
    elif y > 4:
        return f'Valor escolhido y={y} invalido, escolha um valor entre 0 e 4'
    elif r > 255 or g > 255 or b > 255:
        return f'Valor escolhido de cor ({r},{g},{b}) inválido, escolha um valor entre 0 e 255 para cada cor'
    else:
        return f'Coordenadas invalidas, escolha um valor x<=4 e y<=4 e valores para R G B <= 255.'


def apagar():
    """
    Função apagar, digite apagar() parar apagar todos os bitmaps da matriz 5x5
    """
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


def matriz(LED_MATRIX = LED_MATRIX, it=50):
    
    

    apagar()

    for Y in range(5):
        for X in range(5):
            #print(LED_MATRIX)
            led_index = LED_MATRIX[4-Y][X]
            if led_index == r:
                leds(X, Y, r[0]*it, r[1]*it, r[2]*it)
            elif led_index == g:
                leds(X, Y, g[0]*it, g[1]*it, g[2]*it)
            elif led_index == b:
                leds(X, Y, b[0]*it, b[1]*it, b[2]*it)
            elif led_index == y:
                leds(X, Y, y[0]*it, y[1]*it, y[2]*it)
            elif led_index == m:
                leds(X, Y, m[0]*it, m[1]*it, m[2]*it)
            elif led_index == c:
                leds(X, Y, c[0]*it, c[1]*it, c[2]*it)
            elif led_index == w:
                leds(X, Y, w[0]*it, w[1]*it, w[2]*it)
            elif led_index == o:
                leds(X, Y, o[0]*it, o[1]*it, o[2]*it)
            else:
                leds(X, Y, 0, 0, 0)

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
                sleep(tempo)


def jogo_da_velha():
    apagar()  # Garante que todos os LEDs estão apagados inicialmente
    coordenadas = [(1,0), (1,1), (1,2), (1,3), (1,4),
                   (3,0), (3,1), (3,2), (3,3), (3,4),
                   (0,1), (1,1), (2,1), (4,1), (0,3),
                   (1,3), (2,3), (4,3) ]
    for cor in coordenadas:
        print(f'Acendendo LED em cor')
        leds(cor[0], cor[1], 15, 15, 15)
        sleep(0.5)

    
# Exemplos de uso
leds(2, 2, 50, 50, 0)  # Acende o LED central em vermelho

valvula_desligada = [
[ r, o, o, o, r ],
[ o, r, o, r, o ],
[ o, o, r, o, o ],
[ o, r, o, r, o ],
[ r, o, o, o, r ]
]

matriz(valvula_desligada)
gravar(0)
valvula_ligada = [
[ o, o, g, o, o ],
[ o, g, o, g, o ],
[ g, o, o, o, g ],
[ o, g, o, g, o ],
[ o, o, g, o, o ]
]

matriz(valvula_ligada)
gravar(1)

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))

    oled.fill(0)  # Limpar oled
    oled.text(f"Testando o lora", 20, 0, 1)
    oled.text(f"From: {payload.header_from}", 0, 10, 1)
    oled.text(f"Received: {payload.message}", 0, 20, 1)
    oled.text(f"{payload.message}", 0, 30, 2)
    oled.text(f"RSSI: {payload.rssi}", 0, 40, 1)
    oled.text(f"SNR: {type(payload.message)}", 0, 50, 1)
    # oled.text(f"{time.gmtime()[0:3]}", 0, 30, 1)
    # oled.text(f"{time.gmtime()[3:7]}", 0, 50, 1)
    oled.show()

    if payload.message == b'1':
        carregar(1)

    if payload.message == b'2':
        carregar(0)

# Lora Parameters
RFM95_RST = 28
RFM95_SPIBUS = SPIConfig.rp2_0
RFM95_CS = 17
RFM95_INT = 20
RF95_FREQ = 868.0
RF95_POW = 14
CLIENT_ADDRESS = 1
SERVER_ADDRESS = 2

# initialise radio
lora = LoRa(RFM95_SPIBUS, RFM95_INT, SERVER_ADDRESS, RFM95_CS, reset_pin=RFM95_RST, freq=RF95_FREQ, tx_power=RF95_POW, acks=True)

# set callback
lora.on_recv = on_recv

# set to listen continuously
lora.set_mode_rx()
verde.on()
# loop and wait for data
while True:
    sleep(0.1)
# Exemplo I - Programa com função delay

# while True:
#     carregar(0)
#     sleep(10)
#     carregar(1)
#     sleep(10)

#     # Se o Botão A for pressionado
#     if botao_a.value() == 0:
#         carregar(0)
#     elif botao_b.value() == 0:
#         carregar(1)

# Exemplo II - Programa sem função delay

# tempo_anterior = time()    
# while True:

#     temporizador = time() - tempo_anterior
#     if temporizador == 10:
#         carregar(0)
    
#     elif temporizador == 20:
#         carregar(1)
#         temporizador = 0
#         tempo_anterior = time()
    

#     # Se o Botão A for pressionado
#     if botao_a.value() == 0:
#         carregar(0)
#         temporizador = 0
#         tempo_anterior = time()

#     elif botao_b.value() == 0:
#         carregar(1)
#         temporizador = 0
#         tempo_anterior = time()

#     print(temporizador)