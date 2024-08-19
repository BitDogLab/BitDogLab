from pimoroni_bus import SPIBus
from picographics import PicoGraphics, DISPLAY_LCD_240X240, PEN_RGB332
from pngdec import PNG
import lcd

# PEN_RGB332 is an 8 bit, fixed 256 colour palette which conserves your RAM.
# Try switching the pen_type to PEN_RGB565 (16 bit, 65K colour) and see the difference!
lcd.LCD() #reset pin = 20
spibus = SPIBus(cs=17, dc=16, sck=18, mosi=19, bl=4)

display = PicoGraphics(display=DISPLAY_LCD_240X240, bus=spibus, pen_type=PEN_RGB332,rotate=0)
display.set_backlight(1.0)

png = PNG(display)
png.open_file("escola-4p0.png")
png.decode(0, 0)

# Display the result
display.update()
