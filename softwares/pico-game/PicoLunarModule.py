# Game "Lunar Module" by Kuba & Stepan
# Source code from https://github.com/Hellmole/Raspberry-pi-pico-games.git
# adapted to BitDogLab by Juliano Oliveira (juliano@hwit.com.br, jrfoliveira@gmail.com)

from machine import Pin, I2C, PWM, ADC
from ssd1306 import SSD1306_I2C
import time
import random

def pico_lunar_module_main():
    # OLED Screen connected to GP14 (SDA) and GP15 (SCL)
    i2c = I2C(1, sda = Pin(14), scl = Pin(15), freq = 400000)
    oled = SSD1306_I2C(128, 64, i2c)

    oled.fill(0)  
    oled.text("Lunar Module", 5, 6)
    oled.text("By Kuba", 30, 23)
    oled.text("&", 55, 35)
    oled.text("Stepan", 35, 47)
    oled.rect(0, 0, 128, 20 , 1)
    oled.show()
    time.sleep(2)
    
    level = 1
    x_pos = 2
    direction = 0
    ran = 1
    direction2 = 1
    direction3 = 1
    x_pos2 = 2
    y_pos2 = 2
    gravity= 1
    fuel = 25
    fire = 0
    
    button1 = Pin(5, Pin.IN, Pin.PULL_UP)
    button2 = Pin(6, Pin.IN, Pin.PULL_UP)
    
    shift = 0

    while True:
    
        if not button1.value() or not button2:
            # button 1 or 2 pressed => fire thruster
            fire = 1
            gravity = gravity - 5
            fuel = fuel - 1 
  
        oled.fill(0)  
        oled.text("Fuel " + str(fuel), 0, 55)
        oled.text("m/s " + str(gravity), 80, 1)
    
   
        # Lunar modul
        
        oled.rect(6 + x_pos2, 3 + y_pos2, 5, 5, 1)
        oled.vline(5 + x_pos2, 5 + y_pos2, 5, 1)
        oled.vline(11 + x_pos2, 5 + y_pos2, 5, 1)
        oled.rect(7 + x_pos2, 1 + y_pos2, 3, 4 , 1)

        # landing area
        oled.rect(100, 62, 14, 2, 1)
        
        if fire == 1:
            oled.vline(8 + x_pos2, 11 + y_pos2, 8, 1)
            fire = 0

        x_pos2 = x_pos2 + ran 
        y_pos2 = y_pos2 + direction3
        y_pos2 = y_pos2 +  1 + gravity // 10
        gravity = gravity + 1
       
        if x_pos2 > 90 and x_pos2 < 110 and y_pos2 >=  56 and gravity < 4:
            oled.text("Landing OK!", 25, 20)
            level = level + 1
            oled.text("Level " + str(level), 25, 30)
            oled.show()
            time.sleep(2) 
            x_pos = 2
            direction = 0
            gravity = 1
            ran = ran + 1
            direction2 = 1
            direction3 = 1
            x_pos2 = 2
            y_pos2 = 2
            fuel = 25

        elif y_pos2 >=  56 or fuel < 1:       
            oled.text("GAME OVER", 25, 26)
            oled.show()
            time.sleep(2) 
            return
   

        oled.show()

        time.sleep(0.1)
        
if __name__ == "__main__":
    pico_lunar_module_main()
