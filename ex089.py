from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar [S/N]? '))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for indice, valorAluno in enumerate(ficha):
    print(f'{indice:<4}{valorAluno[0]:<10}{valorAluno[2]:>8.1f}')
while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual alunos? (999 interrompe): '))
    if opcao == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< VOLTE SEMPRE! >>>')