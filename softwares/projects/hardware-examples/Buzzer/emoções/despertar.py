from machine import PWM, Pin
import neopixel
import time

# Configuração do NeoPixel
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

def awakening_sound():
    buzzer = PWM(Pin(21))

    # Valores iniciais e finais
    start_freq, end_freq = 50, 120
    start_intensity, end_intensity = 250, 1000
    start_duration, end_duration = 0.6, 0.2

    # Número de etapas
    steps = 10

    # Cálculo do incremento para cada passo
    freq_step = (end_freq - start_freq) / steps
    intensity_step = (end_intensity - start_intensity) / steps
    duration_step = (end_duration - start_duration) / steps

    freq = start_freq
    intensity = start_intensity
    duration = start_duration

    for _ in range(steps):
        buzzer.freq(int(freq))
        buzzer.duty_u16(int(intensity))
        
        # Ajuste o brilho do LED central com base na intensidade
        brightness = int((intensity - start_intensity) / (end_intensity - start_intensity) * 255)
        np[12] = (0, brightness, brightness)
        np.write()
        
        time.sleep(duration)
        
        # Incremento dos valores
        freq += freq_step
        intensity += intensity_step
        duration -= duration_step

    buzzer.duty_u16(0)  # Desliga o buzzer no final
    np[12] = (0, 0, 0)  # Desliga o LED central no final
    np.write()

# Teste
awakening_sound()

