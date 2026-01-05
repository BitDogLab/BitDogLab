from machine import Pin, I2C
from pca9685 import PCA9685
import time


i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
pca = PCA9685(i2c, address=0x40)
pca.freq(50)

print("PCA9685 inicializado com sucesso!")


def servo_angle(channel, angle):
    duty = int(150 + (angle / 180) * 450)
    pca.duty(channel, duty)

def motor_drive(pwma, ain2, ain1, speed):
    if speed > 0:
        pca.duty(ain1, 4095)
        pca.duty(ain2, 0)
        pca.duty(pwma, int(40 * speed))  
    elif speed < 0:
        pca.duty(ain1, 0)
        pca.duty(ain2, 4095)
        pca.duty(pwma, int(40 * abs(speed)))
    else:
        pca.duty(pwma, 0)
        pca.duty(ain1, 0)
        pca.duty(ain2, 0)

print("""
COMANDOS DISPONÍVEIS:
--------------------------------
sdf+  → servo frente direito +15°
sdf-  → servo frente direito -15°
sef+  → servo frente esquerdo +15°
sef-  → servo frente esquerdo -15°
sdt+  → servo traseiro direito +15°
sdt-  → servo traseiro direito -15°
set+  → sservo traseiro esquerdo +15°
set-  → servo traseiro esquerdo -15°

mef  → motor frente esquerdo ON
mdf  → motor frente direito ON
met  → motor traseiro esquerdo ON
mdt  → motor traseiro direito ON
stop → parar tudo
--------------------------------
""")

while True:
    cmd = input("cmd> ")

    if cmd == "sdf+":
        servo_angle(15, 30)
    elif cmd == "sdf-":
        servo_angle(15, 0)
    elif cmd == "sef+":
        servo_angle(14, 30)
    elif cmd == "sef-":
        servo_angle(14, 0)
    elif cmd == "sdt+":
        servo_angle(13, 30)
    elif cmd == "sdt-":
        servo_angle(13, 0)
    elif cmd == "set+":
        servo_angle(12, 30)
    elif cmd == "set-":
        servo_angle(12, 0)

    elif cmd == "mef":
        print("Motor frontal esquerdo LIGADO")
        motor_drive(0, 1, 2, 50)

    elif cmd == "mdf":
        print("Motor frontal direito LIGADO")
        motor_drive(3, 4, 5, 50)

    elif cmd == "met":
        print("Motor traseiro esquerdo LIGADO")
        motor_drive(6, 7, 8, 50)
        
    elif cmd == "mdt":
        print("Motor traseiro direito LIGADO")
        motor_drive(9, 10, 11, 50)

    elif cmd == "stop":
        motor_drive(0, 1, 2, 0)
        motor_drive(3, 4, 5, 0)
        motor_drive(6, 7, 8, 0)
        motor_drive(9, 10, 11, 0)
        print("Motores PARADOS")

    else:
        print("Comando inválido!")