valor = float(input('Qual é o preço do produto? '))
print('''Qual vai ser a forma de pagamento? 

[1]A vista no dinheiro ou cheque.
[2]A vista no cartão.
[3]Em até 2X no cartão.
[4]3X ou mais no cartão.''')

opção = int(input('Qual é a sua opção? '))

if opção == 1:
    total = valor - (valor * 10 / 100)

elif opção == 2:
    total = valor - (valor * 5 / 100)

elif opção == 3:
    total = valor
    parcela = valor / 2
    print(f'Seu produto será parcelado em 2X de {parcela} sem juros.')

elif opção == 4:
    total = valor + (valor * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc} de R${parcela} COM JUROS')

else:
    print('\033[31mOPÇÃO INVÁLIDA.\033[m')

print(f'Sua compra de {valor :.2f} vai custar {total}.')