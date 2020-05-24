from random import randint
maior = menor = 0
sorteados = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram:', end='')
for s in sorteados:
    print(f' {s} ',end='')
print(f'\nO maior valor sorteado foi {max(sorteados)}')
print(f'O menor valor sorteado foi {min(sorteados)}')