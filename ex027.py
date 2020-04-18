n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() # "split()" vai recortar as palavras, vai fatiar e jogar dentro de uma lista
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
# len (nome) vai contar qtos elementos tem na lista, começando do 1. E vai imprimir o ultimo - 1.