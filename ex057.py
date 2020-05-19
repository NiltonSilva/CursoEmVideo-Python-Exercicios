sexo = str(input('Digite o sexo [M/F]: ')).strip().lower()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida. Por favor, digite o sexo [M/F]: ')).strip().lower()[0]
print('Sexo {} cadastrado com sucesso!'.format(sexo))
