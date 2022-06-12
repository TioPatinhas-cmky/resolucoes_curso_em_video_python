totcompra = produto_maior_mil = menor = total_produtos = 0
produto_barato = ' '

print('-' * 34)
print('''           LOJA BARATÃO           ''')
print('-' * 34)

while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço:R$ '))
    total_produtos += 1
    if total_produtos == 1 or preço < menor:
        menor = preço
        produto_barato = produto
    totcompra += preço
    opção = str(input('Quer continuar?[S/N] '))
    
    
    if opção in 'Nn':
        break

    if preço > 1.000:
        produto_maior_mil += 1

    
print('------------------FIM DO PROGRAMA------------------')
print(f'''O total da compra foi {totcompra :.2f}
Temos {produto_maior_mil} produtos custando mais de R$1000
O produto mais BARATO foi {produto_barato} custando {menor:.2f}''')
