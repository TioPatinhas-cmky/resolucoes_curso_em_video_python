real = float(input('quanto dinheiro você tem na carteira ? R$'))
dólar = real / 3.27
print('com R${:.2f} você consegue comprar US${:.2f}'.format(real, dólar))