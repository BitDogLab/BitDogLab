from machine import Pin

CS = 17 #used
DC = 16 #used
SCK = 18
MOSI = 19
RST = 20 #used

class LCD():
    def __init__(self):        
        self.cs = Pin(CS,Pin.OUT)
        self.rst = Pin(RST,Pin.OUT)         
        self.cs(1)
        self.dc = Pin(DC,Pin.OUT)
        self.dc(1)
        self.rst(1)
        self.rst(0)
        self.rst(1)
