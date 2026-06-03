from machine import Pin, I2C

i2c0 = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
i2c1 = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
devices0 = i2c0.scan()
devices1 = i2c1.scan()
print("Endereços dos dispositivos I2C conectados:")
print("I2C0:")
for device in devices0:
    print("   ",hex(device))
print("I2C1:")
for device in devices1:
    print("   ",hex(device))
