import bitdoglab as bd
import time

def generate_led_positions(pattern):
    positions = []
    for y, row in enumerate(pattern):
        for x, char in enumerate(row):
            if char == '*':
                positions.append((x, y))
    return positions

# Exemplo de uso
pattern = [
    "..*..",
    "..*..",
    "..*..",
    "..*..",
    "..*.."
]

led_positions = generate_led_positions(pattern)
print(led_positions)

