from time import sleep, sleep_ms
from machine import Pin, PWM, UART, I2C
from neopixel import NeoPixel

use_oled = False

# ----------------- UART -----------------
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# ----------------- NeoPixel (GPIO7) -----------------
NUM_PIXELS = 25
np = NeoPixel(Pin(7, Pin.OUT), NUM_PIXELS)

# Estado da iluminação
target_brightness = 60  # for manual adjustments only (0..255)
weak_brightness = 30
strong_brightness = 255
light_on = False          # estado atual (apagado/aceso)
# Estado da luz para toggle de 4 níveis
light_state = 0  # 0=apagado, 1=fraco, 2=apagado, 3=forte
horn_state = 0  # 0 = beep_bi_bi, 1 = foon_foon

def _apply_all(r, g, b):
    for i in range(NUM_PIXELS):
        np[i] = (r, g, b)
    np.write()

def matrix_off():
    global light_on
    _apply_all(0, 0, 0)
    light_on = False

def matrix_white_now():
    global light_on
    _apply_all(target_brightness, target_brightness, target_brightness)
    light_on = True

def matrix_white(level):
    """Set all LEDs to a specific brightness (white)"""
    global light_on
    for i in range(NUM_PIXELS):
        np[i] = (level, level, level)
    np.write()
    light_on = True

def matrix_white_ramp():
    global light_on
    step = max(4, target_brightness // 12)  # ramp suave
    for v in range(0, target_brightness + 1, step):
        _apply_all(v, v, v)
        sleep(0.01)
    matrix_white_now()  # garante estado final e marca light_on=True

def set_brightness_level(level_0_to_255):
    # seta brilho absoluto (0..255)
    global target_brightness
    target_brightness = max(0, min(255, level_0_to_255))
    if light_on:
        matrix_white_now()  # atualiza na hora

def brightness_step(delta):
    # muda brilho relativo (+/-)
    set_brightness_level(target_brightness + delta)

def center_flash():
    idx_center = 12  # LED central
    matrix_off()
    np[idx_center] = (20, 20, 20)
    np.write()
    sleep(0.2)
    matrix_off()

def update_light_state():
    global light_state
    # Permite acender luz em nivel fraco e forte alternadamente
    # Incrementa e cicla entre 0..3
    light_state = (light_state + 1) % 4
    
    if light_state == 0:
        matrix_off()               # apagado
        print("-> LIGHT OFF (state 0)")
    elif light_state == 1:
        matrix_white(weak_brightness)
        print("-> LIGHT WEAK (state 1)")
    elif light_state == 2:
        matrix_off()               # apagado
        print("-> LIGHT OFF (state 2)")
    elif light_state == 3:
        matrix_white(strong_brightness)
        print("-> LIGHT STRONG (state 3)")

# ----------------- Motores -----------------
LEFT_FWD = Pin(4, Pin.OUT)
LEFT_BWD = Pin(9, Pin.OUT)
LEFT_PWM = PWM(Pin(8))

RIGHT_FWD = Pin(18, Pin.OUT)
RIGHT_BWD = Pin(19, Pin.OUT)
RIGHT_PWM = PWM(Pin(16))

# Ponte H - Standby (ativar com nível alto)
STBY = Pin(20, Pin.OUT)
STBY.value(1)   # mantém ponte H ativa

# LED auxiliar
ledPin = Pin(22, Pin.OUT)

# PWM dos motores
LEFT_PWM.freq(1000)
RIGHT_PWM.freq(1000)
valSpeed = 40000  # duty inicial (até 65535)

def set_speed(duty):
    global valSpeed
    valSpeed = max(0, min(65535, duty))
    LEFT_PWM.duty_u16(valSpeed)
    RIGHT_PWM.duty_u16(valSpeed)

def stop_all():
    LEFT_FWD.value(0); LEFT_BWD.value(0); LEFT_PWM.duty_u16(0)
    RIGHT_FWD.value(0); RIGHT_BWD.value(0); RIGHT_PWM.duty_u16(0)

def forward():
    LEFT_FWD.value(1); LEFT_BWD.value(0); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(1); RIGHT_BWD.value(0); RIGHT_PWM.duty_u16(valSpeed)

def backward():
    LEFT_FWD.value(0); LEFT_BWD.value(1); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(0); RIGHT_BWD.value(1); RIGHT_PWM.duty_u16(valSpeed)

def left():
    LEFT_FWD.value(0); LEFT_BWD.value(1); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(1); RIGHT_BWD.value(0); RIGHT_PWM.duty_u16(valSpeed)

def right():
    LEFT_FWD.value(1); LEFT_BWD.value(0); LEFT_PWM.duty_u16(valSpeed)
    RIGHT_FWD.value(0); RIGHT_BWD.value(1); RIGHT_PWM.duty_u16(valSpeed)

# ----------------- Buzzer (GPIO21) -----------------
buz = PWM(Pin(21))
buz.duty_u16(0)

def _buzz(freq, duty=35000):
    buz.freq(freq)
    buz.duty_u16(duty)

def _buzz_off():
    buz.duty_u16(0)

def foon_foon(cycles=2, freq=190, ms_on=250, ms_off=125):
    """Efeito 'FOON FOON' grave."""
    for _ in range(cycles):
        # ataque suave
        for d in range(10000, 32000, 5000):
            _buzz(freq, d); sleep_ms(30)
        # sustenta
        _buzz(freq, 32000); sleep_ms(ms_on)
        # release
        for d in range(32000, 0, -7000):
            _buzz(freq, d); sleep_ms(30)
        _buzz_off(); sleep_ms(ms_off)

def beep_bi_bi(cycles=2, freq=700, ms_on=125, ms_off=75):
    """Som de buzina."""
    for _ in range(cycles):
        # ataque suave
        for d in range(3000, 9000, 2000):
            _buzz(freq, d); sleep_ms(15)
        # sustenta
        _buzz(freq, 9000); sleep_ms(ms_on)
        # release
        for d in range(9000, 0, -3000):
            _buzz(freq, d); sleep_ms(15)
        _buzz_off(); sleep_ms(ms_off)

def toggle_horn():
    global horn_state
    if horn_state == 0:
        beep_bi_bi()
        print("-> Horn: BEEP BEEP")
    else:
        foon_foon()
        print("-> Horn: FOON FOON")
    horn_state = 1 - horn_state  # toggle between 0 and 1

# ----------------- NeoPixels: feedback buzina -----------------
def clear_pixels():
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)
    np.write()

def show_horn():
    clear_pixels()
    np[6] = (255, 0, 0)
    np[18] = (255, 0, 0)
    np.write()
    sleep(0.2)
    clear_pixels()

# ----------------- OLED opcional -----------------
def show_text(text):
    oled.fill(0)
    oled.text(text, 0, 30)
    oled.show()

if use_oled:
    import ssd1306
    i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)

print(">> Robô BitDogLab pronto. Comandos: F/B/L/R/S, 0-9 vel, Y horn, I/X toggle luz, W liga, i desliga, +/- brilho")
center_flash()

# ----------------- Loop principal -----------------
while True:
    if uart.any():
        raw = uart.read()
        if not raw:
            continue

        for b in raw:
            c = chr(b)
            if c in ('\r', '\n', '\t', ' '):
                continue

            cu = c.upper()

            # ------ Iluminação ------
            if c == 'i':                   # desliga explícito
                matrix_off()
                if use_oled: show_text("LIGHT OFF")
                print("-> LIGHT OFF")

            elif cu == 'W':                # liga branco imediato
                matrix_white_now()
                if use_oled: show_text("LIGHT ON")
                print("-> LIGHT WHITE NOW @", target_brightness)

            elif cu in ('I', 'X'):  # TOGGLE 4 ESTADOS
                update_light_state()
                if use_oled:
                    if light_state in (1, 3):
                        show_text("LIGHT ON")
                    else:
                        show_text("LIGHT OFF")

            elif c == '+':                 # aumenta brilho
                brightness_step(+16)
                print("-> BRIGHTNESS + =>", target_brightness)

            elif c == '-':                 # diminui brilho
                brightness_step(-16)
                print("-> BRIGHTNESS - =>", target_brightness)

            # ------ Movimento ------
            elif cu == 'F':
                forward(); print("-> Forward")
            elif cu == 'B':
                backward(); print("-> Backward")
            elif cu == 'L':
                left(); print("-> Left")
            elif cu == 'R':
                right(); print("-> Right")
            elif cu == 'S':
                stop_all(); print("-> Stop")

            # ------ Buzina ------
            elif cu == 'Y':
                show_horn()          # NeoPixel feedback
                toggle_horn()        # call toggle function
                if use_oled:
                    show_text("HORN")

            # ------ Velocidade ------
            elif c in '0123456789':
                scale = int(c)
                set_speed(int(65535 * scale / 9))
                print("-> Velocity adjusted:", scale)

            else:
                print("-> Unknown:", repr(c))
