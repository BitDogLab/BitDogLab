# Software Libraries

[English](#english) | [Portugues](#portugues)

## English

This folder contains reusable software libraries for BitDogLab projects, mainly MicroPython modules used by examples, projects, and firmware running on Raspberry Pi Pico/Pico W/Pico 2.

These files are kept separate from project code so they can be copied to the board or imported by multiple examples without duplicating the same drivers in each project.

### Available libraries

- `ssd1306.py`: OLED display driver for SSD1306 displays.
- `neopixel.py`: NeoPixel/WS2812 LED matrix support.
- `matriz_bdl.py`: helper functions for the BitDogLab LED matrix.
- `ahtx0.py`: AHT20/AHTx0 temperature and humidity sensor driver.
- `bh1750.py` and `BH1750_alt.py`: BH1750 light sensor drivers.
- `bme280.py`: BME280 temperature, humidity, and pressure sensor driver.
- `mpu6500.py`, `mpu9250.py`, `ak8963.py`: motion sensor and magnetometer drivers.
- `micropyGPS.py`: GPS parsing library.
- `operator.py`: compatibility/helper module used by some MicroPython code.
- `manifest.py` and `manifest_pico_w.py`: MicroPython manifest files.

### I2C connections on BitDogLab v7

BitDogLab v7 uses two main I2C pin groups:

| Use | Bus | SDA | SCL |
|---|---:|---:|---:|
| External sensors | I2C0 | GPIO0 | GPIO1 |
| OLED display | I2C1 | GPIO2 | GPIO3 |

For the OLED display, use:

```python
from machine import Pin, I2C

i2c_display = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
```

For external I2C sensors, use:

```python
from machine import Pin, I2C

i2c_sensors = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
```

When writing new BitDogLab v7 examples, prefer these pin assignments to avoid conflicts with older v6 examples.

## Portugues

Esta pasta contem bibliotecas de software reutilizaveis para projetos da BitDogLab, principalmente modulos MicroPython usados por exemplos, projetos e firmwares executados no Raspberry Pi Pico/Pico W/Pico 2.

Esses arquivos ficam separados dos codigos dos projetos para que possam ser copiados para a placa ou importados por varios exemplos sem duplicar os mesmos drivers em cada projeto.

### Bibliotecas disponiveis

- `ssd1306.py`: driver para display OLED SSD1306.
- `neopixel.py`: suporte para matriz NeoPixel/WS2812.
- `matriz_bdl.py`: funcoes auxiliares para a matriz de LEDs da BitDogLab.
- `ahtx0.py`: driver para sensor AHT20/AHTx0 de temperatura e umidade.
- `bh1750.py` e `BH1750_alt.py`: drivers para sensor de luz BH1750.
- `bme280.py`: driver para sensor BME280 de temperatura, umidade e pressao.
- `mpu6500.py`, `mpu9250.py`, `ak8963.py`: drivers para sensores de movimento e magnetometro.
- `micropyGPS.py`: biblioteca para interpretacao de dados GPS.
- `operator.py`: modulo auxiliar/de compatibilidade usado por alguns codigos MicroPython.
- `manifest.py` e `manifest_pico_w.py`: arquivos de manifesto do MicroPython.

### Conexoes I2C na BitDogLab v7

A BitDogLab v7 usa dois grupos principais de pinos I2C:

| Uso | Barramento | SDA | SCL |
|---|---:|---:|---:|
| Sensores externos | I2C0 | GPIO0 | GPIO1 |
| Display OLED | I2C1 | GPIO2 | GPIO3 |

Para o display OLED, use:

```python
from machine import Pin, I2C

i2c_display = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
```

Para sensores externos I2C, use:

```python
from machine import Pin, I2C

i2c_sensors = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
```

Ao escrever novos exemplos para a BitDogLab v7, prefira essa pinagem para evitar conflitos com exemplos antigos da v6.
