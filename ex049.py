num = int(input('Digite um numero: '))
print('A TABUADA DE {}'.format(num))
for i in range(0, 11):
    print('{} x {} = {}'.format(i, num, i * num))