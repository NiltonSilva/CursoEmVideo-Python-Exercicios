# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 - para octal, 3 - para hexadecimal.
numero = int(input('Digite um numero: '))
print('''Opções para conversao:
[1] - Converter para BINÁRIO
[2] - Converter para OCTAL
[3] - Converter para HEXADECIMAL''')
opcao = int(input())
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
    print()
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')