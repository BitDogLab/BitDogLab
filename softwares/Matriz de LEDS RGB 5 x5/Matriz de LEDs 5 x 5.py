#funcionando
import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(7), 25)

import time

# Função para definir a cor de um pixel
def set_pixel_color(pixel, r, g, b):
    np[pixel] = (r, g, b)

# Função para limpar a matriz de LEDs
def clear_pixels():
    np.fill((0, 0, 0))

# Função para exibir os efeitos na matriz de LEDs
def show_effects():
    demo(np)

# Função para exibir efeitos na matriz de LEDs
def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

# Teste: definindo a cor de cada pixel individualmente
set_pixel_color(0, 255, 0, 0) # Vermelho
set_pixel_color(1, 0, 255, 0) # Verde
set_pixel_color(2, 0, 0, 255) # Azul
set_pixel_color(3, 255, 255, 0) # Amarelo
set_pixel_color(4, 255, 0, 255) # Magenta

# Exibindo os efeitos na matriz de LEDs
show_effects()

# Aguardando 1 segundo antes de limpar a matriz
time.sleep(1)
clear_pixels()
np.write()

