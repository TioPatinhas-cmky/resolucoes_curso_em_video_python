num = int(input('Digite um número inteiro: '))

print('''Digite um número inteiro:
[1] para BINÁRIO
[2] para OCTAL
[3] para HÉXADECIMAL''')
opção = int(input('Qual é a sua opção? '))
if opção == 1:
    print(f'Convertido para binário é igual a {bin(num)[2:]}')

elif opção == 2:
    print(f'Convertido para octal é igual a {oct(num)[2:]}')

elif opção == 3:
    print(f'Convertido para héxadecimal é igual a {hex(num)[2:]}')

else:
    print('Opção inválida.')