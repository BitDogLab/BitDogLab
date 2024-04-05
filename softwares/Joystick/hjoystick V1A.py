# SPDX-License-Identifier: BSD-3-Clause
import time
from machine import ADC, Pin

# Initialize ADC and GPIO pins
adc = ADC(Pin(26))
adc2 = ADC(Pin(27))

while True:
    # Read ADC values
    adc_x_raw = adc.read_u16()
    adc_y_raw = adc2.read_u16()

    # Display the joystick position something like this:
    # X: [            o             ]  Y: [              o         ]
    bar_width = 40
    adc_max = (1 << 12) - 1
    bar_x_pos = int(adc_x_raw * bar_width / adc_max)
    bar_y_pos = int(adc_y_raw * bar_width / adc_max)
    print("\rX: [", end="")
    for i in range(bar_width):
        print('o' if i == bar_x_pos else ' ', end="")
    print("]  Y: [", end="")
    for i in range(bar_width):
        print('o' if i == bar_y_pos else ' ', end="")
    print("]", end="")
    time.sleep_ms(50)
