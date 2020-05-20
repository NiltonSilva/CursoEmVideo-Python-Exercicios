soma = contador = numero = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Você digitou {contador} números e a soma deles é {soma}.')