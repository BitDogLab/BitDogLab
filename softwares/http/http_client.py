import network
import urequests
import utime
import json
import sys
sys.path.insert(1, 'utils')
import ahtx0
import os
from ssd1306 import SSD1306_I2C
import neopixel

from machine import Pin, SoftI2C, PWM

led = Pin(12, Pin.OUT)
alto_falante = PWM(Pin(21))
onboard = Pin("LED", Pin.OUT, value=0)
# Configuração OLED
i2c_oled = SoftI2C(scl=Pin(15), sda=Pin(14))
oled = SSD1306_I2C(128, 64, i2c_oled)

# Configuração Sensor AHT10/AHT20
i2c_sensor = SoftI2C(scl=Pin(3), sda=Pin(2))
sensor = ahtx0.AHT10(i2c_sensor)
 #matrix de led

NUM_LEDS = 25

# Inicializar a matriz de NeoPixels no GPIO7
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

# 
LED = {
    0: 24, 1: 23, 2: 22, 3: 21, 4: 20,
    5: 15, 6: 16, 7: 17, 8: 18, 9: 19,
    10: 14, 11: 13, 12: 12, 13: 11, 14: 10,
    15: 5, 16: 6, 17: 7, 18: 8, 19: 9,
    20: 4, 21: 3, 22: 2, 23: 1, 24: 0
}

for i in range(NUM_LEDS):
        np[LED[i]] = (0, 0, 0)  # Define o LED como branco
        np.write()

np[LED[0]] = (0, 1, 0)
np[LED[1]] = (0, 1, 0)
np[LED[2]] = (0, 1, 0)
np[LED[3]] = (0, 1, 0)
np[LED[4]] = (0, 1, 0)

np[LED[5]] = (0, 0, 1)
np[LED[6]] = (0, 0, 1)
np[LED[7]] = (0, 0, 1)
np[LED[8]] = (0, 0, 1)
np[LED[9]] = (0, 0, 1)

np[LED[10]] = (1, 0, 0)
np[LED[11]] = (1, 0, 0)
np[LED[12]] = (1, 0, 0)
np[LED[13]] = (1, 0, 0)
np[LED[14]] = (1, 0, 0)

np[LED[15]] = (0, 1, 0)
np[LED[16]] = (0, 1, 0)
np[LED[17]] = (0, 1, 0)
np[LED[18]] = (0, 1, 0)
np[LED[19]] = (0, 1, 0)

np[LED[20]] = (0, 0, 1)
np[LED[21]] = (0, 0, 1)
np[LED[22]] = (0, 0, 1)
np[LED[23]] = (0, 0, 1)
np[LED[24]] = (0, 0, 1)
np.write()


ssid = 'Pedro'
password = '12345678'
wlan = network.WLAN(network.STA_IF)

def connect_to_network():
    wlan.active(True)
    wlan.config(pm = 0xa11140)  # Disable power-save mode
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        utime.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
    return status[0]

def send_post(data, endpoint):

    url = f"http://192.168.43.57:5000{endpoint}"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = urequests.post(url, headers=headers, data=json.dumps(data))
    #print(r.content)
    print(r.status_code)
    r.close()

def get(endpoint):

    url = f"http://192.168.43.57:5000{endpoint}"
    r = urequests.get(url)
    #print(r.content)
    status = r.content
    status = status.decode()
    r.close()

    if(endpoint == '/limiar'):
        status = int(status)
    return status

print('Connecting to Network...')
ip = connect_to_network()

while(True):
    temp = sensor.temperature
    humidity = sensor.relative_humidity
    data = {"temp": temp, "umidade": humidity}
    
    oled.fill(0)
    oled.text('Temp.: {:.2f}C'.format(temp), 0, 0)
    oled.text('Umidade: {:.2f}%'.format(humidity), 0, 20)
    oled.text(f'{ip}', 0, 55)
    oled.show()

    print(data)
   
    alto_falante.freq(50)
    # send_post(data, '/sendtemp')
    limiar = get('/limiar')
    print(limiar)
    status = get('/alerta')
    print(status)
    
    if (status == 'on'):
        led.value(1)
        print('oiii pegou')

    if (status == b'off'):
        led.value(0)
    utime.sleep(5)

# r=urequests.put(url,data=buf)
# print(r.content)
# r.close()
# r=urequests.patch(url,data=buf)
# print(r.content)
# r.close()
# r=urequests.head(url)
# print(r.content)
# print(r.headers)
# r.close()
# r=urequests.delete(url,data=buf)
# print(r.content)
# r.close()