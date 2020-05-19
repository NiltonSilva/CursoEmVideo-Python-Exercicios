fatorial = int(input('Digite um numero para calcular o seu Fatorial: '))
valor = 1
print('Calculando {}! = '.format(fatorial), end='')
while fatorial > 0:
    print('{} '.format(fatorial), end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    valor = valor * fatorial
    fatorial -= 1
print(valor)