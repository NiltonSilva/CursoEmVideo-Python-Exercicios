import random
prim = str(input('Primeiro aluno: '))
segu = str(input('Segundo aluno: '))
terc = str(input('Terceiro aluno: '))
quar = str(input('Quarto aluno: '))
lista = [prim, segu, terc, quar]
sorteado = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))
