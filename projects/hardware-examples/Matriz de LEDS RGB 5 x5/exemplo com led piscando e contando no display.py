from machine import Pin, I2C
import ssd1306

# using default address 0x3C
i2c = I2C(0, sda=Pin(14), scl=Pin(15))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
i = 0

def on_forever():
    global i
    pins.P11.digital_write(True)
    control.wait_micros(1000000)
    pins.P11.digital_write(False)
    control.wait_micros(1000000)
    SSD1306.write_num_new_line(i)
    i += 1
forever(on_forever)