# COMECE POR AQUI: BitDogLab v7 com MicroPython

[Português](#português) | [English](#english)

## Português

**Table of Contents**

- [COMECE POR AQUI: BitDogLab v7 com MicroPython](#comece-por-aqui-bitdoglab-v7-com-micropython)
  - [Objetivo](#objetivo)
  - [Antes de começar](#antes-de-começar)
  - [Instalando a Thonny IDE](#instalando-a-thonny-ide)
  - [Configurando o interpretador MicroPython](#configurando-o-interpretador-micropython)
  - [Gravação do firmware](#gravação-do-firmware)
  - [Alternativas de gravação de firmware](#alternativas-de-gravação-de-firmware)
  - [Executando o primeiro teste da placa](#executando-o-primeiro-teste-da-placa)
  - [Salvando o código como main.py](#salvando-o-código-como-mainpy)
  - [O que observar durante o teste](#o-que-observar-durante-o-teste)

## Objetivo

Este guia apresenta o fluxo inicial para começar a usar a **BitDogLab v7** com **MicroPython** e a **Thonny IDE**.

Ao final deste procedimento, a placa estará pronta para receber códigos Python. O primeiro teste recomendado é copiar o código de verificação geral dos periféricos, colar na Thonny IDE e salvar na placa com o nome `main.py`.

Neste repositório, o código de teste está em:

```text
testar_perifericos_gerais.py
```

Esse arquivo funciona como o teste geral de periféricos da BitDogLab v7.

## Antes de começar

Você vai precisar de:

- uma placa BitDogLab v7;
- um cabo USB compatível com a Raspberry Pi Pico/Pico W/Pico 2 usada na placa;
- um computador com Windows, Linux ou macOS;
- a Thonny IDE instalada;
- o arquivo de teste geral dos periféricos.

Antes de instalar o firmware, localize o botão `BOOTSEL` da Raspberry Pi Pico/Pico W/Pico 2 instalada na BitDogLab.

<img src="images/start/parte_tras_placa_botao_bootloader%20destacado.png" width=70% height=70%>

O botão `BOOTSEL` é usado para colocar a placa em modo de gravação de firmware. Para executar programas normalmente, conecte a placa sem pressionar esse botão.

## Instalando a Thonny IDE

Para programar a BitDogLab com MicroPython, o primeiro passo é instalar a Thonny IDE. Ela é o ambiente onde escrevemos, salvamos e executamos o código na placa.

Acesse a página oficial:

https://thonny.org/

Em seguida, escolha a opção correta para o seu sistema operacional.

Windows:

<img src="doc/Bitdoglab%20V6/illustrations/thonny-windows.png" width=60% height=60%>

Mac:

<img src="doc/Bitdoglab%20V6/illustrations/thonny-mac.png" width=60% height=60%>

Linux:

<img src="doc/Bitdoglab%20V6/illustrations/thonny-linux.png" width=60% height=60%>

Com o arquivo baixado, instale a Thonny IDE seguindo os passos do instalador. Assim que a instalação for concluída, abra a IDE.

## Configurando o interpretador MicroPython

A configuração principal da Thonny é a escolha do interpretador usado para executar os códigos.

Na Thonny IDE, acesse:

```text
Tools > Options
```

<img src="doc/Bitdoglab%20V6/illustrations/thonny-tools-options.png" width=80% height=80%>

Na janela de configurações, acesse a aba `Interpreter` e selecione:

```text
MicroPython (Raspberry Pi Pico)
```

<img src="doc/Bitdoglab%20V6/illustrations/thonny-interpreter.png" width=60% height=60%>

A porta serial da placa normalmente é detectada automaticamente pela Thonny. Se houver mais de uma placa conectada, selecione manualmente a porta correspondente à BitDogLab.

## Gravação do firmware

Com a Thonny configurada, é necessário gravar o firmware MicroPython na placa.

Para isso:

1. Desconecte a BitDogLab do computador.
2. Pressione e segure o botão `BOOTSEL`.
3. Mantendo o botão pressionado, conecte o cabo USB ao computador.
4. Depois que a placa for reconhecida, solte o botão.

<img src="images/start/aperta_botao.png" width=60% height=60%>

<img src="images/start/conecta_usb.png" width=60% height=60%>

Esse procedimento faz com que a placa entre em modo de gravação de firmware. O computador deve reconhecê-la como um disco removível chamado `RPI-RP2`.

<img src="doc/Bitdoglab%20V6/illustrations/RPI-RP2.png" width=25% height=25%>

Com a placa em modo bootloader, volte à aba `Interpreter` da Thonny. A janela deve mostrar a opção para instalar ou atualizar o firmware.

<img src="doc/Bitdoglab%20V6/illustrations/thonny-port-install-update.png" width=60% height=60%>

Clique em:

```text
Install or update firmware
```

Na janela seguinte, confira se o dispositivo selecionado é a Raspberry Pi Pico/Pico W/Pico 2 correta.

<img src="doc/Bitdoglab%20V6/illustrations/select-pipico.png" width=60% height=60%>

Em seguida, instale a versão desejada do MicroPython.

<img src="doc/Bitdoglab%20V6/illustrations/install-micropython.png" width=60% height=60%>

Aguarde até que a instalação termine. Ao final, feche a janela de instalação, desconecte a placa e conecte novamente sem pressionar `BOOTSEL`.

Agora a BitDogLab está pronta para receber códigos Python.

## Alternativas de gravação de firmware

Também é possível gravar o firmware manualmente por drag-and-drop.

Nesse método, a placa deve estar em modo bootloader e aparecer como disco `RPI-RP2`. Depois, basta copiar o arquivo `.uf2` do firmware para esse disco.

Firmware oficial MicroPython:

- Raspberry Pi Pico: https://micropython.org/download/RPI_PICO/
- Raspberry Pi Pico W: https://micropython.org/download/RPI_PICO_W/

## Executando o primeiro teste da placa

Com a configuração finalizada e o firmware MicroPython instalado, o próximo passo é executar o teste geral dos periféricos.

Abra o arquivo:

```text
testar_perifericos_gerais.py
```

Copie todo o conteúdo do arquivo e cole na área principal da Thonny IDE.

<img src="images/start/codigo_colado.png" width=80% height=80%>

Esse teste foi pensado para validar, em sequência, os principais recursos da BitDogLab v7, incluindo:

- LED RGB;
- matriz de LEDs RGB 5x5;
- botões A e B;
- botão do joystick;
- joystick analógico;
- buzzer;
- display OLED;
- microfone.

## Salvando o código como main.py

Para que a placa execute o teste automaticamente, salve o código na memória da Raspberry Pi Pico/Pico W/Pico 2 com o nome `main.py`.

Na Thonny, clique em:

```text
File > Save as...
```

Escolha salvar no dispositivo:

```text
Raspberry Pi Pico
```

<img src="images/start/salvar_como_raspberry_pi_pico.png" width=60% height=60%>

Na janela de nome do arquivo, digite:

```text
main.py
```

<img src="images/start/salvar_main.py.png" width=60% height=60%>

Depois de salvar, confira se o arquivo aparece na lista de arquivos da placa.

<img src="images/start/aquivos_salvar_com_localizao.png" width=80% height=80%>

O nome `main.py` é importante porque o MicroPython executa automaticamente esse arquivo quando a placa inicia.

## Executando o código

Com o arquivo salvo na placa, pressione o botão `Run` da Thonny para executar o código.

<img src="images/start/executar_codigo.png" width=60% height=60%>

Se o arquivo foi salvo como `main.py`, a BitDogLab também executará esse teste automaticamente sempre que for ligada ou reiniciada.

## O que observar durante o teste

Durante a execução, observe se:

- a matriz de LEDs exibe animações;
- o LED RGB muda de cor;
- o display OLED mostra mensagens;
- o buzzer emite sons;
- os botões A e B respondem quando pressionados;
- o joystick altera o comportamento esperado;
- o botão do joystick responde;
- o microfone altera a visualização de intensidade sonora.

Se algo não funcionar, confira:

- se a placa correta está selecionada na Thonny;
- se o firmware MicroPython foi instalado corretamente;
- se a placa foi reconectada sem pressionar `BOOTSEL`;
- se o arquivo foi salvo exatamente como `main.py`;
- se as bibliotecas necessárias, como `ssd1306.py` e `neopixel.py`, estão disponíveis na placa.

As bibliotecas reutilizáveis do repositório estão organizadas em:

```text
libs_software/
```

Depois de validar a placa com esse teste geral, o próximo passo é estudar exemplos menores e isolados em:

```text
basic-examples/
```

Essa pasta deve conter exemplos curtos, didáticos e focados em um periférico por vez.

## English

**Table of Contents**

- [Start Here: BitDogLab v7 with MicroPython](#start-here-bitdoglab-v7-with-micropython)
  - [Goal](#goal)
  - [Before You Start](#before-you-start)
  - [Installing Thonny IDE](#installing-thonny-ide)
  - [Configuring the MicroPython Interpreter](#configuring-the-micropython-interpreter)
  - [Flashing the MicroPython Firmware](#flashing-the-micropython-firmware)
  - [Alternative Firmware Flashing Method](#alternative-firmware-flashing-method)
  - [Running the First Board Test](#running-the-first-board-test)
  - [Saving the Code as main.py](#saving-the-code-as-mainpy)
  - [What to Check During the Test](#what-to-check-during-the-test)

## Start Here: BitDogLab v7 with MicroPython

This guide shows the initial workflow for using **BitDogLab v7** with **MicroPython** and the **Thonny IDE**.

At the end of this procedure, the board will be ready to receive Python code. The recommended first test is to copy the general peripheral test code, paste it into Thonny IDE, and save it on the board as `main.py`.

In this repository, the test code is:

```text
testar_perifericos_gerais.py
```

This file works as the general peripheral self-test for BitDogLab v7.

## Goal

This guide explains how to:

- install and open Thonny IDE;
- configure Thonny for MicroPython;
- put the board into bootloader mode;
- install or update MicroPython;
- copy the BitDogLab v7 peripheral test code;
- save the code on the board as `main.py`;
- run and observe the first hardware test.

## Before You Start

You will need:

- a BitDogLab v7 board;
- a USB cable compatible with the Raspberry Pi Pico/Pico W/Pico 2 used on the board;
- a Windows, Linux, or macOS computer;
- Thonny IDE installed;
- the general peripheral test file.

Before installing MicroPython, locate the `BOOTSEL` button on the Raspberry Pi Pico/Pico W/Pico 2 installed on BitDogLab.

<img src="images/start/parte_tras_placa_botao_bootloader%20destacado.png" width=70% height=70%>

The `BOOTSEL` button is used to put the board into firmware flashing mode. To run programs normally, connect the board without pressing this button.

## Installing Thonny IDE

To program BitDogLab with MicroPython, first install Thonny IDE. It is the environment used to write, save, and run code on the board.

Open the official page:

https://thonny.org/

Choose the correct installer for your operating system.

Windows:

<img src="doc/Bitdoglab%20V6/illustrations/thonny-windows.png" width=60% height=60%>

Mac:

<img src="doc/Bitdoglab%20V6/illustrations/thonny-mac.png" width=60% height=60%>

Linux:

<img src="doc/Bitdoglab%20V6/illustrations/thonny-linux.png" width=60% height=60%>

After downloading the installer, install Thonny IDE and open it.

## Configuring the MicroPython Interpreter

In Thonny IDE, open:

```text
Tools > Options
```

<img src="doc/Bitdoglab%20V6/illustrations/thonny-tools-options.png" width=80% height=80%>

In the settings window, open the `Interpreter` tab and select:

```text
MicroPython (Raspberry Pi Pico)
```

<img src="doc/Bitdoglab%20V6/illustrations/thonny-interpreter.png" width=60% height=60%>

Thonny usually detects the board serial port automatically. If more than one board is connected, manually select the port that belongs to BitDogLab.

## Flashing the MicroPython Firmware

With Thonny configured, install MicroPython on the board.

1. Disconnect BitDogLab from the computer.
2. Press and hold the `BOOTSEL` button.
3. While holding the button, connect the USB cable to the computer.
4. Once the board is detected, release the button.

<img src="images/start/aperta_botao.png" width=60% height=60%>

<img src="images/start/conecta_usb.png" width=60% height=60%>

The computer should recognize the board as a removable drive named `RPI-RP2`.

<img src="doc/Bitdoglab%20V6/illustrations/RPI-RP2.png" width=25% height=25%>

With the board in bootloader mode, return to the `Interpreter` tab in Thonny. The window should show the option to install or update the firmware.

<img src="doc/Bitdoglab%20V6/illustrations/thonny-port-install-update.png" width=60% height=60%>

Click:

```text
Install or update firmware
```

Confirm that the selected device is the correct Raspberry Pi Pico/Pico W/Pico 2.

<img src="doc/Bitdoglab%20V6/illustrations/select-pipico.png" width=60% height=60%>

Then install the desired MicroPython version.

<img src="doc/Bitdoglab%20V6/illustrations/install-micropython.png" width=60% height=60%>

Wait until the installation finishes. Then close the installation window, disconnect the board, and reconnect it without pressing `BOOTSEL`.

BitDogLab is now ready to receive Python code.

## Alternative Firmware Flashing Method

You can also install firmware manually by drag-and-drop.

In this method, the board must be in bootloader mode and appear as the `RPI-RP2` drive. Then copy the `.uf2` firmware file to that drive.

Official MicroPython firmware:

- Raspberry Pi Pico: https://micropython.org/download/RPI_PICO/
- Raspberry Pi Pico W: https://micropython.org/download/RPI_PICO_W/

## Running the First Board Test

After installing MicroPython, run the general peripheral test.

Open the file:

```text
testar_perifericos_gerais.py
```

Copy the whole file and paste it into the main editor area in Thonny IDE.

<img src="images/start/codigo_colado.png" width=80% height=80%>

This test validates the main BitDogLab v7 resources, including:

- RGB LED;
- 5x5 RGB LED matrix;
- buttons A and B;
- joystick button;
- analog joystick;
- buzzer;
- OLED display;
- microphone.

## Saving the Code as main.py

To make the board run the test automatically, save the code on the Raspberry Pi Pico/Pico W/Pico 2 memory as `main.py`.

In Thonny, click:

```text
File > Save as...
```

Choose:

```text
Raspberry Pi Pico
```

<img src="images/start/salvar_como_raspberry_pi_pico.png" width=60% height=60%>

Name the file:

```text
main.py
```

<img src="images/start/salvar_main.py.png" width=60% height=60%>

After saving, check that the file appears in the board file list.

<img src="images/start/aquivos_salvar_com_localizao.png" width=80% height=80%>

The name `main.py` is important because MicroPython automatically runs this file when the board starts.

## Running the Code

With the file saved on the board, press Thonny's `Run` button.

<img src="images/start/executar_codigo.png" width=60% height=60%>

If the file was saved as `main.py`, BitDogLab will also run this test automatically whenever it is powered on or restarted.

## What to Check During the Test

During the test, check whether:

- the LED matrix shows animations;
- the RGB LED changes color;
- the OLED display shows messages;
- the buzzer emits sounds;
- buttons A and B respond when pressed;
- the joystick changes the expected behavior;
- the joystick button responds;
- the microphone changes the sound intensity visualization.

If something does not work, check:

- whether the correct board is selected in Thonny;
- whether MicroPython was installed correctly;
- whether the board was reconnected without pressing `BOOTSEL`;
- whether the file was saved exactly as `main.py`;
- whether required libraries such as `ssd1306.py` and `neopixel.py` are available on the board.

Reusable software libraries from this repository are organized in:

```text
libs_software/
```

After validating the board with this general test, continue with smaller isolated examples in:

```text
basic-examples/
```

This folder should contain short educational examples focused on one peripheral at a time.
