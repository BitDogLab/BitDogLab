# [PT-BR] Manual BitDogLab (Iniciando com Micropython)

**Table of Contents**

- [[PT-BR] Manual BitDogLab (Iniciando com Micropython)](https://github.com/BitDogLab/BitDogLab/tree/main/doc#pt-br-manual-bitdoglab-iniciando-com-micropython)

	- [Conteúdo material](https://github.com/BitDogLab/BitDogLab/tree/main/doc#conte%C3%BAdo-material)

	- [Montando a BitDogLab](https://github.com/BitDogLab/BitDogLab/tree/main/doc#montando-a-bitdoglab)

	- [Especificação/Periféricos da BitDogLab v5.3](https://github.com/BitDogLab/BitDogLab/tree/main/doc#especifica%C3%A7%C3%A3operif%C3%A9ricos-da-bitdoglab-v53)

	- [Iniciando com MicroPython](https://github.com/BitDogLab/BitDogLab/tree/main/doc#iniciando-com-micropython)

		- [Gravação do firmware](https://github.com/BitDogLab/BitDogLab/tree/main/doc#grava%C3%A7%C3%A3o-do-firmware)

			- [Alternativas de gravação de firmware](https://github.com/BitDogLab/BitDogLab/tree/main/doc#alternativas-de-grava%C3%A7%C3%A3o-de-firmware)

	- [Executando primeiro exemplo de código](https://github.com/BitDogLab/BitDogLab/tree/main/doc#executando-primeiro-exemplo-de-c%C3%B3digo)


A **BitDogLab**, é uma iniciativa que partiu do projeto escola 4.0 na Unicamp, uma ferramenta educacional voltada para o aprendizado de computação embarcada e eletrônica. Baseada no dispositivo Raspberry Pi Pico H ou W (wifi/bluetooth), a BitDogLab permite ao usuário explorar, montar e programar usando componentes montados nesta placa além de componentes adicionais externos (periféricos) conectados em uma forma organizada e estruturada. Meticulosamente selecionados, os componentes fomentam o aprendizado com "mãos na massa", encorajando os usuários a evoluírem suas habilidades em programação embarcada e eletrônica de forma progressiva e sinérgica. Essa plataforma rica oferece uma experiência vibrante, This enriching platform offers a vibrant experience, provendo imersão dos usuários em um ambiente de aprendizado colorido, autoral e sinestésico. Adicionalmente a BitDogLab é otimizada para programação assistida por meio de large language models (LLM), como o GPT-4o, facilitando uma aprendizagem mais intuitiva guiada por um tutor incansável.

Objetivando a educação pré-universitária (12+), BitDogLab busca catalizar e incorporar a educação tecnológica, provendo uma ferramenta robusta e flexível únicamente integrada com a jornada de aprendizado dos estudantes.

## Conteúdo material

A bitdoglab vem uma caixa padrão de correio (16x11x5 cm) como a ilustrada abaixo.

<img src="./illustrations/box.png" width=40% height=40%>

Dentro da caixa você encontra a BitDogLab envolta em um envelope anti-estático, um cabo tipo micro-usb para usb-a e a capa do joystick analógico da BitDogLab.

<img src="./illustrations/open-box.png" width=40% height=40%>

Cabo tipo micro-usb para usb-a

<img src="./illustrations/microusb-usba.png" width=25% height=25%>

Capa do joystick

<img src="./illustrations/joystick-cap.png" width=25% height=25%>

## Montando a BitDogLab

Retire a placa do envelope anti-estático.

<img src="./illustrations/bitdoglab-antistaticbag.png" width=70% height=70%>

Plugue a capa do joystick na BitDogLab como ilustrado abaixo.

<img src="./illustrations/joystick-cap-bitdoglab.png" width=40% height=40%>

Dessa forma a BitDogLab estará pronta para uso

<img src="./illustrations/joystick-assembled.png" width=40% height=40%>

## Especificação/Periféricos da BitDogLab v5.3

<img src="https://github.com/BitDogLab/BitDogLab/blob/main/kicad/bitdoglabsmd/bitdoglab_main/bitdoglab_smd_top.jpg" width=40% height=40%>
<img src="https://github.com/BitDogLab/BitDogLab/blob/main/kicad/bitdoglabsmd/bitdoglab_main/bitdoglab_smd_bot.jpg" width=40% height=40%>

A Placa BitDogLab é uma plataforma completa indicada para ensino de software/sistemas embarcados.
O módulo Microcontrolador é o cérebro da placa, composto pelo microcontrolador [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html "Raspberry Pi Pico W") com as seguintes especificações:
- Microcontrolador RP2040 microcontroller
- Módulo castelado para soldagem direta na placa base BitDogLab
- Processador Dual-core Arm Cortex-M0+, clock flexivel até 133 MHz
- 264kB SRAM e 2MB QSPI flash embarcado
- Rede sem fio do tipo LAN 2.4GHz 802.11n
- Bluetooth 5.2
- 26 pinos multifuncionais (GPIO), incluindo 3 pinos analógicos
- Controladores: 2 × UART, 2 × SPI, 2 × I2C e 16 canais PWM 
- Controlador USB 1.1 com PHY, suportando modos host e device
- 8x I/Os programáveis (PIO) por meio de máquinas de estado para periféricos customizados
- Tensão de entrada de 1.8–5.5V DC
- Temperatura de operação de -20°C to +70°C
- Programação do tipo Drag-and-drop usando mass storage USB
- Modo de operação de baixo consumo e dormente
- Clock preciso e sensor de temperatura embarcado
- Bibliotecas de aceleração de cálculos inteiros e de ponto flutuante no chip

Pinout Raspberry Pi Pico W

<img src="https://github.com/BitDogLab/BitDogLab/blob/main/doc/illustrations/picow-pinout.svg" width=70% height=70%>

Lista de periféricos embarcados na placa BitDogLab:
1) A BitDogLab possui uma Bateria 3.7V 2200Mah Li-Ion CR18650 e seu devido suporte de bateria.

<img src="./illustrations/battery.png" width=50% height=50%>

2) LED Colorido (SMD5050 RGB LEDs ROHS)

<img src="./illustrations/led-rgb.png" width=25% height=25%>

3) Display OLED (0.96 polegadas I2C 128x64 oled display)

<img src="./illustrations/oled.png" width=25% height=25%>

4) Matriz de LEDs coloridos (LED-RGB 5x5 5050 WS2812)

<img src="./illustrations/led-rgb-array.png" width=30% height=30%>

5) Microfone com amplificador de áudio (MAX4466EXK)

<img src="./illustrations/mic.png" width=25% height=25%>

6) Joystick Analógico (Plugin 13x13mm Multi-Dir ROHS)

<img src="./illustrations/analog-joystick.png" width=25% height=25%>

7) Botões (A e B) - Chave Táctil 12x12x7.5 mm

<img src="./illustrations/buttons.png" width=60% height=60%>

8) Buzzers (Esquerdo e Direito) - 80dB Externally Driven Magnetic 2.7kHz SMD, 8.5x8.5mm Buzzers ROHS

<img src="./illustrations/stereo-buzzers.png" width=60% height=60%>

9) Conectores de sensores de expansão I2C (1 e 0) - 2.5mm Plugin,P=2.5mm Wire To Board Connector ROHS
- I2C1 (pino 1 – esquerda)
	- 1: GP3 (SCL I2C1)
	- 2: GP2 (SDA I2C1)
	- 3: 3.3V
	- 4: GND referencia
- I2C0 (pino 1 – esquerda)
	- 1: GP1 (SCL I2C0)
	- 2: GP0 (SDA I2C0)
	- 3: 3.3V
	- 4: GND referencia

<img src="./illustrations/i2c-sensor-actuator.png" width=50% height=50%>

10) Circuito de gerenciamento de energia - IP5306 ESOP-8 Battery Management ICs ROHS (Fully-Integrated Power Bank System-On-Chip with 2.1A charger, 2.4A discharger)

<img src="./illustrations/battery-charger.png" width=25% height=25%>

11) Conector de expansão de GPIOs (pino 1 canto superior esquerdo) - 2.54mm Straight Gold Brass 2x7P 7 Push - Pull P=2.54mm IDC Connectors ROHS
- 1: GND referencia
- 2: VSYS (5V)
- 3: 3.3V
- 4: GP8
- 5: GP28
- 6: GP9
- 7: AGND
- 8: GP4
- 9: GP17
- 10: GP20
- 11: GP16
- 12: GP19
- 13: GND referencia
- 14: GP18

<img src="./illustrations/idc-connector.png" width=20% height=20%>

12) Botão de reset - 8mm Round Button Brick nogging SPST SMD Tactile Switches ROHS

<img src="./illustrations/reset-button.png" width=25% height=25%>

13) Conector para painel solar (6V) - 1x2P -40℃~+105℃ 8A 130V Green 18~26 Straight 2.54mm 0.5~1 1 2 Plugin,P=2.54mm Screw terminal ROHS

<img src="./illustrations/solar-conn.png" width=25% height=25%>

14) Conector para bateria externa - 1x2P -40℃~+105℃ 8A 130V Green 18~26 Straight 2.54mm 0.5~1 1 2 Plugin,P=2.54mm Screw terminal ROHS

<img src="./illustrations/ext-battery.png" width=25% height=25%>

15) Chave liga-desliga (um toque = liga, dois toques em menos de 1 segundo = desliga)

<img src="./illustrations/on-off-button.png" width=25% height=25%>

16) Pinos e expansão para painel compatível com garras jacaré ou parafusos (1x5 header esquerdo e direito, cor preta)
- 1x5 header esquerdo J5 (pino 5 na esquerda, pino 1 na direita):
	- 5: AGND
	- 4: GP28 (se solder jumper JP1 ativo)
	- 3: GND referencia
	- 2: 3.3V
	- 1: VSYS (5V)
- 1x5 header direito J12 (pino 5 na esquerda, pino 1 na direita):
	- 5: GND
	- 4: GP0
	- 3: GP1
	- 2: GP2
	- 1: GP3

<img src="./illustrations/expansion-pins.png" width=60% height=60%>
<img src="./illustrations/i2c-ext-pin.png" width=60% height=60%>

17) Jumper de seleção de conversor analógico digital (pino ANA-IN no painel jacaré ou microfone), pino 1 indicado com marcação J1

<img src="./illustrations/jumper-analog-in.png" width=10% height=10%>

## Iniciando com MicroPython

Para programar a Raspberry Pi Pico ou Pico W, precisamos realizar duas configurações iniciais, que são a configuração da Thonny IDE e a gravação do firmware para a linguagem Python.

O primeiro passo para a programação da placa é a instalação da Thonny IDE, que é o ambiente onde desenvolvemos e pelo qual gravamos o código na placa. Para isso, acesse a página de download da IDE abaixo.
https://thonny.org/

Em seguida então escolha a opção certa para o seu sistema operacional, como mostrado abaixo quando você posicionar o mouse no sistema operacional desejado.
Windows:

<img src="./illustrations/thonny-windows.png" width=60% height=60%>

Mac:

<img src="./illustrations/thonny-mac.png" width=60% height=60%>

Linux:

<img src="./illustrations/thonny-linux.png" width=60% height=60%>

Com o arquivo baixado (em computadores Windows ou macOS), instale a Thonny IDE seguindo os passos do instalador. Em computadores Linux a instalação será feita automaticamente com o envio do comando no terminal. Assim que a instalação da IDE for concluída, abra-a.

A configuração que precisa ser feita na Thonny IDE para a programação da Raspberry Pi Pico é alterar o interpretador que será usado para a execução do código. Para isso, acesse as configurações da IDE, seguindo o caminho a seguir (Tools > Options).

<img src="./illustrations/thonny-tools-options.png" width=80% height=80%>

Ao selecionar essa opção, será aberta uma janela com as configurações da IDE, como a da imagem a seguir. Não é necessária nenhuma configuração na seção "geral" ("General"), portanto apenas acesse a seção "Interpreter", como demarcado na imagem, e selecione o tipo de interpretador desejado, no nosso caso o **MicroPython (Raspberry Pi Pico)**.

<img src="./illustrations/thonny-interpreter.png" width=60% height=60%>

### Gravação do firmware

Com essa configuração finalizada, está na hora de gravar o firmware do interpretador MicroPython na placa. Para isso, pressione o botão "BOOTSEL" da sua Raspberry Pi Pico, enquanto ela ainda está desconectada. Então conecte-a ao seu computador usando o cabo Micro USB, mantendo o botão pressionado. Depois que o cabo for completamente inserido no conector da placa, você já pode soltar o botão, como no GIF a seguir.

<img src="./illustrations/usb-conn-ok.png" width=60% height=60%>

<img src="./illustrations/bootsel.png" width=60% height=60%>

https://github.com/user-attachments/assets/af29f560-eb8b-4e25-add5-d71e613a0b1c

https://github.com/BitDogLab/BitDogLab/blob/main/doc/illustrations/bootsel-animation.mp4

<img src="./illustrations/bootsel-pressed.png" width=60% height=60%>

Esse procedimento faz com que a placa entre em modo de gravação de firmware e seja reconhecida como um disco removível. Inclusive você também poderá vê-la no diretório de discos do seu computador, como nesta imagem.

<img src="./illustrations/RPI-RP2.png" width=25% height=25%>

Neste momento, abra novamente a seção "Interpreter" das configurações da Thonny IDE, para a gravação do firmware da placa. Ao acessar novamente essa seção, você verá que a janela está um pouco diferente agora, como a da imagem abaixo.

<img src="./illustrations/thonny-port-install-update.png" width=60% height=60%>

A porta serial da placa é por padrão selecionada automaticamente pela IDE (opção "Try to detect port automatically" no campo "Port"), porém é possível realizar essa configuração manualmente se você estiver trabalhando com mais de uma placa ao mesmo tempo. Para isso, basta clicar sobre o campo "Port" para expandir as portas seriais disponíveis, e então selecionar a porta correspondente da sua placa no seu computador (o "Gerenciador de Dispositivos" do seu computador pode ajudar nesta seleção).

Com esta janela aberta, clique sobre a opção "Install or update firmware", como demarcado na imagem acima. Isso abrirá uma segunda janela com as informações sobre o disco e a versão do firmware que será gravado, como na imagem a seguir.

<img src="./illustrations/select-pipico.png" width=60% height=60%>
<img src="./illustrations/install-micropython.png" width=60% height=60%>

A seleção do disco que será gravado é automática, portanto apenas certifique-se de que o dispositivo que será gravado está com o nome "Raspberry Pi RP2", como demarcado na imagem acima.

Se essa seleção estiver correta, pressione o botão "Install" e aguarde alguns instantes. Assim que a gravação começar, será apresentada uma barra de progresso, e quando a gravação for concluída, será apresentada a mensagem "DONE!" ao lado da barra de progresso.

Assim que a gravação estiver finalizada, você pode fechar essa janela de gravação e fechar a janela de configuração da Thonny IDE. Para que a placa saia do modo de gravação de firmware, é necessário desconectar e reconectar a placa, porém, desta vez, sem pressionar o botão "BOOTSEL".

Agora a sua Raspberry Pi Pico já está pronta para receber códigos Python!

#### Alternativas de gravação de firmware

Drag and drop direto do arquivo de firmware baixado no disco montado RPI-RP2 no seu computador.

<img src="./illustrations/RPI-RP2.png" width=25% height=25%>

Firmware Oficial MicroPython Raspberry Pi Pico: https://micropython.org/download/RPI_PICO/

Firmware Oficial MicroPython Raspberry Pi Pico W: https://micropython.org/download/RPI_PICO_W/

Firmware BitDogLab, compilado já com as bibliotecas de sensores e atuadores ahtx0 (Sensor de temperatura/umidade AHT10 i2c), bh1750 (Sensor de luminosidade i2c) e ssd1306 (Oled i2c): https://github.com/BitDogLab/BitDogLab/tree/main/Firmware

Firmware Raspberry Pi Pico: https://github.com/BitDogLab/BitDogLab/blob/main/Firmware/BitDogLab.uf2

Firmware Raspberry Pi Pico W: https://github.com/BitDogLab/BitDogLab/blob/main/Firmware/BitDogLab_W.uf2

## Executando primeiro exemplo de código

Com a configuração finalizada e com a gravação de firmware concluída, digite o código a seguir na Thonny IDE (Acendendo o Led embarcado na Raspberry Pi Pico ou Pico W).

```python
import machine #biblioteca de controle do microcontrolador (machine)
import time #biblioteca de controle dos recursos de temporização

led = machine.Pin('LED', machine.Pin.OUT) #configura o pino LED como um pino de saida e cria um objeto 'led' da classe Pin (Pino)

while True: #enquanto for True for verdadeiro, ou seja, para sempre, faça...
  led.value(True)  #Liga o LED
  time.sleep(1)   #espera 1 segundo
  led.value(False)  #desliga o LED
  time.sleep(1)   #espera por 1 segundo
```

O código inicia com as adições da instância "Pin" da biblioteca "machine" do interpretador MicroPython e da função "sleep" da biblioteca "time" da própria linguagem Python. Feito isso, é criado o objeto led como uma saída do sistema conectada ao 'LED' da placa (esse objeto evita que você tenha que diferenciar o GPIO entre as placas Pi Pico e Pi Pico W), graças ao comando led = Pin('LED', Pin.OUT).

Já na repetição do código (função while True), apenas acendemos (led.value(True)) e apagamos (led.value(False)) o LED, com uma interrupção de 1 segundo (time.sleep(1)) a cada mudança de estado (de "high" para "low", e vice versa).

Após digitar o código na Thonny IDE, pressione o botão "Run", demarcado em amarelo na imagem abaixo, para executar o código.

<img src="./illustrations/led-blink-save-pipico.png" width=100% height=100%>

Após selecionar essa opção, será aberta uma segunda janela requisitando o nome do arquivo, como na imagem a seguir (main.py).

<img src="./illustrations/led-blink-mainpy.png" width=100% height=100%>

Neste momento, digite um nome para o arquivo com a extensão ".py" (como feito na imagem acima), e então pressione o botão "OK". Assim que o arquivo for salvo na placa, ela já começará a executá-lo, piscando o LED de 1 em 1 segundo, como no vídeo a seguir.

https://github.com/user-attachments/assets/31ae1e8b-52e4-4fde-a836-95af6cfb6a52

https://github.com/BitDogLab/BitDogLab/blob/main/doc/illustrations/led-blink.mp4
