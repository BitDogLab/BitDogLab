# Projects

[English](#english) | [Portugues](#portugues)

## English

This folder contains BitDogLab projects, experiments, examples, tools, and hardware expansion projects. It is intended for complete or exploratory code that is larger than a clean beginner example.

Basic, beginner-friendly examples will be kept separately in the root `basic-examples/` folder.

### Folder structure

| Folder | Purpose |
|---|---|
| `hardware-examples/` | Existing examples focused on onboard hardware such as LEDs, buttons, buzzer, joystick, OLED display, microphone, I2C, and the LED matrix. |
| `sensor-examples/` | Existing examples focused on external or onboard sensors, such as accelerometers, light sensors, BME280/BME680, and presence sensors. |
| `hardware-expansion/` | Projects that involve custom hardware, expansion boards, shields, Gerber files, KiCad files, mechanical parts, or dedicated external modules. |
| `application-examples/` | Small application-oriented examples that combine multiple features for a specific use case. |
| `tools/` | Auxiliary software, web tools, visual interfaces, external examples, or support projects. |

### Hardware expansion projects

The `hardware-expansion/` folder includes projects that are not only software examples. These projects may include PCB files, Gerbers, CAD models, custom shields, expansion boards, or mechanical parts.

Current examples:

- `wireless-communication-module/`: wireless communication module previously stored as `WCM`.
- `RoboMovel/`: mobile robot project with code, mechanical files, and custom board files.
- `LoRa_Shield/`: LoRa shield related code and support files.
- `Expansao_PWM/`: software support for a PWM expansion board.

### Notes

Some projects in this folder are legacy, experimental, or still being reviewed for BitDogLab v7. Before using them as official v7 examples, check the pin assignments, especially OLED I2C pins, buzzer pins, and any external sensor connections.

## Portugues

Esta pasta contem projetos, experimentos, exemplos, ferramentas e projetos com expansao de hardware da BitDogLab. Ela e destinada a codigos completos ou exploratorios, maiores do que um exemplo basico e limpo para iniciantes.

Os exemplos basicos e didaticos ficarao separados na pasta `basic-examples/`, na raiz do repositorio.

### Estrutura de pastas

| Pasta | Finalidade |
|---|---|
| `hardware-examples/` | Exemplos existentes focados no hardware da placa, como LEDs, botoes, buzzer, joystick, display OLED, microfone, I2C e matriz de LEDs. |
| `sensor-examples/` | Exemplos existentes focados em sensores externos ou embarcados, como acelerometros, sensores de luz, BME280/BME680 e sensores de presenca. |
| `hardware-expansion/` | Projetos que envolvem hardware proprio, placas expansoras, shields, arquivos Gerber, arquivos KiCad, partes mecanicas ou modulos externos dedicados. |
| `application-examples/` | Pequenos exemplos de aplicacao que combinam varios recursos para um uso especifico. |
| `tools/` | Softwares auxiliares, ferramentas web, interfaces visuais, exemplos externos ou projetos de apoio. |

### Projetos com expansao de hardware

A pasta `hardware-expansion/` inclui projetos que nao sao apenas exemplos de software. Esses projetos podem conter arquivos de PCB, Gerbers, modelos CAD, shields personalizados, placas expansoras ou partes mecanicas.

Exemplos atuais:

- `wireless-communication-module/`: modulo de comunicacao sem fio que antes estava como `WCM`.
- `RoboMovel/`: projeto de robo movel com codigo, arquivos mecanicos e arquivos de placa propria.
- `LoRa_Shield/`: codigo e arquivos de apoio relacionados ao shield LoRa.
- `Expansao_PWM/`: suporte de software para uma placa expansora PWM.

### Observacoes

Alguns projetos nesta pasta sao legados, experimentais ou ainda estao em revisao para a BitDogLab v7. Antes de usa-los como exemplos oficiais v7, confira a pinagem, principalmente os pinos I2C do display OLED, os pinos de buzzer e as conexoes de sensores externos.
