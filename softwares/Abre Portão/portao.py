import time
from machine import Pin, PWM

class Servo:
    __servo_pwm_freq = 50
    __min_u16_duty = 1640 - 2 # offset for correction
    __max_u16_duty = 7864 - 0  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001


    def __init__(self, pin):
        self.__initialise(pin)


    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.__max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)


    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty


    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)

pin_red = Pin(12, Pin.OUT)
pin_green = Pin(13, Pin.OUT)
pin_blue = Pin(11, Pin.OUT)

# Configuração dos botões A e B
pin_btn_a = Pin(5, Pin.IN, Pin.PULL_UP)
pin_btn_b = Pin(6, Pin.IN, Pin.PULL_UP)

sg90_servo = Servo(pin=17)  #GPIO17 da BitDog

# Função para definir a cor do LED RGB
def set_color(red, green, blue):
    pin_red.value(red)
    pin_green.value(green)servoseasdadsasada
    pin_blue.value(blue)

while True:
    if not pin_btn_a.value():
        sg90_servo.move(0)  # turns the servo to 0°.
        time.sleep(1)
        set_color(0,0,1) #led vermelhor = fechado
    elif not pin_btn_b.value():
        sg90_servo.move(90)  # turns the servo to 90°.
        time.sleep(1)
        set_color(1,0,0) #led verde = aberto'