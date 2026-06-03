import machine
import utime

# Configuração do pino do buzzer
buzzer_pin = machine.Pin(14, machine.Pin.OUT)

# Frequências das notas do hino do Palmeiras
C = 262
D = 294
E = 330
F = 349
G = 392
A = 440
B = 494

# Toca o hino do Palmeiras
buzzer = machine.PWM(buzzer_pin)
buzzer.duty_u16(32768) # Define a amplitude do sinal
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(E)
utime.sleep(0.25)
buzzer.freq(C)
utime.sleep(0.25)
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(A)
utime.sleep(0.25)
buzzer.freq(B)
utime.sleep(0.5)
buzzer.freq(A)
utime.sleep(0.25)
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(F)
utime.sleep(0.25)
buzzer.freq(E)
utime.sleep(0.25)
buzzer.freq(D)
utime.sleep(0.25)
buzzer.freq(C)
utime.sleep(0.5)
buzzer.freq(C)
utime.sleep(0.25)
buzzer.freq(D)
utime.sleep(0.25)
buzzer.freq(E)
utime.sleep(0.25)
buzzer.freq(E)
utime.sleep(0.25)
buzzer.freq(F)
utime.sleep(0.25)
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(A)
utime.sleep(0.25)
buzzer.freq(B)
utime.sleep(0.5)
buzzer.freq(A)
utime.sleep(0.25)
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(F)
utime.sleep(0.25)
buzzer.freq(E)
utime.sleep(0.25)
buzzer.freq(D)
utime.sleep(0.25)
buzzer.freq(E)
utime.sleep(0.25)
buzzer.freq(C)
utime.sleep(0.5)
buzzer.freq(G)
utime.sleep(0.25)
buzzer.freq(E)
utime.sleep(0.25)

# Desliga o buzzer
buzzer.deinit()

    
