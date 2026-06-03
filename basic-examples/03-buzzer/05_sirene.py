from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

while True:
    for f in range(500, 1500, 40):
        buzzer.freq(f)
        buzzer.duty_u16(8000)
        time.sleep_ms(10)
    for f in range(1500, 500, -40):
        buzzer.freq(f)
        buzzer.duty_u16(8000)
        time.sleep_ms(10)
