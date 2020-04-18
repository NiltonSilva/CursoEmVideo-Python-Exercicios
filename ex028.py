from random import randint
from time import sleep  # o computador espera por alguns segundos até que o próximo comando seja executado
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)                # configuração do tempo que o computador espera.
if jogador == computador:
    print('PARABÉNS!!! Você acertou.')
else:
    print('Você errou.')
    print('Eu pensei no número {}.'.format(computador))