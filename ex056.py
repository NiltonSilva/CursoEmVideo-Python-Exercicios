idadeTotal = 0
idadeMaisVelho = 0
contador = 0
for i in range(1, 5):
    print('----- {}º PESSOA -----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    idadeTotal += idade
    mediaIdade = idadeTotal / 4
    if sexo == 'M' or sexo == 'm':
        if idade > idadeMaisVelho:
            idadeMaisVelho = idade
            nomeMaisVelho = nome
    if sexo == 'F' or sexo == 'f':
        if idade < 20:
            contador +=1
print('A média de idade do grupo é de {}'.format(mediaIdade))
print('O homem mais velho é o Sr. {}, que tem {} anos'.format(nomeMaisVelho, idadeMaisVelho))
print('Existem {} pessoas do sexo feminino que têm menos de 20 anos'.format(contador))