from machine import Pin, Timer
import neopixel
 
valv01 = Pin(16, Pin.OUT) # verde

def ligar(t):
    valv01.on()

def desligar(t):
    valv01.off()

Timer1 = Timer(period = 2000, callback=ligar)
Timer1 = Timer(period = 4000, callback=desligar)

while True:
    pass