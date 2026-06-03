from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))
buzzer.freq(700)

while True:
    for volume in range(0, 16000, 800):
        buzzer.duty_u16(volume)
        time.sleep_ms(80)
    for volume in range(16000, -1, -800):
        buzzer.duty_u16(volume)
        time.sleep_ms(80)
