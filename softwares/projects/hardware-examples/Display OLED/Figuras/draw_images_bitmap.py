# referência: https://www.donskytech.com/micropython-interfacing-with-ssd1306-oled-display/
from machine import Pin, SoftI2C
import ssd1306
import framebuf
import images_repo
import utime


# using default address 0x3C
i2c = SoftI2C(sda=Pin(14), scl=Pin(15))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    for image in images_repo.images_list:
        buffer = image

        fb = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)
        display.fill(0)
        display.blit(fb, 8, 0)

        display.show()
        utime.sleep_ms(2000)
