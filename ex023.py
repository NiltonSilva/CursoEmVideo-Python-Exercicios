numero = int(input('Digite um número: '))
uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print('O número digitado foi {}.'.format(numero))
print('UNIDADE {}'.format(uni))
print('DEZENA {}'.format(dez))
print('CENTENA {}'.format(cen))
print('MILHAR {}'.format(mil))
