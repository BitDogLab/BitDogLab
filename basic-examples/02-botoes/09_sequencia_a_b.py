from machine import Pin
import time

a = Pin(5, Pin.IN, Pin.PULL_UP)
b = Pin(6, Pin.IN, Pin.PULL_UP)
ultimo = ""

while True:
    if a.value() == 0 and ultimo != "A":
        ultimo = "A"
        print("primeiro A")
        time.sleep_ms(200)
    if b.value() == 0 and ultimo == "A":
        print("sequencia A depois B")
        ultimo = ""
        time.sleep_ms(200)
