from machine import Pin, SoftI2C
from time import sleep_ms
import exPWM.dcmotor as dcmotor

INDEX = 0

i2c = SoftI2C(scl=Pin(1), sda=Pin(0))
dc = dcmotor.DCMotor(i2c)

while True:
  for i in range(-4096, 4096, 8):
    dc.dutyDC(INDEX, i)
    sleep_ms(10)
  for i in range(-4096, 4096, 8):
    dc.dutyDC(INDEX, -i)
    sleep_ms(10)