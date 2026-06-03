# Basic Examples - BitDogLab v7

Exemplos curtos em MicroPython, separados por periferico.

As pastas estao numeradas do mais simples para o mais avancado. Dentro de cada pasta, cada exemplo ja e um arquivo `.py` direto.

Para testar, abra o arquivo do exemplo na Thonny e salve na placa como `main.py`.

## Perifericos

- `01-led-rgb`: 10 exemplos
- `02-botoes`: 10 exemplos
- `03-buzzer`: 10 exemplos
- `04-matriz-led`: 10 exemplos
- `05-display-oled`: 10 exemplos
- `06-joystick`: 5 exemplos
- `07-microfone`: 5 exemplos

## Pinagem usada

- LED RGB: vermelho GPIO13, verde GPIO11, azul GPIO12
- Matriz 5x5 NeoPixel: GPIO7
- Display OLED: SDA GPIO2, SCL GPIO3
- Botoes: A GPIO5, B GPIO6, C GPIO10, joystick GPIO22
- Buzzer: GPIO21
- Joystick: X GPIO27, Y GPIO26
- Microfone: GPIO28

## Observacoes

- Exemplos com display usam `ssd1306.py` na placa.
- Exemplos com matriz usam a biblioteca `neopixel`.
- `read_u16()` retorna valores de 0 a 65535.
- `duty_u16()` tambem usa valores de 0 a 65535 para PWM.
