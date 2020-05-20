totalCompras = produtosMais1000 = menorPreco = contador = 0
produtoBarato = ' '
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$ '))
    totalCompras += preco
    if preco > 1000:
        produtosMais1000 += 1
    if contador == 0 or preco < menorPreco:
        menorPreco = preco
        produtoBarato = produto
    contador += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {totalCompras:.2f}.')
print(f'Temos {produtosMais1000} produtos custando mais de R$ 1000.00.')
print(f'O produto mais barato foi {produtoBarato} que custa R$ {menorPreco:.2f}.')
