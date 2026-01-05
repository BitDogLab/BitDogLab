# PCA9685 Driver para MicroPython
# Compatível com Raspberry Pi Pico

import time
from machine import I2C

MODE1 = 0x00
PRESCALE = 0xFE

class PCA9685:
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.reset()

    def reset(self):
        self.write(MODE1, 0x00)
        time.sleep_ms(5)

    def write(self, reg, value):
        self.i2c.writeto_mem(self.address, reg, bytes([value]))

    def read(self, reg):
        return self.i2c.readfrom_mem(self.address, reg, 1)[0]

    def freq(self, freq):
        prescale = int(25000000 / (4096 * freq) - 1)
        oldmode = self.read(MODE1)
        newmode = (oldmode & 0x7F) | 0x10  
        self.write(MODE1, newmode)
        self.write(PRESCALE, prescale)
        self.write(MODE1, oldmode)
        time.sleep_ms(5)
        self.write(MODE1, oldmode | 0xA1)

    def duty(self, channel, value):
        value = max(0, min(4095, value))
        reg = 0x06 + 4 * channel
        data = bytearray([0, 0, value & 0xFF, value >> 8])
        self.i2c.writeto_mem(self.address, reg, data)
