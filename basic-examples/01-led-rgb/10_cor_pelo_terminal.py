from machine import Pin, PWM

r = PWM(Pin(13), freq=1000)
g = PWM(Pin(11), freq=1000)
b = PWM(Pin(12), freq=1000)

def cor(vr, vg, vb):
    r.duty_u16(vr * 257)
    g.duty_u16(vg * 257)
    b.duty_u16(vb * 257)

while True:
    nome = input("cor: ")
    if nome == "vermelho":
        cor(255, 0, 0)
    elif nome == "verde":
        cor(0, 255, 0)
    elif nome == "azul":
        cor(0, 0, 255)
    else:
        cor(0, 0, 0)
