'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou sej já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.
'''
from datetime import date
hoje = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = hoje - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, hoje))
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade > 18:
    print('Já passou do tempo de ser alistar')
    print('Você deveria ter se alistado há {} anos.'.format(idade-18))
else:
    print('Ainda não chegou o período de se alistar, pois ainda não tem 18 anos. ')
    print('Ainda faltam {} para o alistamento. Volte no ano {}.'.format(18-idade, hoje + (18-idade)))