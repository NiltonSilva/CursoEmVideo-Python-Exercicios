print('Gerador de PA')
print('-=' * 10)
numeroTermos = int(input('Quantos termos de PA? '))
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 1
print(primeiroTermo, " -> ", end='')
while contador < numeroTermos:
    proximo = primeiroTermo + (contador * razao)
    print(proximo, end='')
    contador += 1
    print(' -> ' if contador < numeroTermos else '\nFIM', end='')
