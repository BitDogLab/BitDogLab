from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))

buzzer.freq(440)
buzzer.duty_u16(10000)
time.sleep(1)
buzzer.duty_u16(0)
