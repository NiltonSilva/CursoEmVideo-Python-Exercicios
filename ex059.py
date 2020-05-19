from time import sleep
pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('     [ 1 ] - Somar')
    print('     [ 2 ] - Multiplicar')
    print('     [ 3 ] - Maior')
    print('     [ 4 ] - Novos números')
    print('     [ 5 ] - Sair do programa')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print('A soma entre {} + {} é {}.'.format(pri, seg, pri + seg))

    elif opcao == 2:
        print('O resultado de {} x {} é {}.'.format(pri, seg, pri * seg))

    elif opcao == 3:
        maior = pri
        if seg > pri:
            print('O maior número é o segundo: {}.'.format(seg))
        else:
            print('O maior número é o primeiro: {}.'.format(pri))

    elif opcao == 4:
        pri = int(input('Primeiro valor: '))
        seg = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa. Valews, Falows!')