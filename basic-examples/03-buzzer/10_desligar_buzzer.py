from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))
buzzer.freq(1000)
buzzer.duty_u16(10000)
time.sleep_ms(300)
buzzer.duty_u16(0)
buzzer.deinit()
