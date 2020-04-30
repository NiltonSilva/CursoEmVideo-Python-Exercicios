# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de avordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida
from math import pow
peso = float(input('Informe o peso: '))
altura = float(input('Informe a altura: '))
imc = peso / pow(altura, 2)
print('Seu peso {}'.format(peso))
print('Sua altura {}'.format(altura))
if imc < 18.5:
    print('Seu IMC: {:.2f}.\nVocê está ABAIXO DO PESO.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC: {:.2f}.\nVocê está no PESO IDEAL.'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC: {:.2f}.\nVocê está com SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC: {:.2f}.\nVocê está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC: {:.2f}.\nVocê está com OBESIDADE MÓRBIDA.'.format(imc))