import time
from neopixel import Neopixel
 
numpix = 30
pixels = Neopixel(numpix, 0, 28, "GRB")
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
color0 = red
 
pixels.brightness(50)
pixels.fill(orange)
pixels.set_pixel_line_gradient(3, 13, green, blue)
pixels.set_pixel_line(14, 16, red)
pixels.set_pixel(20, (255, 255, 255))
 
while True:
    if color0 == red:
       color0 = yellow
       color1 = red
    else:
        color0 = red
        color1 = yellow
    pixels.set_pixel(0, color0)
    pixels.set_pixel(1, color1)
    pixels.show()
    #time.sleep(100)