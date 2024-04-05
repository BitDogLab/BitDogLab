from sensor_pack import bus_service
from sensor_pack.base_sensor import BaseSensor, Iterator


class Bh1750(BaseSensor, Iterator):
    """Class for work with ambient Light Sensor BH1750.
    https://www.mouser.com/datasheet/2/348/bh1750fvi-e-186247.pdf"""

    def __init__(self, adapter: bus_service.BusAdapter, address: int = 0x23):
        """adapter - экземпляр класса bus_service.BusAdapter. Должен быть создан до вызова этого контсруктора.
        address - адрес устройства на шине I2C.
        adapter - an instance of the bus_service.BusAdapter class. Must be created before calling this constructor.
        address - device address on the I2C bus."""
        super().__init__(adapter, address, big_byte_order=True)
        self._buf_2 = bytearray((0 for _ in range(2)))  # для хранения
        self._high_resolution = False
        self._continuously = False
        # typical measurement_accuracy is 1.2 (from 0.96 to 1.44 times). Pls. see Measurement Accuracy in datasheet!
        self._measurement_accuracy = 1.0

    def __del__(self):
        self.power(False)   # power off before delete

    def _send_cmd(self, command: int):
        """send 1 byte command to device"""
        bo = self._get_byteorder_as_str()[0]    # big, little
        self.adapter.write(self.address, command.to_bytes(1, bo))

    def get_id(self):
        """No ID support in sensor!"""
        return None

    def soft_reset(self):
        """Software reset."""
        self._send_cmd(0b0000_0111)

    def power(self, on: bool = True):
        """Sensor powering"""
        self._send_cmd(0b0000_0001 if on else 0b0000_0000)

    def set_mode(self, continuously: bool = True, high_resolution: bool = True):
        """Set sensor mode.
        high resolution mode 2 not implemented. I have no desire to do this!"""
        if continuously:
            cmd = 0b0001_0000  # continuously mode
        else:
            cmd = 0b0010_0000  # one shot mode

        if not high_resolution:
            cmd |= 0b11    # L-Resolution Mode

        self._send_cmd(cmd)
        #
        self._high_resolution = high_resolution
        self._continuously = continuously

    def get_illumination(self) -> float:
        """Возвращает освещенность в люксах. Параметр measurement_accuracy определен в datasheet.
        Впрочем, его можно не учитывать, так, как он близок к единице, от 0.96 до 1.44!
        Return illumination in lux. use_measurement_accuracy.
        Parameter measurement_accuracy is defined in datasheet.
        However, it can be ignored, since it is close to 1.0, from 0.96 to 1.44!"""
        buf = self._buf_2
        self.adapter.bus.readfrom_into(self.address, buf)       # tmp = self.adapter.read(self.address, 2)
        # typical measurement_accuracy is 1.2 (from 0.96 to 1.44 times). Pls. see Measurement Accuracy in datasheet!
        return self.unpack("H", buf)[0] / self._measurement_accuracy

    def __next__(self) -> float:
        return self.get_illumination()

    def get_conversion_cycle_time(self, max_value: bool = False) -> int:
        """Возвращает время преобразования в [мс] датчиком в зависимости от его настроек.
        Если max_value == True, метод возвращает наибольшее значение (для особо плохих датчиков из партии),
        иначе типовое. Смотри BH1750FVI Technical Note,
        Electrical Characteristics ( V CC = 3.0V, DVI = 3.0V, Ta = 25℃, unless otherwise noted )
        Returns the conversion time in [ms] by the sensor depending on its settings.
        If max_value == True, the method returns the largest value (for particularly bad sensors from the batch),
        otherwise it returns a typical value."""
        offs = 2 * int(self._high_resolution) + int(max_value)
        # low resolution:   16, 24
        # hi resolution:    120, 180
        t = 16, 24, 120, 180
        return t[offs]

    @property
    def high_resolution(self) -> bool:
        """Hi (return True) or Low (return False) resolution mode. Use set_mode method!!!
        In hi mode resolution is 1 lux.
        In low mode resolution is 4 lux."""
        return self._high_resolution

    @property
    def continuously(self) -> bool:
        """Режим непрерывного преобразования или по запросу. Для установки используй метод set_mode.
        Continuous conversion mode or on request. To set, use the set_mode method."""
        return self._continuously

    @property
    def measurement_accuracy(self) -> float:
        """Значение из datasheet в диапазоне от 0.96 до 1.44.
        Value from the datasheet in the range from 0.96 to 1.44."""
        return self._measurement_accuracy

    @measurement_accuracy.setter
    def measurement_accuracy(self, value: float):
        if not 0.96 <= value <= 1.44:
            raise ValueError(f"Invalid measurement accuracy value: {value}")
        self._measurement_accuracy = value
