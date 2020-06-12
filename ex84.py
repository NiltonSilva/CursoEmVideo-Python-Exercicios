nomesPesos = []
listaCompleta = []
maior = menor = 0
while True:
    nomesPesos.append(str(input('Digite o nome: ')))
    nomesPesos.append(int(input('Digite o peso: ')))
    if len(listaCompleta) == 0:
        maior = menor = nomesPesos[1]
    else:
        if nomesPesos[1] > maior:
            maior = nomesPesos[1]
        if nomesPesos[1] < menor:
            menor = nomesPesos[1]
    listaCompleta.append(nomesPesos[:])
    nomesPesos.clear()
    continua = str(input('Quer continuar [S/N]? '))
    if(continua in 'nN'):
        break

print('-=' * 30)
print(f'O total de pessoas cadastradas foram: {len(listaCompleta)} pessoas.')
print(f'O maior peso foi de {maior} quilos.  Peso de ', end='')
for p in listaCompleta:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} quilos. Peso de ', end='')
for p in listaCompleta:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
