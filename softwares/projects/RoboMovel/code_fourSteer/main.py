from machine import Pin, PWM, UART
from time import sleep

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

STBY = Pin(20, Pin.OUT)
STBY.value(1)

LEFT_FWD = Pin(4, Pin.OUT)
LEFT_BWD = Pin(9, Pin.OUT)
LEFT_PWM = PWM(Pin(8))

RIGHT_FWD = Pin(19, Pin.OUT)
RIGHT_BWD = Pin(18, Pin.OUT)
RIGHT_PWM = PWM(Pin(16))

buzPin = Pin(21, Pin.OUT)
ledPin = Pin(22, Pin.OUT)

LEFT_PWM.freq(1000)
RIGHT_PWM.freq(1000)
valSpeed = 40000

def set_speed(duty):
    global valSpeed
    valSpeed = duty
    LEFT_PWM.duty_u16(valSpeed)
    RIGHT_PWM.duty_u16(valSpeed)

def stop_all():
    LEFT_FWD.value(0); LEFT_BWD.value(0); LEFT_PWM.duty_u16(0)
    RIGHT_FWD.value(0); RIGHT_BWD.value(0); RIGHT_PWM.duty_u16(0)

def forward():
    LEFT_FWD.value(1); LEFT_BWD.value(0); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(1); RIGHT_BWD.value(0); RIGHT_PWM.duty_u16(valSpeed)

def backward():
    LEFT_FWD.value(0); LEFT_BWD.value(1); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(0); RIGHT_BWD.value(1); RIGHT_PWM.duty_u16(valSpeed)

def left():
    LEFT_FWD.value(1); LEFT_BWD.value(0); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(0); RIGHT_BWD.value(1); RIGHT_PWM.duty_u16(valSpeed)

def right():
    LEFT_FWD.value(0); LEFT_BWD.value(1); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(1); RIGHT_BWD.value(0); RIGHT_PWM.duty_u16(valSpeed)

print("Controle pronto! Aguardando HC-05 (UART0 GP0/GP1)...")

while True:
    if uart.any():
        b = uart.read(1)
        if not b:
            continue
        try:
            command = b.decode('utf-8').strip().upper()
        except:
            continue
        if command == "":
            continue
        print("Recebido:", command)
        cmd = command[0]
        if cmd == 'F':
            forward(); print("-> Frente")
        elif cmd == 'B':
            backward(); print("-> Trás")
        elif cmd == 'L':
            left(); print("-> Esquerda")
        elif cmd == 'R':
            right(); print("-> Direita")
        elif cmd == 'S':
            stop_all(); print("-> Parar")
        elif cmd == 'Y':
            buzPin.value(1); sleep(0.2); buzPin.value(0); print("-> Buzina")
        elif cmd == 'X':
            ledPin.value(1); print("-> LED ON")
        elif cmd == 'x':
            ledPin.value(0); print("-> LED OFF")
        elif cmd in '0123456789':
            scale = int(cmd)
            set_speed(int(65535 * scale / 9))
            print("-> Velocidade ajustada:", scale)
