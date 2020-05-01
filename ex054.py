from datetime import date
hoje = date.today().year
contadorMaior = 0
contadorMenor = 0
for i in range(1, 8):
    nascimento = int(input('Informe o {}º ano de nascimento: '.format(i)))
    if (hoje - nascimento) >= 18:
        contadorMaior += 1
    else:
        contadorMenor += 1
print('Ao todo tivermos {} com idade igual ou superior a 18 anos.'.format(contadorMaior))
print('E também tivemos {} com idade menor que 18 anos.'.format(contadorMenor))