import bitdoglab as bd
import time

def generate_led_positions(pattern):
    positions = []
    for y, row in enumerate(reversed(pattern)):  # Inverte a ordem das linhas
        for x, char in enumerate(row):
            if char == '*':
                positions.append((x, y))  # Inverte a ordem das coordenadas
    return positions

# padrão do coração  ..# está de cabeça ára baixo 
pattern = [
    "*****",
    "*****",
    "*****",
    "*****",
    "*****"
]

coracao = generate_led_positions(pattern)
print(coracao)

