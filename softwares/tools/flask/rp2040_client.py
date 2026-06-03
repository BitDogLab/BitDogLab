# scp -P 2223 -r .\flask\ lsm@192.168.43.57:~/bitdoglab-iot/exemplos/
from machine import Pin, SoftI2C, PWM, I2C, ADC
import math
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
from bh1750 import BH1750


green = Pin(11, Pin.OUT)
red = Pin(12, Pin.OUT)
blue = Pin(13, Pin.OUT)

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

i2c0_sda = Pin(0)
i2c0_scl = Pin(1)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)

bh1750 = BH1750(0x23, i2c0)

MIC = ADC(Pin(28))  # GP28 para o microfone
OFFSET = int(1.65 / 3.3 * 65536)  # Valor ADC correspondente a 1,65V


ssid = 'bitdog'
password = '12345678'
# url_server = 'http://192.168.0.53:5000'
url_server = 'https://pedrodsk.pythonanywhere.com/'
# url_server = 'http://192.168.43.57:5000'
wlan = network.WLAN(network.STA_IF)

NUM_COLS = 5
NUM_ROWS = 5
NUM_LEDS = NUM_COLS * NUM_ROWS

def color_gradient(percentage):
    if percentage < 0.5:
        # De azul para verde
        r = 0
        g = int(510 * percentage)
        b = 255 - g
    else:
        # De verde para vermelho
        g = 255 - int(510 * (percentage - 0.5))
        r = 255 - g
        b = 0
    return (r, g, b)

def set_pixel(x, y, r, g, b):
    index = (NUM_ROWS - 1 - y) * NUM_COLS + x
    np[index] = (r, g, b)

def update_display():
    np.write()

def vu_meter(adc_value, last_value):
    volume = max(0, (adc_value - OFFSET)*2)  # Subtrai o offset e garante que o valor seja positivo
    volume_ratio = volume / 65536.0
    num_leds_lit = int(NUM_LEDS * (math.log10(1 + 9 * volume_ratio)))
    
    if num_leds_lit != last_value:
        np.fill((0, 0, 0))
        for i in range(num_leds_lit):
            x = i % NUM_COLS
            y = i // NUM_COLS
            r, g, b = color_gradient(i / (NUM_LEDS - 1))
            set_pixel(x, y, r, g, b)
        update_display()
    
    return num_leds_lit

def convert(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def connect_to_network():
    wlan.active(True)
    wlan.config(pm = 0xa11140)  # Disable power-save mode
    wlan.connect(ssid, password)

    max_wait = 15
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

    url = f"{url_server}{endpoint}"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = urequests.post(url, headers=headers, data=json.dumps(data))
    if r.status_code != 200:
        print(r.status_code)
    r.close()

def send_get(endpoint):

    url = f"{url_server}{endpoint}"
    print(url)
    r = urequests.get(url)
    status = r.content
    status = status.decode()
    r.close()

    # if(endpoint == endpoint):
    #     status = int(status)
    return status

def fill_matriz(r,g,b):
    for i in range(NUM_LEDS):
        np[LED[i]] = (r, g, b)  # Define o LED como branco
        np.write()

def color_leds(r,g,b):
    red.value(r)
    green.value(g)
    blue.value(b)

print('Connecting to Network...')
ip = connect_to_network()

def limiar(get, variavel):
        # print(f"tamanho de char: {len(get)}")
        if get != '0$$$0$$$0$$$0$$$Led':
            values = get.split('$$$')
            print(f"Variavel: {variavel} | Data, Sensor Max, Min, Alerta : {values}")
            data = values[0]
            sensor = values[1]
            max = float(values[2])
            min = float(values[3])
            alerta = values[4]
            if(variavel >= max):
                print(f"ALERTA MAX no {alerta}")
            elif variavel < min:
                print(f"ALERTA MIN no {alerta}")
            else:
                print(f"Sem alertas no {alerta}!")
        
            if alerta == 'Led':
                if variavel >= max:
                    color_leds(r=1, g=0, b=0)
                elif variavel < min:
                    color_leds(r=1, g=0, b=1)
                else:
                    color_leds(r=0, g=1, b=0)
            else:
                color_leds(r=0, g=0, b=0)

            if alerta == 'Buzzer':
                if variavel >= max:
                    alto_falante.init(freq=100, duty_ns=50000)
                elif variavel < min:
                    alto_falante.init(freq=900, duty_ns=25000)
                else:
                    alto_falante.deinit()
            else:
                alto_falante.deinit()
            
            if alerta == 'Matriz':
                if variavel >= max:
                    
                    for i in range(NUM_LEDS):
                        fill_matriz(r=1, g=0, b=0)
                elif variavel < min:
                    for i in range(NUM_LEDS):
                        fill_matriz(r=1, g=0, b=1)
                else:
                    for i in range(NUM_LEDS):
                        fill_matriz(r=0, g=1, b=0)
            else:
                for i in range(NUM_LEDS):
                        fill_matriz(r=0, g=0, b=0)
        else:
                print("nada")
                color_leds(r=0, g=0, b=0)
                alto_falante.deinit()
                fill_matriz(r=0, g=0, b=0)
                max = 0
                min = 0
                alerta = 'Led'
        return data, sensor, max, min, alerta
               

while(True):
    temp = round(sensor.temperature, 2)
    humidity = round(sensor.relative_humidity, 2)
    lux = round(bh1750.measurement, 2)
    mic = MIC.read_u16()

    data = {"temperatura": temp, "umidade": humidity, "luminosidade": lux}
    print(f"\n\nDados coletados : {data}")
   
    send_post(data, '/send_data')
    get_limiar = send_get('/get_limiar')
    data = get_limiar.split('$$$')[0]
    var = get_limiar.split('$$$')[1]
    # print(f"var e data {var} {data}")
    
    if(var == "temperatura"):
        limiar(get_limiar, temp)

        oled.fill(0)
        oled.text('Temp.: {:.2f}C'.format(temp), 0, 0)
        oled.hline(0, 10, 128, 1)  # draw horizontal line x=0, y=8, width=4, colour=1
        oled.text('Umidade: {:.2f}%'.format(humidity), 0, 20)
        oled.text('Lux: {:.2f}'.format(lux), 0, 30)
        oled.text(f'IP: {ip}', 0, 55)
        # oled.text(f'{ip}', 0, 55)
        oled.show()
    elif(var == "umidade"):
        limiar(get_limiar, humidity)

        oled.fill(0)
        oled.text('Temp.: {:.2f}C'.format(temp), 0, 20)
        oled.hline(0, 10, 128, 1)  # draw horizontal line x=0, y=8, width=4, colour=1
        oled.text('Umidade: {:.2f}%'.format(humidity), 0, 0)
        oled.text('Lux: {:.2f}'.format(lux), 0, 30)
        oled.text(f'IP: {ip}', 0, 55)
        # oled.text(f'{ip}', 0, 55)
        oled.show()
    elif(var == "luminosidade"):
        limiar(get_limiar, lux)
        oled.fill(0)
        oled.text('Temp.: {:.2f}C'.format(temp), 0, 30)
        oled.hline(0, 10, 128, 1)  # draw horizontal line x=0, y=8, width=4, colour=1
        oled.text('Umidade: {:.2f}%'.format(humidity), 0, 20)
        oled.text('Lux: {:.2f}'.format(lux), 0, 0)
        oled.text(f'IP: {ip}', 0, 55)
        # oled.text(f'{ip}', 0, 55)
        oled.show()

    else:
        oled.fill(0)
        oled.text('Temp.: {:.2f}C'.format(temp), 0, 0)
        oled.hline(0, 10, 128, 1)  # draw horizontal line x=0, y=8, width=4, colour=1
        oled.text('Umidade: {:.2f}%'.format(humidity), 0, 20)
        oled.text('Lux: {:.2f}'.format(lux), 0, 30)
        oled.text(f'IP: {ip}', 0, 55)
        # oled.text(f'{ip}', 0, 55)
        oled.show()
    # reinitialise with a period of 200us, duty of 50us
    

    
    # if (g_temp == 'on'):
    #     led.value(1)
    #     print('oiii pegou')

    # if (g_temp == b'off'):
    #     led.value(0)
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