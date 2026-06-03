from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

for nota in [262, 294, 330, 349, 392, 440, 494, 523]:
    buzzer.freq(nota)
    buzzer.duty_u16(9000)
    time.sleep_ms(250)
    buzzer.duty_u16(0)
    time.sleep_ms(60)
