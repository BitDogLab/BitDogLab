import time
import ustruct

HIGH = const(1)
LOW = const(0)

class ExpandedPWM:
    def __init__(self, i2c, pca_addr=0x40, pcf_addr=0x20):
        self._i2c = i2c
        self._pca_addr = pca_addr
        self._pcf_addr = pcf_addr
        self.scan()
        self._pcf_port = bytearray(2)
        self._writePCA(0x00, 0x00) # Resets PCA.
    
    def _readPCA(self, addr: int, nbytes: int=1):
        '''
        Reads `nbytes` bytes, starting with PCA register at address `addr`.
        
                Parameters:
                    addr (int): Address of starting register.
                    nbytes (int): Number of bytes to be read, beginning at register.
                Returns:
                    Data from register(s). If nbytes is 1, data is an int; else, a bytes object.
        '''
        data = self._i2c.readfrom_mem(self._pca_addr, addr, nbytes) # readfrom_mem returns a bytes object.
        return data if nbytes > 1 else data[0]
    
    def _writePCA(self, addr: int, data):
        '''
        Writes contents of buffer `data` to PCA registers, starting at address `addr`.
        
                Parameters:
                    addr (int): Starting register address in which data is written.
                    data (bytearray): Content to be written.
        '''
        if isinstance(data, int):        
            self._i2c.writeto_mem(self._pca_addr, addr, bytearray([data]))
        else:
            self._i2c.writeto_mem(self._pca_addr, addr, data)
    
    def _readPCF(self):
        '''
        Reads pin data from PCF.
        
        There are 14 pins, so bits 15 and 7 of return value are always zero.
        
                Returns:
                    Pin data in the form of an int.
        '''
        self._i2c.readfrom_into(self._pcf_addr, self._pcf_port)
        return (self._pcf_port[1] << 8) | self._pcf_port[0]

    def _writePCF(self, data=None):
        '''
        Writes `data` to `_pcf_port` buffer and PCF pins.
        
                Parameters:
                    data (int): Port data to be written in PCF.
        '''
        if data is not None:
            self._pcf_port[1] = (data >> 8) & 0xFF
            self._pcf_port[0] = data & 0xFF
        self._i2c.writeto(self._pcf_addr, self._pcf_port)
    
    def _validatePinPCF(self, pin: int):
        if 0 <= pin <= 7:
            return pin
        if 10 <= pin <= 17:
            return pin - 2
        raise ValueError(f"Invalid pin {pin}. Pin number should be between 0 and 7 or between 10 and 17.")
    
    def _validateChannelPCA(self, channel: int):
        if not 0 <= channel <= 15:
            raise ValueError(f"Invalid channel {channel}. Channel number should be between 0 and 15.")
    
    def scan(self):
        scan_result = self._i2c.scan()
        if scan_result.count(self._pcf_addr) == 0:
            raise OSError(f"PCF8575 not found at address {self._pcf_addr:#x}")
        if scan_result.count(self._pca_addr) == 0:
            raise OSError(f"PCA9685 not found at address {self._pca_addr:#x}")
        return True
    
    def pin(self, pin: int, value=None):
        '''
        Writes pin value. When `value` is None, reads current pin value.
        
                Parameters:
                    pin (int): Pin number. Must be between 0 and 7 or between 10 and 17.
                    value (int, optional): New pin value.
        '''
        
        pin = self._validatePinPCF(pin) # Initial pin number validation.
        
        if value is None: # If reading, return pin value in _pcf_port.
            return (self._pcf_port[pin // 8] >> (pin % 8)) & 0x01
        
        # If writing...
        if value: # Else, if value is written to high, change _pcf_port bit to high.
            self._pcf_port[pin // 8] |= 1 << (pin % 8)
        else: # If value is written to low, change _pcf_port bit to low.
            self._pcf_port[pin // 8] &= ~(1 << (pin % 8))
        self._writePCF() # After that, rewrite bits in PCF.
    
    def freqPWM(self, freq=None):
        '''
        Writes new PWM frequency. When `freq` is None, reads current PWM frequency.
        
        The PCA's internal oscillator is 25MHz and its max counter value is 4096.
        Thus, the PWM frequency and its prescaler are related as per the equation
            f_PWM = 25000000 / (4096 * PSC)
        which is the same as saying
            PSC = 25000000 / (4096 * f_PWM)
        
                Parameters:
                    freq (int, optional): New frequency value for PWM channels.
        '''
        if freq is None:
            # freq is None, so read current frequency.
            prescaler = self._readPCA(0xFE) # Reads from PRE_SCALE register.
            return int(-0.5 + (25000000.0 / 4096.0) / prescaler)
        
        # freq is not None, so update frequency.
        old_mode1 = self._readPCA(0x00) # Reads from MODE1 register.
        self._writePCA(0x00, (old_mode1 & 0b01111111) | 0b00010000) # Sets SLEEP bit.
        self._writePCA(0xFE, int(0.5 + (25000000.0 / 4096.0) / freq)) # Writes new prescaler.
        self._writePCA(0x00, old_mode1) # Restores previous MODE1 value.
        time.sleep_us(500)
        self._writePCA(0x00, old_mode1 | 0b10100001) # Restores old MODE1 value, with RESTART, AI and ALLCALL bits set.
        
    def dutyPWM(self, channel: int, duty=None):
        '''
        Writes new duty cycle value in channel `channel`. When `duty` is None, reads current duty value.
        
                Parameters:
                    channel (int): PWM channel to be read or written in.
                    duty (int, optional): New duty cycle value.
        '''
        self._validateChannelPCA(channel)
        
        if duty is None:
            pwm = self._readPCA(0x06 + 4 * channel, 4)
            value = ustruct.unpack('<HH', pwm)
            if value[0] == 4096:
                return 4095
            if value[1] == 4096:
                return 0
            return value[1]
        
        if 0 < duty < 4095:
            on = 0
            off = duty # I have no idea why this works, but it's the only way it works.
        elif duty == 0: # If duty cycle is 100% on or 100% off, just use designated bits.
            on = 0
            off = 4096
        elif duty == 4095:
            on = 4096
            off = 0
        else:
            raise ValueError(f"Invalid duty value {duty}. Duty must be between 0 and 4095.")
        data = ustruct.pack("<HH", on, off)
        self._writePCA(0x06 + 4 * channel, bytearray(data))

if __name__ == "__main__":
    from machine import Pin, I2C
    i2c = I2C(0, scl=Pin(1, pull=Pin.PULL_UP), sda=Pin(0, pull=Pin.PULL_UP))
    epwm = ExpandedPWM(i2c)
    epwm.freqPWM(500)
    epwm.pin(11, 1)
    epwm.pin(10, 0)
    epwm.pin(12, 1)