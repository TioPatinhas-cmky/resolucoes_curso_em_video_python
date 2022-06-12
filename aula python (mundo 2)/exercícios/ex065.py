soma = quant = média = maior = menor = 0
opcao = 'S'
while opcao in 'Ss':
    numero = int(input('Digite um valor: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    opcao = str(input('Quer continuar?[S/N] ')).upper()
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}')
print(f'E o maior número lido foi {maior}, e o menor foi {menor}')
