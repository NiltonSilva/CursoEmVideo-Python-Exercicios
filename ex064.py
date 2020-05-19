numero = 0
soma = 0
contador = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:

    contador += 1
    soma += numero
print('Você digitou {} números e a soma entre eles foi {}.'.format(contador, soma))