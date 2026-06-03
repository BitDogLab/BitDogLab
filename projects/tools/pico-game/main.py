# main.py: Game selection menu by Vincent Mistler (YouMakeTech)
# adapted to BitDogLab by Juliano Oliveira (juliano@hwit.com.br, jrfoliveira@gmail.com)

from machine import Pin, PWM, I2C, Timer, ADC
from ssd1306 import SSD1306_I2C
import time
import random
import neopixel

if __name__ == "__main__":
    NUM_LEDS = 25
    # definir cores para os LEDs
    RED = (50, 0, 0)
    GREEN = (0, 50, 0)
    BLUE = (0, 0, 50)
    YELLOW = (30, 30, 0)
    MAGENTA = (30, 0, 30)
    CYAN = (0, 30, 30)
    WHITE = (25, 25, 25)
    BLACK = (0, 0, 0)
    np = neopixel.NeoPixel(Pin(7), NUM_LEDS)
    # Definindo a matriz de LEDs
    LED_MATRIX = [
        [24, 23, 22, 21, 20],
        [15, 16, 17, 18, 19],
        [14, 13, 12, 11, 10],
        [5, 6, 7, 8, 9],
        [4, 3, 2, 1, 0]
    ]
    for i in range(len(np)):
        np[i] = BLACK
    np.write()
    
    led_r = PWM(Pin(12))
    led_g = PWM(Pin(13))
    led_b = PWM(Pin(11))

    led_r.freq(1000)
    led_g.freq(1000)
    led_b.freq(1000)
    
    led_r.duty_u16(0)
    led_g.duty_u16(0)
    led_b.duty_u16(0)
    
    # To avoid strange errors at startup
    # I don't know why but it works!
    time.sleep(0.2)
    
    # size of the screen
    SCREEN_WIDTH=128                       
    SCREEN_HEIGHT=64
    
    # list of games
    GAMELIST=["Pong","Snake","Space Invaders", "Dino", "2048", "Tetris","Full Speed","Lunar Module"]

    # Buttons connected to GP2 to GP7
    #up = Pin(2, Pin.IN, Pin.PULL_UP)
    #down = Pin(3, Pin.IN, Pin.PULL_UP)
    #left = Pin(4, Pin.IN, Pin.PULL_UP)
    #right = Pin(5, Pin.IN, Pin.PULL_UP)
    
    # Inicializar ADC para os pinos VRx (GPIO26) e VRy (GPIO27)
    adc_vrx = ADC(Pin(26))
    adc_vry = ADC(Pin(27))
    def left():#up():
        vrx_value = adc_vrx.read_u16()
        vry_value = adc_vry.read_u16()
        if ((vrx_value > 16384) and (vry_value < 16384))==True:
            return True
        else:
            return False
    def right():#down():
        vrx_value = adc_vrx.read_u16()
        vry_value = adc_vry.read_u16()
        if ((vrx_value > 16384) and (vry_value > 49152))==True:
            return True
        else:
            return False
    def down():#up():#left():
        vrx_value = adc_vrx.read_u16()
        vry_value = adc_vry.read_u16()
        if ((vrx_value < 16384) and (vry_value > 16384))==True:
            return True
        else:
            return False
    def up():#down():#right():
        vrx_value = adc_vrx.read_u16()
        vry_value = adc_vry.read_u16()
        if ((vrx_value > 49152) and (vry_value > 16384))==True:
            return True
        else:
            return False
    
    button1 = Pin(5, Pin.IN, Pin.PULL_UP)
    button2 = Pin(6, Pin.IN, Pin.PULL_UP)
    
    # Buzzer connected to GP21 or GP10
    buzzer = PWM(Pin(21))
    buzzer.freq(50)  # Frequência inicial grave
    buzzer2 = PWM(Pin(10))
    buzzer2.freq(50)  # Frequência inicial grave
    buzzer.duty_u16(0)
    buzzer2.duty_u16(0)
    
    # OLED Screen connected to GP14 (SDA) and GP15 (SCL)
    i2c = machine.I2C(1, sda = Pin(14), scl = Pin(15), freq = 400000)
    oled = SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c)

    current = 0
    game_selected = -1

    while True:
        oled.fill(0)
        for row in range(0, len(GAMELIST)):
            if row == current:
                oled.fill_rect(0, row*8, SCREEN_WIDTH, 7, 1)
                color = 0
            else:
                color = 1
            
            oled.text(GAMELIST[row], int(SCREEN_WIDTH/2)-int(len(GAMELIST[row])/2 * 8), row*8,color)
        
        oled.show()
        
        time.sleep(0.2)
        
        buttonPressed = False
        
        while not buttonPressed:
            if (down() == 1 or right() == 1) and current < len(GAMELIST) - 1:
                current += 1
                buttonPressed = True
            elif (up() == 1 or left() == 1) and current > 0:
                current -= 1
                buttonPressed = True
            elif button1.value()==0 or button2.value()==0:
                buttonPressed = True
                game_selected = current

        # Make a sound
        buzzer.freq(1000)
        buzzer.duty_u16(2000)
        time.sleep(0.100)
        buzzer.duty_u16(0)
        
        # Start the selected game
        if game_selected >= 0:
            oled.fill(0)
            oled.show()
            
            if game_selected==0:
                from PicoPong import *
                pico_pong_main()
            elif game_selected==1:
                from PicoSnake import *
                pico_snake_main()
            elif game_selected==2:
                from PicoInvaders import *
                pico_invaders_main()
            elif game_selected==3:
                from PicoDino import *
                pico_dino_main()
            elif game_selected==4:
                from Pico2048 import *
                pico_2048_main()
            elif game_selected==5:
                from PicoTetris import *
                pico_tetris_main()
            elif game_selected==6:
                from PicoFullSpeed import *
                pico_full_speed_main()
            elif game_selected==7:
                from PicoLunarModule import *
                pico_lunar_module_main()
                
        game_selected=-1


