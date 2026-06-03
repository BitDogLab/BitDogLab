from machine import Pin, PWM
import utime

# Inicializa os buzzers como saídas PWM
buzzer1 = PWM(Pin(4))
buzzer2 = PWM(Pin(5))

# Frequência inicial para os buzzers
frequency = 440

# Tempo de início do teste
start_time = utime.ticks_ms()

while utime.ticks_diff(utime.ticks_ms(), start_time) < 20 * 1000:
    # Faz o buzzer1 emitir um som
    buzzer1.freq(frequency)
    buzzer1.duty_u16(32768)  # 50% de duty cycle
    utime.sleep_ms(200)
    buzzer1.duty_u16(0)  # Silencia o buzzer1
    
    # Faz o buzzer2 emitir um som
    buzzer2.freq(frequency)
    buzzer2.duty_u16(32768)  # 50% de duty cycle
    utime.sleep_ms(200)
    buzzer2.duty_u16(0)  # Silencia o buzzer2

    # Aumenta a frequência para o próximo ciclo
    frequency += 100
