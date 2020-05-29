numeros = []
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Deseja continuar [S/N]? '))
    if continuar in 'nN':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}.')