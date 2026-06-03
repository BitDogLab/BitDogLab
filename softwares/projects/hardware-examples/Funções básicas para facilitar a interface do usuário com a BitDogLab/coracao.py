import bitdoglab as bdl

# esta função define que será desenhado um coração na matriz de Leds, a cor deste coração pode ser definida pelos argumentos (r, g, b)
def coracao(r=25, g=0, b=0):
    #use o scripy "converte padrao desenhado para a funcao leds.py para obter este vetor abaixo
    coracao = [(2, 0), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (1, 4), (3, 4)]
    for x, y in coracao:
        bdl.leds(x, y, r, g, b)  # Acende os LEDs nas posições especificadas com as cores fornecidas

# Exemplo de uso
coracao()  # Acende o coração com as cores padrão (r=25, g=0, b=0)
#coracao(255, 0, 0)  # Acende o coração na cor vermelha


    
    