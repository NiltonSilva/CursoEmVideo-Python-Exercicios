dias = int(input('Informe a quantidade de dias alugados: '))
km = int(input('Informe a quantidade de KM rodado: '))
total = (km * 0.15) + (dias * 60)
print('O valor a ser pago será R$ {:.2f} reais.'.format(total))
