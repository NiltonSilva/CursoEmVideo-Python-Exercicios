salario = float(input('Qual o salário do funcionário? '))
if salario > 1250:
    novoSalario = salario + (salario * 10 / 100)
else:
    novoSalario = salario + (salario * 15 /100)
print('O salário com reajuste será de R${:.2f}.'.format(novoSalario))