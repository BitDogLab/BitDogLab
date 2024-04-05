from machine import Pin, ADC
import neopixel
import time

# Inicializa o display
chain = neopixel.NeoPixel(Pin(7), 25)

# Inicializa o joystick
adc_x = ADC(Pin(26))
adc_y = ADC(Pin(27))
button = Pin(22, Pin.IN, Pin.PULL_UP)

# Mapeia a saída ADC para um índice de LED
def map_adc_to_led(value, adc_min=272, adc_max=512, led_min=0, led_max=4):
    return ((value - adc_min) * (led_max - led_min)) // (adc_max - adc_min) + led_min

# Define a posição inicial (no centro do display)
x = 2
y = 2

# Define um limiar para determinar uma "grande" mudança
threshold = 50

# Armazena os últimos valores ADC
last_adc_value_x = adc_x.read_u16()
last_adc_value_y = adc_y.read_u16()

while True:
    # Lê a posição do joystick
    adc_value_y = adc_x.read_u16() # Invertido
    adc_value_x = adc_y.read_u16() # Invertido

    # Limpa o display
    for i in range(25):
        chain[i] = (0, 0, 0)

    # Verifica se houve uma grande mudança no valor ADC em qualquer direção
    if abs(adc_value_x - last_adc_value_x) > threshold:
        if adc_value_x > last_adc_value_x:
            x += 1
        else:
            x -= 1

    if abs(adc_value_y - last_adc_value_y) > threshold:
        if adc_value_y > last_adc_value_y:
            y += 1
        else:
            y -= 1
   
    # Atualiza os últimos valores ADC
    last_adc_value_x = adc_value_x
    last_adc_value_y = adc_value_y

    # Certifique-se de que x e y estão dentro dos limites de 0 e 4
    x = max(0, min(4, x))
    y = max(0, min(4, y))

    # Inverte o eixo y, pois o (0,0) na matriz de LEDs está no canto superior esquerdo
    y = 4 - y

    # Calcula o índice do LED na matriz unidimensional
    index = y * 5 + x

    # Acende o LED na nova posição com a cor azul
    chain[index] = (0, 0, 255)

    # Atualiza o display
    chain.write()

    # Imprime os valores de x e y lado a lado na saída serial
    print("x: ", x, " y: ", y, "adcx:", adc_value_x, "adcy:", adc_value_y )
    
    # Aguarda um pouco antes da próxima leitura
    time.sleep(0.2)




