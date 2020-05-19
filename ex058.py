from random import randint
numero = randint(0, 10)
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinha qual foi?')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == numero:
        acertou = True
    else:
        if jogador < numero:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
