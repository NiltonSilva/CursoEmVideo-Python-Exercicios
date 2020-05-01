prim = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo = prim + (10 - 1) * razao
for i in range(prim, decimo, razao):
    print(i, end=' -> ')
print('ACABOU')