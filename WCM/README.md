# Wireless Communication Module

This document aims to describe the open-source hardware of the wireless communication module used in the BitDogLab project.

It is based on the ESP32-C3 microcontroller (RISC-V), developed by Seeed Studio XIAO, as well as an RFM95W LoRa transceiver.

## Github Structure
```bash
└─── Gerber Files "the following files contain the PCB Fabrication data"
```

## Hardware Description

<img src="./Wireless Communication Module.png" width=40% height=40%>

The developed module, based on the ESP32-C3 (RISC-V) and the RFM95W (SX1276 chip), is designed so that both components are connected via the SPI interface (MOSI, MISO, SCK, RST), along with additional auxiliary pins (DIO0, DIO1, and DIO2), all of which are required to enable full LoRaWAN communication functionality.

The following table shows the pin mapping between the ESP32-C3 and the RFM95W.

| ESP32-C3 | RFM95W |
|----------|--------|
| GND | GND |
| 3,3V | 3,3V |
| D10/MOSI | MOSI |
| D9/MISO | MISO |
| D8/SCK | SCK |
| D0/CS | NSS |
| D2 | RESET |
| D1 | DIO0 |
| D5 | DIO1 |
| D4 | DIO2 |

Regarding the D0/CS pin, it is necessary to use a pull-up resistor (e.g., 10 Ω). This prevents unintended communication with the RFM95W during the ESP32-C3’s startup.

## Physical Connections

The WCM (Wireless Communication Module) enables connection to the BitDogLab through UART and SPI communication when using the 14-pin IDC header, or through UART only when using the 6-pin connector.

For SPI communication, the ESP32-C3 must act as the Master, since the communication between the ESP32-C3 and the RFM95W is SPI-based.

The following table shows the IDC pinout in relation to the ESP32-C3.

<table>
  <tr>
    <td>ESP32-C3</td>
    <td>D8/SCK</td>
    <td>D7/RX</td>
    <td>D6/TX</td>
    <td>D10/MOSI</td>
    <td></td>
    <td>3,3V</td>
    <td>GND</td>
  </tr>
  <tr>
    <td>IDC 14 pins</td>
    <td>GPIO14</td>
    <td>GPIO16</td>
    <td>GPIO17</td>
    <td>GPIO15</td>
    <td>GPIO28</td>
    <td>3,3 V</td>
    <td>GND</td>
  </tr>
  <tr>
    <td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>
  </tr>
  <tr>
    <td>IDC 14 pins</td>
    <td>GPIO18</td>
    <td>GPIO19</td>
    <td>GPIO20</td>
    <td>GPIO4</td>
    <td>GPIO9</td>
    <td>GPIO8</td>
    <td>5 V</td>
  </tr>
  <tr>
    <td>ESP32-C3</td>
    <td>D4/SDA</td>
    <td>D5/SCL</td>
    <td></td>
    <td>D3/CS_RP</td>
    <td>D2/RESET_LORA</td>
    <td>D9/MISO</td>
    <td>5 V</td>
  </tr>
</table>

Next, the following table shows the 6-pin connector configuration.

<table>
  <tr>
    <td>Raspberry Pi Pico</td>
    <td>Key</td>
    <td>5 V</td>
    <td>GND</td>
    <td>GPIO1</td>
    <td>GPIO0</td>
    <td>Stat</td>
  </tr>
  <tr>
    <td>ESP32-C3</td>
    <td></td>
    <td>5 V</td>
    <td>GND</td>
    <td>D6/TX</td>
    <td>D7/RX</td>
    <td></td>
  </tr>
</table>

## Wireless Connections

This module supports three types of wireless connections: BLE and Wi-Fi through the ESP32-C3 chip, and LoRa via the RFM95W module. Both the ESP32-C3 and the RFM95W module have antenna connectors, as shown in the "Hardware Description" section.

The RFM95W module is fully connected to the ESP32-C3. Therefore, in order to use it, the ESP32-C3 must run a code that handles this connection. In other words, the ESP32-C3 is responsible for all network management, which is its main function. Developing a unified library capable of managing all networks within the same code is entirely feasible and is one of the main goals of this module.