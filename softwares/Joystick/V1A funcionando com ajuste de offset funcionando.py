from machine import Pin, ADC, PWM
import neopixel
import time

# Número de LEDs na sua matriz 5x5
NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# Definindo a matriz de LEDs
LED_MATRIX = [
    [24, 23, 22, 21, 20],
    [15, 16, 17, 18, 19],
    [14, 13, 12, 11, 10],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0]
]

# Inicializar ADC para os pinos VRx (GPIO26) e VRy (GPIO27)
adc_vrx = ADC(Pin(26))
adc_vry = ADC(Pin(27))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    # Ler valores analógicos de VRx e VRy
    vrx_value = adc_vrx.read_u16()
    vry_value = adc_vry.read_u16()
    
    # Mapear valores para o intervalo [0, 4] para corresponder aos índices da matriz
    #row = map_value(vrx_value, 240, 65279, 0, 4)
    offsetx = 0
    offsety = 400
    row = map_value(vrx_value - offsetx, 240, 65279, 0, 4)
    col = map_value(vry_value - offsety, 65278, 240, 0, 4)
    
    # Desligar todos os LEDs
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    
    # Acender o LED correspondente
    led_index = LED_MATRIX[row][col]
    np[led_index] = (255, 255, 255)  # Define o LED como branco
    np.write()  # Atualiza o estado da matriz
    
    # Esperar um pouco antes da próxima leitura
    time.sleep(0.1)
