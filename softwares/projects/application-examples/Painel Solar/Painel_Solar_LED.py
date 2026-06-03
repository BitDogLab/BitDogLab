from machine import ADC, Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import time

# Inicialize o pino analógico ADC
adc = ADC(28)  # O pino 28 é o GPIO28

# Inicialize o display OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Inicialize os pinos do LED RGB integrado
led_r = Pin(13, Pin.OUT)  # GPIO 18 para o LED vermelho
led_g = Pin(12, Pin.OUT)  # GPIO 17 para o LED verde
led_b = Pin(11, Pin.OUT)  # GPIO 16 para o LED azul

def acender_led_rgb(r, g, b):
    led_r.value(r)
    led_g.value(g)
    led_b.value(b)

def ler_voltagem():
    # Leitura do valor analógico
    valor_analogico = adc.read_u16()

    # Converta o valor lido para volts (considerando que o módulo fornece 3.3V como referência)
    volts = (valor_analogico / 65535) * 3.3

    # Multiplica a voltagem por 2,6
    volts = volts * 2.6

    return volts

def mostrar_voltagem_no_display(volts):
    oled.fill(0)  # Limpa o display
    oled.text("Voltagem:", 0, 0)
    oled.text("{:.2f} V".format(volts), 0, 20)
    oled.show()

# Função para transição gradual de cor do LED RGB
def transicao_de_cor(volts):
    # Mapeia a voltagem para a faixa de 0 a 1 (para determinar a cor)
    cor = min(1, volts / 3)
    
    # Define a intensidade de cada componente de cor
    intensidade_r = 1 - cor
    intensidade_g = cor
    
    # Define os valores de intensidade para o LED RGB
    acender_led_rgb(intensidade_r, intensidade_g, 0)

# Loop principal
while True:
    volts = ler_voltagem()
    mostrar_voltagem_no_display(volts)
    transicao_de_cor(volts)
    time.sleep(5)  # Espera 5 segundos antes de fazer a próxima leitura e exibição
