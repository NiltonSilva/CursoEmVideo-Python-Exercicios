matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
maior = 0
somaTercColu = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor [{linha, coluna}]: '))
print(matriz)
print(f'-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]
    print()
print(f'-=' * 30)
print(f'A soma dos valores pares é {somaPares}.')
for linha in range(0, 3):
    if matriz[linha][2]:
        somaTercColu += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaTercColu}.')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior elemento da 2º linha é {maior}.')


