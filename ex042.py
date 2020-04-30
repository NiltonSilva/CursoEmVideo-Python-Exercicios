a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if a == b == c:
        print('Triângulo EQUILÁTERO')
    elif (a != b and b != c and a != c):
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
