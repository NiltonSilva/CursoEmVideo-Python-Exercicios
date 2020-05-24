lista = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafoto',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport',
         'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-=' * 15)
print(f'Lista dos times do Brasileirão: {lista}')
print('-=' * 15)
print(f'Lista dos 5 primeiros colocados: {lista[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são: {lista[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(lista)}')
print('-=' * 15)
chape = lista.index('Chapecoense')
print(f'A Chapecoense estão na {chape+1}º posição.')