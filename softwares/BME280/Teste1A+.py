from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
import bme280       #importing BME280 library
 
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)    #initializing the I2C method 
 
 
while True:
  bme = bme280.BME280(i2c=i2c)          #BME280 object created
  print(bme.values)
  sleep(1)           #delay of 1s