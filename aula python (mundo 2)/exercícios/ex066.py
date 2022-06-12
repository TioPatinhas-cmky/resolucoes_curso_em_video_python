vezes = soma = numero = 0 

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    vezes += 1
print(f'Você digitou {vezes} números. A soma entre eles foi {soma}')