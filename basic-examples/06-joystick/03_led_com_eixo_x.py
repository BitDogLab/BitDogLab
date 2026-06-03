from machine import Pin, ADC, PWM
import time

x = ADC(Pin(27))
led = PWM(Pin(13), freq=1000)

while True:
    led.duty_u16(65535 - x.read_u16())
    time.sleep_ms(20)
