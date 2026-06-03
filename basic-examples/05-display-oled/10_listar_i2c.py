from machine import Pin, I2C

i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)

print("Dispositivos I2C:")
for endereco in i2c.scan():
    print(hex(endereco))
