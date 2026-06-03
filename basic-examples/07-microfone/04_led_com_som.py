from machine import Pin, ADC, PWM
import time

mic = ADC(Pin(28))
led = PWM(Pin(13), freq=1000)
centro = 32768

while True:
    valor = abs(mic.read_u16() - centro)
    brilho = min(65535, valor * 4)
    led.duty_u16(brilho)
    time.sleep_ms(20)
