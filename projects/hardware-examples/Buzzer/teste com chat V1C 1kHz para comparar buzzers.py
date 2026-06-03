from machine import Pin, PWM
import time

# Definindo GPIO21 como saída para PWM (Buzzer A)
buzzer = PWM(Pin(21))

# Definindo a freqüência inicial
start_freq = 20
# Definindo a freqüência final
end_freq = 20000
# Definindo o passo de aumento da frequência
step = 10

for freq in range(start_freq, end_freq + 1, step):
    buzzer.freq(freq)  # Definindo a frequência atual
    buzzer.duty_u16(32768)  # Definindo a duty cycle para 50% (32768 de 65535)
    time.sleep(0.01)  # Intervalo entre cada passo de frequência

buzzer.deinit()  # Desligando o PWM

