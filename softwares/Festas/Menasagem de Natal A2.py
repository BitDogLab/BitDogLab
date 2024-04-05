from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from machine import Pin, PWM
import time


# Define os pinos dos Buzzers
buzzer1 = PWM(Pin(21))
buzzer2 = PWM(Pin(4))



# Conecte o LED RGB aos pinos GP13, GP12 e GP14
led_red = PWM(Pin(11))
led_green = PWM(Pin(12))
led_blue = PWM(Pin(13))

# Configuração OLED
i2c = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c)

# Teste OLED
oled.fill(0)  # Limpar display
oled.text("Feliz Natal!", 0, 0)
oled.text("aos colegas do", 0, 25)
oled.text("     D E E B", 0, 50)
oled.show()

time.sleep(2)

#funcionando
import machine, neopixel
import time

np = neopixel.NeoPixel(machine.Pin(7), 25)

# definir cores para os LEDs
#RED = (255, 0, 0)
RED = (0, 0, 25)
GREEN = (0, 25, 0)
#BLUE = (0, 0, 255)
BLUE = (30, 0, 0)
YELLOW = (25, 25, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(1)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = RED
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(1)

# acender cada LED em uma cor diferente
np[5] = BLUE
np[6] = BLACK
np[7] = BLACK
np[8] = BLACK
np[9] = BLUE
np[0] = BLACK
np[1] = BLUE
np[2] = BLUE
np[3] = BLUE
np[4] = BLACK
np[10] = BLACK
np[11] = BLACK
np[12] = BLACK
np[13] = BLACK
np[14] = BLACK
np[15] = BLACK
np[16] = BLUE
np[17] = BLACK
np[18] = BLUE
np[19] = BLACK
np[20] = BLACK
np[21] = BLACK
np[22] = BLACK
np[23] = BLACK
np[24] = BLACK

np.write()

# aguardar 1 segundo
time.sleep(5)


# apagar todos os LEDs
for i in range(len(np)):
    np[i] = BLACK
np.write()




