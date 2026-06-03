from machine import Pin, PWM
import time

# O buzzer da BitDogLab fica no GPIO21.
buzzer = PWM(Pin(21))
buzzer.freq(1000)
buzzer.duty_u16(8000)
time.sleep_ms(200)
buzzer.duty_u16(0)
