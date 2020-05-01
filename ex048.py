soma = 0
contador = 0
for i in range(3, 500, 6):
    #print(i)
    soma += i;
    contador += 1
print('O valor da total da soma dos {} números foi {}'.format(contador, soma))