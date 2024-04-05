from machine import Pin, ADC, NeoPixel
import time

# Inicializar ADC para os pinos VRx (GPIO26) e VRy (GPIO27)
adc_vry = ADC(Pin(26))
adc_vrx = ADC(Pin(27))

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Configuração da Matriz LED 5x5 RGB
NUM_LEDS = 25  # 5x5
pin_num = 5  # O número do GPIO que controla a matriz
np = NeoPixel(Pin(pin_num), NUM_LEDS)

def turn_off_all_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def turn_on_led(x, y, color=(255, 0, 0)):  # color é RGB
    index = 5 * y + x
    turn_off_all_leds()
    np[index] = color
    np.write()

while True:
    # Ler valores analógicos de VRx e VRy
    vrx_value = adc_vrx.read_u16()
    vry_value = adc_vry.read_u16()
    
    # Mapear valores para o intervalo [0, 4]
    vrx_mapped = map_value(vrx_value, 240, 65279, 0, 4)
    vry_mapped = map_value(vry_value, 240, 65279, 0, 4)
    
    # Acender o LED correspondente
    turn_on_led(vrx_mapped, vry_mapped)
    
    # Exibir valores no console
    print('VRx:', vrx_mapped, 'VRy:', vry_mapped)
    
    # Esperar um pouco antes da próxima leitura
    time.sleep(0.5)

