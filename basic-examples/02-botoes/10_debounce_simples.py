from machine import Pin
import time

botao = Pin(5, Pin.IN, Pin.PULL_UP)
estado = botao.value()

while True:
    novo = botao.value()
    if novo != estado:
        # Espera um pouco para evitar leitura duplicada do mesmo clique.
        time.sleep_ms(30)
        if botao.value() == novo:
            estado = novo
            print("apertou" if estado == 0 else "soltou")
