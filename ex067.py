while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    print('-' * 30)
    contador = 1
    while contador <= 10:
        print(f'{tabuada} x {contador} = {tabuada * contador}')
        contador += 1
    print('-' * 30)
print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!!!')