num = (int(input(f'Digite o 1º número: ')),
          int(input(f'Digite o 2º número: ')),
          int(input(f'Digite o 3º número: ')),
          int(input(f'Digite o 4º número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição.')
else:
    print('O valor 3 não digitado em nenhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')