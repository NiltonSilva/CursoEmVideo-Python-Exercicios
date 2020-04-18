distancia = int(input('Digite a distância (em km) da viagem: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O valor da passagem é R${:.2f}.'.format(preco))