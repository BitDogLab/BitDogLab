from machine import Pin, PWM, SoftI2C
import ssd1306
import time
import neopixel

# Inicialização dos dispositivos I2C para o sensor AHT20 e o display OLED
i2c_sensor = SoftI2C(scl=Pin(3), sda=Pin(2))
sensor_address = 0x38
i2c_display = SoftI2C(scl=Pin(15), sda=Pin(14))
display = ssd1306.SSD1306_I2C(128, 64, i2c_display, 0x3C)

# Inicialização dos pinos para controle dos motores e válvulas
IN1_A = Pin(4, Pin.OUT)
IN2_A = Pin(9, Pin.OUT)
PWM_A = PWM(Pin(8))
IN1_B = Pin(18, Pin.OUT)
IN2_B = Pin(19, Pin.OUT)
PWM_B = PWM(Pin(8))
STBY = Pin(20, Pin.OUT)

# Botões com resistores de pull-up
button_A = Pin(5, Pin.IN, Pin.PULL_UP)
button_B = Pin(6, Pin.IN, Pin.PULL_UP)

# Adicionando o buzzer
BUZZER_PIN = 21  # Substitua com o pino correto onde o buzzer está conectado
buzzer = PWM(Pin(BUZZER_PIN))

# Configuração da matriz de LEDs WS2812B
np = neopixel.NeoPixel(Pin(7), 25)  # 5x5 matriz de LEDs

valve_A_open = False
valve_B_open = False

def setup():
    PWM_A.freq(1000)
    PWM_B.freq(1000)
    STBY.value(1)
    np.fill((0, 0, 0))
    np.write()

def display_sensor_values():
    temperature, humidity = read_aht20()
    display.fill(0)
    display.text('Temp: {:.2f} C'.format(temperature), 0, 10, 1)
    display.text('Umid: {:.2f} %'.format(humidity), 0, 50, 1)
    display.show()

def read_aht20():
    i2c_sensor.writeto(sensor_address, b'\xAC\x33\x00')
    time.sleep(0.1)
    data = i2c_sensor.readfrom(sensor_address, 6)
    humidity = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) * 100 / 0x100000
    temperature = (((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]) * 200 / 0x100000 - 50
    return temperature, humidity

def valve_control(motor_in1, motor_in2, motor_pwm, valve_open, led_indices, valve_name):
    if valve_open:
        motor_in1.value(1)
        motor_in2.value(0)
        for index in led_indices:
            np[index] = (0, 40, 0)  # Verde para aberta
    else:
        motor_in1.value(0)
        motor_in2.value(1)
        for index in led_indices:
            np[index] = (40, 0, 0)  # Vermelho para fechada
    motor_pwm.duty_u16(65535)
    np.write()
    print(f"{valve_name} {'aberta' if valve_open else 'fechada'}: IN1={motor_in1.value()}, IN2={motor_in2.value()}")

setup()

# Definição para ativar o buzzer
def beep(duration_ms=100, frequency=100):
    buzzer.freq(frequency)
    buzzer.duty_u16(12767)  # 50% duty cycle
    time.sleep_ms(duration_ms)
    buzzer.duty_u16(0)

def acender_lilas():
    # Cor lilás, valores aproximados, ajuste conforme necessidade
    lilas = (35, 0, 30)  # RGB para lilás

    # Lista dos índices dos LEDs que devem acender em lilás
    indices_lilas = [2, 7, 12, 17, 22]

    # Aplicar a cor lilás aos LEDs especificados
    for indice in indices_lilas:
        np[indice] = lilas

    # Atualizar a matriz de LEDs para mostrar as novas cores
    np.write()


try:
    while True:
        display_sensor_values()
        acender_lilas()
        if not button_A.value():
            time.sleep(0.1)
            if not button_A.value():
                beep()  # Aciona o beep
                valve_A_open = not valve_A_open
                valve_control(IN1_A, IN2_A, PWM_A, valve_A_open, [3, 4, 5, 6, 13, 14, 15, 16, 23, 24], "Válvula A")
                while not button_A.value():
                    time.sleep(0.1)

        if not button_B.value():
            time.sleep(0.1)
            if not button_B.value():
                beep()  # Aciona o beep
                valve_B_open = not valve_B_open
                valve_control(IN1_B, IN2_B, PWM_B, valve_B_open, [0, 1, 8, 9, 10, 11, 18, 19, 20, 21], "Válvula B")
                while not button_B.value():
                    time.sleep(0.1)

        time.sleep(0.1)

finally:
    motor_stop(IN1_A, IN2_A, PWM_A)
    motor_stop(IN1_B, IN2_B, PWM_B)
    STBY.value(0)
    np.fill((0, 0, 0))
    np.write()
    buzzer.deinit()  # Desativa o buzzer para liberar o pino PWM