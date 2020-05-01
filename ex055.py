maiorPeso = 0
menorPeso = 0
for i in range(1, 6):
    peso = float(input('Informe o {}º peso: '.format(i)))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('Maior peso registrado foi {} kg.'.format(maiorPeso))
print('Menor peso registrado foi {} kg.'.format(menorPeso))