# .strip vai eliminar os espaços antes e depois no nome completo
nome = input('Digite seu nome: ').strip()
print(('Analisando seu nome...'))

# Nome em maiusculo
print('Seu nome em maiúsculo é {}'.format(nome.upper()))

# Nome em minusculo
print('Seu nome em minúsculo é {}'.format(nome.lower()))

#
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

# Contar quantas letras tem o primeiro nome (1º - separar as palavras; 2º - contar qtos caracteres na primeira palavra
primeiroNome = (nome.split())
print('Seu primeiro nome tem {} letras'.format(len(primeiroNome[0])))
# Pode ser assim também. Nesse caso, ele vai dizer a posição em que está o 'espaço' que separa o nome e o sobrenome
print('Seu primeiro nome tem {} letras'.format((nome.find((' ')))))
