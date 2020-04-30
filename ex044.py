# Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:
# à vista dinheiro ou cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
preco = float(input('Preço do produto: '))
print('Opções de pagamento:')
print('[ 1 ] - à vista dinheiro ou cheque')
print('[ 2 ] - à vista no cartão de débito')
print('[ 3 ] - até 2x no cartão de crédito')
print('[ 4 ] - 3x ou mais no cartão de crédito')
condicao = (int(input('Infome a opção de pagamento: ')))
if condicao == 1:
    print('PREÇO NORMAL R$ {:.2f}'.format(preco))
    preco -= preco * 0.1
    print('PRECO FINAL COM DESCONTO R$ {:.2f}'.format(preco))
elif condicao == 2:
    print('PREÇO NORMAL R$ {:.2f}'.format(preco))
    preco -= preco * 0.05
    print('PRECO FINAL COM DESCONTO R$ {:.2f}'.format(preco))
elif condicao == 3:
    print('PREÇO NORMAL R$ {:.2f}. SEM DESCONTO'.format(preco))
elif condicao == 4:
    qtdadeParcelas = int(input('Informe a quantidade de parcelas: '))
    print('PREÇO NORMAL R$ {:.2f}'.format(preco))
    preco += preco * 0.2
    print('PRECO FINAL COM ACRESCIMENTO DO CARTÃO R$ {:.2f}'.format(preco))
    print('Compra parcelada em {} vezes de R$ {:.2f}'.format(qtdadeParcelas, preco/qtdadeParcelas))
else:
    print('Condição inválida.')