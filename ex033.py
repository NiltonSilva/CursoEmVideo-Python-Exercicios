a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# Verificando quem é menor. Parti do principio que A é o menor dos 3
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é maior. Parti do principio que C é o menor dos 3
maior = b
if a > b and a > c:
    maior = a
if c > a and c > b:
    maior = c
print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))
