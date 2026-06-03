from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

while True:
    buzzer.freq(1200)
    buzzer.duty_u16(8000)
    time.sleep_ms(100)
    buzzer.duty_u16(0)
    time.sleep_ms(400)
