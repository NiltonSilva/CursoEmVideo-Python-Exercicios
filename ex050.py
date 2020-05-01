soma = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(i)))
    if numero % 2 == 0:
        soma += numero
print('O valor total da soma foi {}'.format(soma))