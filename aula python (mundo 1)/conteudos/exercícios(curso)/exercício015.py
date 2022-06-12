dias = int(input('Por quantos dias o carro foi alugado ?'))
km = float(input('quantos KM foram rodados com o carro ?'))
pago = (dias * 60 ) + (km * 0.15)
print('o total a pagar é de {:.2f}'.format(pago))