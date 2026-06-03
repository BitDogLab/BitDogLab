from pimoroni_bus import SPIBus
from picographics import PicoGraphics, DISPLAY_LCD_240X240, PEN_RGB332
import time
import gc
import lcd

# PEN_RGB332 is an 8 bit, fixed 256 colour palette which conserves your RAM.
# Try switching the pen_type to PEN_RGB565 (16 bit, 65K colour) and see the difference!
lcd.LCD() #reset pin = 20
spibus = SPIBus(cs=17, dc=16, sck=18, mosi=19, bl=4)
display = PicoGraphics(display=DISPLAY_LCD_240X240, bus=spibus, pen_type=PEN_RGB332,rotate=0)
display.set_backlight(1.0)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()

BLACK = display.create_pen(0, 0, 0)


def free(full=False):
    # Calculates RAM usage
    gc.collect()
    F = gc.mem_free()
    A = gc.mem_alloc()
    T = F + A
    P = '{0:.2f}%'.format(F / T * 100)
    if not full:
        return P
    else:
        return (f"Total RAM \n{T} bytes \nUnused RAM \n{F} bytes \n({P} free)")


def hsv_to_rgb(h, s, v):
    # From CPython Lib/colorsys.py
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


h = 0

while True:
    h += 1
    r, g, b = [int(255 * c) for c in hsv_to_rgb(h / 360.0, 1.0, 1.0)]  # rainbow magic
    display.set_pen(BLACK)
    RAINBOW = display.create_pen(r, g, b)  # Create pen with converted HSV value
    display.set_pen(RAINBOW)
    display.set_font("bitmap8")
    display.text(free(full=True), 0, 0, WIDTH, 3)
    display.update()
    time.sleep(1.0 / 60)