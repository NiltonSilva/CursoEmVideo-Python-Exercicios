from time import sleep
print('Gerador de PA')
print('-=' * 10)
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 1
print(primeiroTermo, ' -> ', end='')
termos = 10
termosParcial = termos
while termos != 0:
    while contador < termosParcial:
        proximo = primeiroTermo + (razao * contador)
        print(proximo, '-> ', end='')
        contador += 1
        if contador == termosParcial:
            print('PAUSA')
    sleep(1)
    termos = int(input('Quantos termos você quer mostrar a mais? '))
    termosParcial = termosParcial + termos
print('Progressão finalizada com {} termos mostrados'.format(contador))