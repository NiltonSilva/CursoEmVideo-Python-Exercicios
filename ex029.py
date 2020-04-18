velocidade = int(input('Qual a velocidade do carro? '))

if velocidade > 80:
    print('VOCÊ FOI MULTADO.')
    valorMulta = (velocidade - 80) * 7
    print('O valor da multa será de R${:.2f}.'.format(valorMulta))
else:
    print('Você está dentro do limite de velocidade.')
print('Dirija com segurança e boa viagem!!!')