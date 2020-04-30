# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? '))
salarioComprador = float(input('Qual o salário do comprador? '))
tempoPagamento = int(input('Informe o tempod e pagamento (em anos): '))

prestacao = (valorCasa / tempoPagamento) / 12

if prestacao > (salarioComprador * 0.3):
    print('EMPRESTIMO NEGADO!')
    print('Valor da prestação maior que 30% do salário do comprador.')
    print('Para pagar uma casa de R${} em {} anos a prestação será de {:.2f} mensal.'.format(valorCasa, tempoPagamento, prestacao))
else:
    print('Parabéns, EMPRESTIMO APROVADO!')
    print('O valor da prestação mensal é R$ {:.2f}.'.format(prestacao))