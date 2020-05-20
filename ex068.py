from random import randint
vitoria = 0
while True:
    computador = randint(0, 10)
    print('=-' * 30)
    numero = int(input('Diga um número: '))
    soma = computador + numero
    parOuImpar = ' '
    while parOuImpar not in 'PI':
        parOuImpar = str(input('Par ou Ímpar [P/I]: ')).strip().upper()
    print('=-' * 30)
    if soma % 2 == 0 and parOuImpar == 'P':
        print(f'Computador escolheu {computador} e você escolheu {numero}. Resultado {soma}.')
        print('O resultado deu PAR. Parabens, você venceu!')
    elif soma % 2 != 0 and parOuImpar == 'I':
        print(f'Computador escolheu {computador} e você escolheu {numero}. Resultado {soma}')
        print('O resultado deu ÍMPAR. Parabens, você venceu!')
    else:
        print(f'Computador escolheu {computador} e você escolheu {numero}. Resultado {soma}')
        print('Você perdeu!')
        break
    vitoria += 1
    print(f'Total de vitórias = {vitoria}')
    print('Vamos jogar novamente...')
print('=-' * 30)
print(f'Você venceu o total de {vitoria} partidas.')
