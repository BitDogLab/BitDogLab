# BH1750
Micropython module for BH1750 ambient light sensor.

Just connect your BH1750 board to Arduino, ESP or any other board with MicroPython firmware.

Supply voltage BH1750 3.3 or 5.0 volts! Use four wires to connect (I2C).
1. +VCC (Supply voltage)
2. GND
3. SDA
4. SCL

Upload micropython firmware to the NANO(ESP, etc) board, and then four *.py files: main.py, bh1750.py,
bus_service.py, base_sensor.py. 
Then open main.py in your IDE and run it.

# Pictures
## IDE
![alt text](https://github.com/octaprog7/BH1750/blob/master/ide1750.png)
## Breadboard
![alt text](https://github.com/octaprog7/BH1750/blob/master/bh1750board.jpg)
