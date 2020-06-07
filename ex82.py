num = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'nN':
        break
pares = list()
impares = list()
for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')