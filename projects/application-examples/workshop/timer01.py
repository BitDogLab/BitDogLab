from machine import Pin, Timer
import neopixel
 
green = Pin(11, Pin.OUT) # verde
blue = Pin(12, Pin.OUT) # azul
red = Pin(13, Pin.OUT) #vermelho

chain = neopixel.NeoPixel(Pin(7), 25)

def ligar_verde(t):
    chain[0] = (0, 255, 0)
    chain.write()

def desligar_verde(t):
    chain[0] = (0, 0, 0)
    chain.write()

def ligar_vermelho(t):
    chain[1] = (255, 0, 0)
    chain.write()

def desligar_vermelho(t):
    chain[1] = (0, 0, 0)
    chain.write()


Timer1 = Timer(period = 1100, callback=ligar_verde)
Timer2 = Timer(period = 2300, callback=desligar_verde)
Timer3 = Timer(period = 3100, callback=ligar_vermelho)
Timer4 = Timer(period = 6400, callback=desligar_vermelho)
while True:
    pass