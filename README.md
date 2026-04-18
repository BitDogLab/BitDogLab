# BitDogLab V7

An open-source hardware project designed to promote learning in embedded systems, programming, and electronics.

BitDogLab, an initiative of the **Escola 4.0 Project at Unicamp**, is an educational tool devoted to electronics and computing. Based on the **Raspberry Pi Pico H, W, and Pico 2 (RP2350)**, it allows users to explore, assemble, and program using components mounted on its board and also external ones connected in an organized and secure manner.

Meticulously selected, the components foster **hands-on learning**, encouraging users to enhance programming and electronics skills synergistically and progressively. This enriching platform offers a vibrant experience, immersing users in a colourful, auditory, and synesthetic learning environment.

Additionally, BitDogLab is optimized for programming assisted by **Large Language Models (LLMs)**, like ChatGPT, facilitating a more intuitive learning guided by a tireless tutor. Aimed at **pre-university and university education**, BitDogLab aims to catalyze the incorporation of educational technology, providing a robust and flexible tool uniquely integrated into students' learning journey.

---
[![License: CERN-OHL-S v2.0](https://img.shields.io/badge/License-CERN--OHL--S%20v2.0-blue.svg)](https://cern.ch/cern-ohl 

## 🌟 What’s new in Version 7.0

✨ BitDogLab V7 improves upon the solid foundation of V6 with the following updates:

✅ Cost optimization: design adjustments to keep fabrication cost under US$ 25 (≈ R$ 250 in Brazil, including taxes).

✅ Support for Raspberry Pi Pico 2 (RP2350) with dual-core ARM and RISC-V architecture.

✅ Enhanced LED matrix: 5×5 WS2812B RGB array, now using smaller LEDs for better integration.

✅ Display connection updated: OLED now connected to I²C pins GPIO2 (SDA) and GPIO3 (SCL).

✅ New Battery Management System (BMS): integrated INA226 for easy monitoring and control.

✅ Flexible display options: support for OLED modules with 128×64 or 128×128 pixel resolution, expanding visualization capabilities.

✅ Additional input control: inclusion of a third button (A, B, and C), enabling more interactive applications.

✅ Modular microcontroller socket: a new socketed design for the MCU module, allowing future upgrades and simplified maintenance.

---

## 💻 How to Program BitDogLab

BitDogLab supports multiple programming environments, ranging from visual block-based tools for beginners to professional C/C++ development for advanced users.
Below is a step-by-step guide to start programming your board easily using Blockly.

### 🧩 Programming with Blockly (Visual Blocks)

Blockly is the easiest way to get started with BitDogLab — ideal for students and beginners learning programming logic and embedded systems.
You can access it directly online, without installing anything:

👉 Blockly for BitDogLab:
https://bitdoglab-blocos.github.io/BIPES-BITDOGLAB/ui/

Steps to use Blockly:

1) Connect your BitDogLab to your computer using a USB cable.

2) Open the link above in your browser (preferably Chrome or Edge).

3) Select the serial port corresponding to your board.

4) Drag and connect the programming blocks to create your program.

5) Click on “Run” or “Upload” to send the program to your BitDogLab.

⚠️ Important:
If your board already contains a file named main.py in its internal memory, delete it before using Blockly.
The presence of this file can prevent Blockly from communicating properly with the microcontroller.

Tip:

Blockly automatically generates MicroPython code, which can also be viewed and modified in the Thonny IDE if you prefer text-based programming.

###  Programming with MicroPython 

After experimenting with Blockly, you can easily migrate to MicroPython using Thonny IDE with the examples available in the /Firmware/examples/ folder of this repository.
https://gitlab.unicamp.br/fabiano/bitdoglab-v7/-/tree/main/Firmware/examples?ref_type=heads#bitdoglab-micropython-examples

#### 🧰 Tools & Environment
MicroPython with Thonny IDE

Steps:

Flash/update MicroPython firmware on Pico/Pico 2. OBS: Normaly you already received a BitDogLab with a the firmware flashed. 

Connect BitDogLab via USB, select the port under Tools → Interpreter.

Upload the generated script (main.py or similar).

If using Blockly, remove main.py first (it can block communication).


### Quick Guide — Programming BitDogLab with AI (using the BIH)

The simplest workflow to generate code (MicroPython or C/C++) with the help of Artificial Inteligence models using the Hardware Information Database (BIH) — a text file describing the BitDogLab hardware connection is explained bellow:


🔎 What is the BIH

The BIH [Hardware Bank Database (BIH)](https://docs.google.com/document/d/13-68OqiU7ISE8U2KPRUXT2ISeBl3WPhXjGDFH52eWlU/edit?usp=sharing)  is a plain text file containing the pinouts and peripherals of the board/project. It gives technical context so that an LLM (Large Language Model) can write correct code for your BitDogLab, avoiding pin/address mismatches.

#### AI Workflow (Step-by-Step)

1) Open the BIH from the link above.

2) Open your AI assistant (e.g., ChatGPT) and paste the BIH before requesting code.

3) Use a task prompt specifying: target language (MicroPython or C/C++), desired functionality, and constraints. Start with simple tasks.

4) Ask for complete, testable code (with main() or a full script and comments).

5) Iterate: send any compilation/runtime errors back to the AI, always including the BIH and the error log.

Here you can find a visual version of the BIH (Hardware Bank Database). (https://docs.google.com/document/d/1-2Eoo6H1gfTAlxZgFs26p7X4CeaLkS8X8hNTC96PetQ/edit?usp=sharing)


## 📂 Repository Structure
```
under construction ...
```


---


## 🛠️ Hardware Design Files (Open Hardware)

This repository holds **open-source design files** for BitDogLab V7, released under the **CERN Open Hardware Licence v2 – Strongly Reciprocal (CERN-OHL-S)**.  
All files can be freely **copied, manufactured, assembled, and improved** by the community, in alignment with open hardware principles.  

### 📂 Structure of hardware files
```
hardware/
├── kicad/
│ ├── bitdoglab/ → Schematics, PCB layout and gerbers (DIY)
│ ├── bitdoglabsmd/ → Schematics, PCB layout and gerbers (SMD)
│ └── libs/ → Symbols, footprints and 3D models
│
└── docs/
├── BOM/ → Bill of Materials (.xlsx and .csv)
└── fabrication/ → Panelization, pick-and-place, gerber and drill

```

### 🔑 Key Components – BitDogLab V7

- **MCU board:** Raspberry Pi Pico H/W or Pico 2 (RP2350)  
- **LEDs:** RGB LED (common cathode) + 5×5 WS2812B matrix  
- **Inputs:** Buttons A/B + Reset, analog joystick (VRx/VRy + SW)  
- **Audio:** Passive buzzers A and B (stereo capable)  
- **Display:** OLED 128×64 via I²C (GPIO2 = SDA, GPIO3 = SCL)  
- **Sensing:** Electret or MEMS microphone (analog)  
- **Power:** USB 5V, battery charger, **INA226** for monitoring (BMS)  
- **Expansion:** IDC header exposing GPIOs, I²C/SPI/UART, 3V3/5V/GND  

### 📐 Hardware Schematic

The [annotated schematic of BitDogLab V7](https://docs.google.com/document/d/1cR74ubS8tIO2sSQk1Hf8aKo57Ta3R8EJL4mGiqV2mH0/edit?usp=sharing) describes the complete circuit, including the MCU pins, power supply, LEDs, buzzers, joystick, display, sensors, and connectors. A [high-resolution schematic diagram] is also available.

The complete **schematics of BitDogLab V7** are available in this [**document**](https://docs.google.com/document/d/1cR74ubS8tIO2sSQk1Hf8aKo57Ta3R8EJL4mGiqV2mH0/edit?usp=sharing). .  
They describe the entire circuit, including MCU pins, power supply, LEDs, buzzers, joystick, display, sensors, and connectors.

- **Fabrication Files (version 7) with PCB and assembly with SMD componentes:** [**Gerber + BOM + Pick Place**](https://drive.google.com/drive/folders/1TGEBqiHnaR470X9izp0-9XtS-pPj8GxW?usp=sharing
)


> The schematic is the starting point for anyone wishing to understand, replicate, or modify BitDogLab.  
> It ensures **full transparency** in the design, reinforcing the open hardware philosophy of this project.


### 📑 Bill of Materials (BOM)

- **Spreadsheet (Google Sheets):** [BOM](https://docs.google.com/spreadsheets/d/1lPjkUmOSgNfBfdC2lzMRuLAa2dZAN5wuEols-8MtYGg/edit?usp=sharing)  


---

## 📚 Hardware Database


- **Português**: [Banco de Informação de Hardware (BIH)](https://docs.google.com/document/d/13-68OqiU7ISE8U2KPRUXT2ISeBl3WPhXjGDFH52eWlU/edit?usp=sharing)  

---

## 📜 License

This project is licensed under:  
- **CERN Open Hardware Licence v2 – Strongly Reciprocal (CERN-OHL-S)** for hardware  
- **MIT** for software and firmware  

---

## 🤝 Sponsors & Support

- **IEEE-EDS**: STEM outreach program  
- **CNPq – INCT Namitec**  

---

## 👨‍🏫 Authors and Acknowledgment

- **Prof. Dr. Fabiano Fruett** – Project coordination and development  
- Contributors: students and collaborators from **Escola 4.0 / FEEC – Unicamp** 
