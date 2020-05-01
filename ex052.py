numero = int(input('Digite um número: '))
contador = 0
for i in range(1, numero+1):
    if numero % i == 0:
        print('\033[33m', end='')
        contador += 1
    else:
        print('\033[31m', end='')
    print(' {} '.format(i), end='')
print('\33[m')
if contador > 2:
    print('\nO número {} foi divisível {} vezes'.format(numero, contador))
    print('E por isso ele NÃO É PRIMO!')
else:
    print('\nO número {} foi divisível {} vezes.'.format(numero, contador))
    print('E por isso ele É PRIMO!')