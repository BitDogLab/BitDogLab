from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))
buzzer.freq(900)

def bip(ms):
    buzzer.duty_u16(9000)
    time.sleep_ms(ms)
    buzzer.duty_u16(0)
    time.sleep_ms(120)

while True:
    for tempo in [120, 120, 120, 350, 350, 350, 120, 120, 120]:
        bip(tempo)
    time.sleep(1)
