# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO.
nota1 = float(input('PRIMEIRA nota: '))
nota2 = float(input('SEGUNDA nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print('''Aluno APROVADO!\nPrimeira nota {}\nsegunda nota {}\nMÉDIA = {}.'''.format(nota1, nota2, media))
elif media > 5.0 and media < 7.0:
    print('''Aluno EM RECUPERAÇÃO!\nPrimeira nota {}\nSegunda nota {}\nMÉDIA = {}.'''.format(nota1, nota2, media))
else:
    print('''Aluno REPROVADO!\nPrimeira nota {}\nSegunda nota {}\nMÉDIA = {}.'''.format(nota1, nota2, media))
