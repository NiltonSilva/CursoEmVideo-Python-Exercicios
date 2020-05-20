resto = notas50 = notas20 = notas10 = notas1 = 0
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
while True:
    valor = int(input('Qual valor você quer sacar? R$ '))
    if valor >= 50:
        notas50 = int(valor / 50)
        resto = valor % 50
        print(f'Total de {notas50:.0f} cédulas de R$ 50,00.')
    if resto >= 20:
        valor = resto
        notas20 = int(valor / 20)
        resto = valor % 20
        print(f'Total de {notas20:.0f} cédulas de R$ 20,00.')
    if resto >= 10:
        valor = resto
        notas10 = int(valor / 10)
        resto = valor % 10
        print(f'Total de {notas10} cédulas de R$ 10,00.')
    if resto >= 1:
        valor = resto
        notas1 = int(valor / 1)
        resto = valor % 1
        print(f'Total de {notas1:.0f} cédulas de R$ 1,00.')
    if resto == 0:
        break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')




