from machine import Pin, ADC
import time

# Eixos analogicos do joystick.
x = ADC(Pin(27))
y = ADC(Pin(26))

while True:
    # Cada leitura vai de 0 a 65535.
    print("x:", x.read_u16(), "y:", y.read_u16())
    time.sleep_ms(300)
