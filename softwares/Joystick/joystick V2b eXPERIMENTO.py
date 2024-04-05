from machine import Pin, I2C
import ssd1306

# Inicializa o display OLED
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Variáveis para as posições x e y
x = 2
y = 2

# Função para atualizar o display OLED com as posições
def atualizar_display():
    display.fill(0)  # Limpa o display
    display.text("x: {}".format(x), 0, 0)  # Exibe a posição x
    display.text("y: {}".format(y), 0, 10)  # Exibe a posição y
    display.show()  # Atualiza o display

# Exemplo de uso
while True:
    # Atualiza as posições x e y conforme o joystick ou outros comandos
    # ...

    # Chama a função para atualizar o display OLED
    atualizar_display()

    # Aguarda um pouco antes da próxima atualização
    time.sleep(0.2)