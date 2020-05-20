idadeMais18 = totalHomens = mulheresIdadeMenor20 = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA     ')
    print('-' * 30)
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
       idadeMais18 += 1
    if sexo == 'M':
        totalHomens += 1
    else:
        if idade < 20:
            mulheresIdadeMenor20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {idadeMais18}.')
print(f'Ao todo temos {totalHomens} homens cadastrados.')
print(f'E temos {mulheresIdadeMenor20} mulheres com menos de 20 anos.')
