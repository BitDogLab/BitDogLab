import time
import ustruct
from micropython import const
from exPWM.base import ExpandedPWM

CLOCKWISE = const(0)
COUNTERCLOCKWISE = const(1)

A0 = const(0)
B0 = const(1)
A1 = const(2)
B1 = const(3)
STBY0 = const(4)
STBY1 = const(5)

class DCMotor(ExpandedPWM):
    __PWM_INDEXES = [A0, A1, B0, B1]
    __PWM_PINS = {
        A0: [11, 10], # get pins!!!
        B0: [13, 14],
        A1: [15, 16],
        B1: [6, 7],
        STBY0: 12,
        STBY1: 17
    }
    __PWM_CHANNELS = {
        A0: 9,
        B0: 10,
        A1: 13,
        B1: 14
    }
    
    def __init__(self, i2c, pca_addr=0x40, pcf_addr=0x20):
        super().__init__(i2c, pca_addr, pcf_addr)
        self.freqPWM(500)
        self.pin(self.__PWM_PINS[STBY0], 1)
        self.pin(self.__PWM_PINS[STBY1], 1)
        
    def _validateIndex(self, index: int):
        if not A0 <= index <= B1:
            raise ValueError(f"Given index {index} not valid. Use index from 0 to 3.")
        
    def directionDC(self, index: int, direction=None):
        self._validateIndex(index)
        
        if direction is None:
            if self.pin(self.__PWM_PINS[index][0]):
                return CLOCKWISE
            return COUNTERCLOCKWISE
        
        self.pin(self.__PWM_PINS[index][0], direction)
        self.pin(self.__PWM_PINS[index][1], not direction)
    
    def dutyDC(self, index: int, duty: int):
        direction = self.directionDC(index, int(duty < 0))
        if duty < 0:
            duty = -duty
        self.dutyPWM(self.__PWM_CHANNELS[index], duty)
        return self.directionDC(index)
        
if __name__=="__main__":
    from machine import Pin, I2C
    i2c = I2C(0, scl=Pin(1), sda=Pin(0))
    dc = DCMotor(i2c)
    print(dc.dutyDC(A0, 4095))
