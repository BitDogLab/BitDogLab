from machine import Pin, PWM
import time

buzzer = PWM(Pin(21))
musica = [(330, 200), (392, 200), (440, 400), (392, 200), (330, 400)]

for freq, tempo in musica:
    buzzer.freq(freq)
    buzzer.duty_u16(9000)
    time.sleep_ms(tempo)
    buzzer.duty_u16(0)
    time.sleep_ms(80)
