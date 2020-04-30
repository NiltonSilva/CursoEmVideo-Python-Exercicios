from datetime import date
hoje = date.today().year
nasc = int(input('Informe o ano de nascimento: '))
idade = hoje - nasc

if idade <= 9:
    print('Categoria MIRIM')
    print('Quem nasceu em {} tem {} anos.'.format(nasc, idade))
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
    print('Quem nasceu em {} tem {} anos.'.format(nasc, idade))
elif idade > 14 and idade <= 19:
    print('Categoria JÚNIOR')
    print('Quem nasceu em {} tem {} anos.'.format(nasc, idade))
elif idade >19 and idade <= 25:
    print('Categoria SÊNIOR')
    print('Quem nasceu em {} tem {} anos.'.format(nasc, idade))
else:
    print('Categoria MASTER')
    print('Quem nasceu em {} tem {} anos.'.format(nasc, idade))