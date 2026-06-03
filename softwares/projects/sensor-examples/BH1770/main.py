# micropython
# mail: goctaprog@gmail.com
# MIT license


# Please read this before use!: https://www.mouser.com/datasheet/2/348/bh1750fvi-e-186247.pdf
from machine import I2C
import bh1750
from sensor_pack.bus_service import I2cAdapter
import time

if __name__ == '__main__':
    # пожалуйста установите выводы scl и sda в конструкторе для вашей платы, иначе ничего не заработает!
    # please set scl and sda pins for your board, otherwise nothing will work!
    # https://docs.micropython.org/en/latest/library/machine.I2C.html#machine-i2c
    # i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=400_000) # для примера
    # bus =  I2C(scl=Pin(4), sda=Pin(5), freq=100000)   # на esp8266    !
    # Внимание!!!
    # Замените id=1 на id=0, если пользуетесь первым портом I2C !!!
    # Warning!!!
    # Replace id=1 with id=0 if you are using the first I2C port !!!
    i2c = I2C(id=0, freq=400_000)  # on Arduino Nano RP2040 Connect tested
    adaptor = I2cAdapter(i2c)
    sol = bh1750.Bh1750(adaptor)

    # если у вас посыпались исключения EIO, то проверьте все соединения.
    # if you get EIO exceptions, then check all connections.
    # Радиотехника - наука о контактах! РТФ-Чемпион!
    sol.power(on=True)     # Sensor Of Lux
    sol.set_mode(continuously=True, high_resolution=True)
    sol.measurement_accuracy = 1.0      # default value
    old_lux = curr_max = 1.0
    
    for lux in sol:
        if lux != old_lux:
            curr_max = max(lux, curr_max)
            lt = time.localtime()
            print(f"{lt[3:6]}\tIllumination [lux]: {lux}.; max: {curr_max}.; Normalized [%]: {100*lux/curr_max}.")
        old_lux = lux        
        time.sleep_ms(sol.get_conversion_cycle_time())
