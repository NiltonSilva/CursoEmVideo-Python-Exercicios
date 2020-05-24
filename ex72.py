numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        print('Tente novamente! Digite um número entre 0 e 20: ')
    if 0 <= num <= 20:
        print(f'Você digitou o número {numero[num]}.')
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
        if continuar == 'N':
            break
print('FIM')

