import network
import socket
import time
import sys
sys.path.insert(1, 'utils')
import ahtx0
import os
from ssd1306 import SSD1306_I2C
import neopixel

from machine import Pin, SoftI2C, PWM
import uasyncio as asyncio


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

html = """<!DOCTYPE html>
<html>
    <head> <title>BitDogLab</title> </head>
    <body> <h1>BitDogLab - IoT</h1>
        <h2>%s</h2>
    </body>
</html>
"""

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
        time.sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])
    return status[0]

async def serve_client(reader, writer, limiar=50):
    print("Client connected")
    request_line = await reader.readline()
    print("Request:", request_line)
    # We are not interested in HTTP request headers, skip them
    while await reader.readline() != b"\r\n":
        pass

    request = str(request_line)
    led_on = request.find('/On')
    led_off = request.find('/Off')
    print( 'led on = ' + str(led_on))
    print( 'led off = ' + str(led_off))
    #print('GET Request Content = %s' % request)
    teste = '%s' % request
    temp = sensor.temperature
    humidity = sensor.relative_humidity
    alerta_disparado = "Alerta não disparado"
    
    if(teste.split(' ')[1].split('/')[1] != ''):
        teste = teste.split(' ')[1].split('/')[1]
        print(f"O valor do get: {teste}")
        limiar = int(teste)
        print(f"O valor do limiar: {limiar}")
        if (temp >= limiar):
            led.value(1)
            alto_falante.duty_u16(200)
            alerta_disparado = "Alerta disparado"
            for i in range(NUM_LEDS):
                np[LED[i]] = (255, 0, 0)  # Define o LED como branco
                np.write()
        else:
            led.value(0)
            alto_falante.duty_u16(0)
            for i in range(NUM_LEDS):
                np[LED[i]] = (0, 0, 0)  # Define o LED como branco
                np.write()

    stateis = f"Temperatura: {temp}"
    stateis2 = f"Umidade: {humidity}"
    list = [stateis, stateis2]
    if led_on == 6:
        print("led on")
        led.value(1)
        stateis = "LED is ON"
    
    if led_off == 6:
        print("led off")
        led.value(0)
        stateis = "LED is OFF"
        
    response = html % list
    #imgfile = open('logo1.jpg', 'rb').read()
    writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(f"""
       <!DOCTYPE html>
        <html>
            <head>
                <title>BitDogLab-IoT Webserver</title>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta http-equiv="refresh" content="10" >
                <!-- <link href="/styles.css" rel="stylesheet"> -->
            </head>
            <body class="bg-gray-100" style="background-color:powderblue;">
        <div class="relative flex min-h-screen flex-col justify-center overflow-hidden bg-gray-50 py-6 sm:py-12">
        <div class="relative bg-white px-6 pb-8 pt-10 shadow-xl ring-1 ring-gray-900/5 sm:mx-auto sm:max-w-lg sm:rounded-lg sm:px-10">
        <div class="mx-auto max-w-md">
        """)
    #writer.write(imgfile)
    writer.write(f"""
        <div class="divide-y divide-gray-300/50">
        <div class="space-y-6 py-8 text-base leading-7 text-gray-600">
          <h1 class="text-lg font-semibold"style="text-align: center;">BitDogLab-IoT</h1>
          <h3 class="text-base font-semibold">Temperatura: {temp}</h3>
          <h3 class="text-base font-semibold">Umidade do ar: {humidity}</h3>
            
          


        """
        )
    writer.write("""  
                <input type="text" placeholder="limiar da temperatura" id="myInput">
                <button type="button" onclick="getInputValue();">Alterar</button>
    
    <script>
        function getInputValue(){
            // Selecting the input element and get its value 
            var inputVal = document.getElementById("myInput").value;
            location.replace(inputVal)
        }
    </script> """)
    writer.write(f"""
                 <p class="text-base font-semibold">Limiar da temperatura: {limiar}</p>
                 <h4 class="text-base font-semibold"style="background-color:tomato;">{alerta_disparado}</h4> """)

   # writer.write(response)

    await writer.drain()
    await writer.wait_closed()
    
    print("Client disconnected")

async def main():
    print('Connecting to Network...')
    ip = connect_to_network()

    print('Setting up webserver...')
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 80))
    while True:
        onboard.on()
        temp = sensor.temperature
        humidity = sensor.relative_humidity
        oled.fill(0)
        oled.text('Temp.: {:.2f}C'.format(temp), 0, 0)
        oled.text('Umidade: {:.2f}%'.format(humidity), 0, 20)
        oled.text(f'{ip}', 0, 55)
        alto_falante.freq(50)
        oled.show()
        print(f"Temp: {temp}")
        #print(f"dir : {os.listdir('.')}")
        

        await asyncio.sleep(0.25)
        onboard.off()
        await asyncio.sleep(5)
        
try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()