# Crie um programa que faça o computador jogar JOKENPÔ com você
from random import randint
from time import sleep
print('[ 1 ] - Pedra')
print('[ 2 ] - Papel')
print('[ 3 ] - Tesoura')
opcao = int(input('Escolha sua jogada: '))
print('')

computador = randint(1, 3)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO...')

print('')
if opcao == 1:
    if computador == 2:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('VOCÊ PERDEU')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você escolheu PEDRA')
        print('Computador escolheu PAPEL')
    elif computador == 3:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('VOCÊ GANHOU')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você escolheu PEDRA')
        print('Computador escolheu TESOURA')
    elif computador == 1:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('EMPATE')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Os dois escolheram PEDRA')
elif opcao == 2:
    if computador == 1:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('VOCÊ VENCEU')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você escolheu PAPEL')
        print('Computador escolheu PEDRA')
    elif computador == 2:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('EMPATE')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Os dois escolheram PAPEL')
    elif computador == 3:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('VOCÊ PERDEU')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você escolheu PAPEL')
        print('Computador escolheu TESOURA')
elif opcao == 3:
    if computador == 1:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('VOCÊ PERDEU')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você escolheu TESOURA')
        print('Computador escolheu PEDRA')
    elif computador == 2:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('VOCÊ VENCEU')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você escolheu TESOURA')
        print('Computador escolheu PAPEL')
    elif computador == 3:
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('EMPATE')
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print('Você escolheu TESOURA')
        print('Computador escolheu TESOURA')
else:
    print('Você escolheu uma opção inválida!')