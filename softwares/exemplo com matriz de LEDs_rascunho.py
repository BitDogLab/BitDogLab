# Example using PIO to drive 64 WS2812 LEDs on CJMCU-64 board
# Tony Goodhew 25th March 2022
# 5V to VBUS
# GND to GND
# DIN to GP16
import array, time
from machine import Pin
import rp2

# ============= Neopixel driver from Raspberry Pi Pico Guide =============
# Configure the number of WS2812 LEDs.
NUM_LEDS = 25
PIN_NUM = 7     # DIN  Define o # da GPIO
brightness = .1 # controla a intensidade do 0.005 >= # )= 0.1

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Create the StateMachine with the ws2812 program, outputting on pin
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)

# Display a pattern on the LEDs via an array of LED RGB values.
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

################ Standard Neopixel demos #########################
def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i,c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g<<16) + (r<<8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]
    
def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)

def color_chase(color, wait):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        time.sleep(wait)
        pixels_show()
    time.sleep(0.2)
 
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
  
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            pixels_set(i, wheel(rc_index & 255))
        pixels_show()
        time.sleep(wait)

# Extra routines 
def xy_set(x, y, color):
    pos = x + y*8
    # Avoid out of range errors
    if (pos > -1) and (pos < NUM_LEDS):
        pixels_set(pos, color)

def clear():
    pixels_fill((0,0,0))
    
def sq(x,y,w,r,g,b):
    # Hollow square at (x,y), w pixels wide coloured (r,g,b)
    cc = (r,g,b)
    for i in range(x,x+w):
        xy_set(i,y,cc)
        xy_set(i,y+w-1,cc)
    for i in range(y+1,y+w):
        xy_set(x,i,cc)
        xy_set(x+w-1,i,cc)
    pixels_show()

def vert(x,y,l,r,g,b):
    # Vertical line at (x,y), l pixels long coloured (r,g,b)
    cc = (r,g,b)
    for i in range(l):
        xy_set(x,i,cc)

def horiz(x,y,l,r,g,b):
    # Horizontal line
    cc = (r,g,b)
    for i in range(l):
        xy_set(i,y,cc)

def flag():
    for y in range(4):
        for x in range(8):
            xy_set(x,y,(0,0,255))
            xy_set(x,y+4,(255,255,0))
    pixels_show()

# ============== MAIN ===============
flag()
time.sleep(3)
clear()
pixels_show() 
for xx in range(0,8,2):    
    vert(xx,0,8,200,0,0)
    vert(xx+1,0,8,0,0,200)
pixels_show()
time.sleep(1)
for yy in range(0,8,2):    
    horiz(0,yy,8,200,0,0)
    horiz(0,yy+1,8,0,0,200)
pixels_show()
time.sleep(1)

clear()
sq(0,0,8,0,200,0)
time.sleep(1)
sq(1,1,6,200,200,0)
time.sleep(1)
sq(2,2,4,200,0,0)
time.sleep(1)
sq(3,3,2,0,0,200)
time.sleep(2)
sq(0,0,4,200,0,0)
time.sleep(1)
sq(4,4,4,200,0,0)
time.sleep(1)
sq(4,0,4,0,0,200)
time.sleep(1)
sq(0,4,4,0,0,200)
time.sleep(1)
sq(2,2,4,0,200,0)
time.sleep(3)

# Basic colour values
# See htmlcolorcodes.com to find 'difficult colours'
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

print("Fills")
for color in COLORS:       
    pixels_fill(color)    
pixels_show()

print("Chases")
for color in COLORS:       
    color_chase(color, 0.01)

print("Rainbow")
rainbow_cycle(0)
time.sleep(3)
flag()
time.sleep(3)
pixels_fill(GREEN)
time.sleep(3)
pixels_fill(BLACK)
pixels_show()
print("\nAll done ##############")

