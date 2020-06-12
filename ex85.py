'''numeros = list()
listaPar = list()
listaImpar = list()
listaFinal = list()
for numero in range(1, 8):
    numeros.append(int(input(f'Digite o {numero}º valor: ')))
for numero in numeros:
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)

print(f'{numeros}')
listaImpar.sort()
print(f'LISTA DE Nº IMPARES: {listaImpar}')
listaPar.sort()
print(f'LISTA DE Nº PARES: {listaPar}')
listaFinal.append(listaImpar)
listaFinal.append(listaPar)
print(listaFinal)'''

núm = [[], []]
valor = 0
for contador in range(1, 8):
    valor = int(input(f'Digite o {contador}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
print(f'Os valores pares digitados foram: {núm[0]}')
núm[1].sort()
print(f'Os valores ímpares digitados foram: {núm[1]}')