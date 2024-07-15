# PicoGame.py by YouMakeTech
# A class to easily write games for the Raspberry Pi Pico RetroGaming System
# adapted to BitDogLab by Juliano Oliveira (juliano@hwit.com.br, jrfoliveira@gmail.com)

from machine import Pin, PWM, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
from framebuf import FrameBuffer, MONO_HLSB
import time
import random

class PicoGame(SSD1306_I2C):
    def __init__(self):
        self.SCREEN_WIDTH = 128
        self.SCREEN_HEIGHT = 64
        
        self.__adc_vrx = ADC(Pin(26))
        self.__adc_vry = ADC(Pin(27))
        #self.__up = Pin(2, Pin.IN, Pin.PULL_UP)
        #self.__down = Pin(3, Pin.IN, Pin.PULL_UP)
        #self.__left = Pin(4, Pin.IN, Pin.PULL_UP)
        #self.__right = Pin(5, Pin.IN, Pin.PULL_UP)
        self.__button_A = Pin(6, Pin.IN, Pin.PULL_UP)
        self.__button_B = Pin(5, Pin.IN, Pin.PULL_UP)
        self.__buzzer = PWM(Pin(21))
        
        self.__i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.__i2c)
        
        self.__fb=[] # Array of FrameBuffer objects for sprites
        self.__w=[]
        self.__h=[]
        
        self.__mute = False
    
    def center_text(self, s, color = 1):
        x = int(self.width/2)- int(len(s)/2 * 8)
        y = int(self.height/2) - 8
        self.text(s, x, y, color)
        
    def top_right_corner_text(self, s, color = 1):
        x = self.width - int(len(s) * 8)
        y = 0
        self.text(s, x, y, color)
        
    def add_sprite(self, buffer, w, h):
        fb = FrameBuffer(buffer, w, h, MONO_HLSB)
        self.__fb.append(fb)
        self.__w.append(w)
        self.__h.append(h)
        return len(self.__fb) - 1
       
    def sprite(self, n, x, y, key = 0):
        self.blit(self.__fb[n], x, y, key)
        
    def sprite_width(self,n):
        return self.__w[n]
    
    def sprite_height(self,n):
        return self.__h[n]
    
    def sprites_intersection(self, x1, y1, w1, h1, x2, y2, w2, h2):
    # return true if the 2 sprites rectangles
    # (x1,y1,w1,h1) and (x2,y2,w2,h2) overlaps
        overlap = True
        if x2 > x1 + w1 - 1:
            overlap = False
        if x2 + w2 - 1 < x1:
            overlap = False
        if y2 > y1 + h1 -1:
            overlap = False
        if y2 + h2 -1 < y1:
            overlap = False
        return overlap
    
    def sprites_collision(self, n, x1, y1, m, x2, y2):
        if self.sprites_intersection(x1, y1, self.sprite_width(n), self.sprite_height(n), x2, y2, self.sprite_width(m), self.sprite_height(m)):
            dx = max(x1, x2)
            dy = max(y1, y2)
            dw = min(x1 + self.sprite_width(n), x2 + self.sprite_width(m)) - dx
            dh = min(y1 + self.sprite_height(n), y2 + self.sprite_height(m)) - dy
            for j in range(dy, dy + dh):
                for i in range(dx, dx + dw):
                    if self.__fb[n].pixel(i - x1, j - y1) and self.__fb[m].pixel(i - x2, j - y2):
                        return True          
        return False
            
    def button_up(self):
        #return self.__up.value()==0
        vrx_value = self.__adc_vrx.read_u16()
        vry_value = self.__adc_vry.read_u16()
        if ((vrx_value > 49152) and (vry_value > 16384))==True:
            return True
        else:
            return False
    
    def button_down(self):
        #return self.__down.value()==0
        vrx_value = self.__adc_vrx.read_u16()
        vry_value = self.__adc_vry.read_u16()
        if ((vrx_value < 16384) and (vry_value > 16384))==True:
            return True
        else:
            return False
    
    def button_left(self):
        #return self.__left.value()==0
        vrx_value = self.__adc_vrx.read_u16()
        vry_value = self.__adc_vry.read_u16()
        if ((vrx_value > 16384) and (vry_value < 16384))==True:
            return True
        else:
            return False
    
    def button_right(self):
        #return self.__right.value()==0
        vrx_value = self.__adc_vrx.read_u16()
        vry_value = self.__adc_vry.read_u16()
        if ((vrx_value > 16384) and (vry_value > 49152))==True:
            return True
        else:
            return False
        
    def button_A(self):
        return self.__button_A.value()==0
    
    def button_B(self):
        return self.__button_B.value()==0
    
    def any_button(self):
        # returns True if any button is pressed
        button_pressed=False
        if self.button_up():
            button_pressed = True
        if self.button_down():
            button_pressed = True
        if self.button_left():
            button_pressed = True
        if self.button_right():
            button_pressed = True
        if self.button_A():
            button_pressed = True
        if self.button_B():
            button_pressed = True
        return button_pressed
    
    def sound(self, freq, duty_u16 = 2000):
        if not self.__mute:
            # Make a sound at the selected frequency in Hz
            if freq>0:
                self.__buzzer.freq(freq)
                self.__buzzer.duty_u16(duty_u16)
            else:
                self.__buzzer.duty_u16(0)
       
