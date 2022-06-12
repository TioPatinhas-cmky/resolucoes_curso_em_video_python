from time import sleep


n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
print('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS VALORES\n[5]SAIR DO PROGRAMA')
opção = int(input('>>>> Qual é a sua opção? '))

while opção != 5:

    if opção == 1:

        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
        print('=-='*20)
        sleep(2)
        print('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS VALORES\n[5]SAIR DO PROGRAMA')
        opção = int(input('>>>> Qual é a sua opção? '))

    if opção == 2:

        multiplicaçao = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicaçao}')
        print('=-='*20)
        sleep(2)
        print('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS VALORES\n[5]SAIR DO PROGRAMA')
        opção = int(input('>>>> Qual é a sua opção? '))

    if opção == 3:

        maior = max(n1, n2)
        print(f'O maior valor entre {n1} e {n2} é {maior}')
        print('=-='*20)
        sleep(2)
        print(
            '''[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS VALORES\n[5]SAIR DO PROGRAMA''')
        opção = int(input('>>>> Qual é a sua opção? '))

    if opção == 4:

        print('=-=' * 20)
        print('coloque seus novos valores')
        sleep(2)
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
        print(
            '''[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS VALORES\n[5]SAIR DO PROGRAMA''')
        opção = int(input('>>>> Qual é a sua opção? '))

    if opção > 5:
        print('=-=' * 20)
        print('Opção inválida. Tente novamente')
        print('=-=' * 20)
        sleep(2)
        print(
            '''[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS VALORES\n[5]SAIR DO PROGRAMA''')
        opção = int(input('>>>> Qual é a sua opção? '))


print('Você desejou sair. Volte sempre!')
