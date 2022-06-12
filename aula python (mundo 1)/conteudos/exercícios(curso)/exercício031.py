d = int(input('qual é a distancia da sua viagem ? '))
print('vc está prestes a ir em uma viagem de {} KM'.format(d))
primeirocusto = d * 0.50
segundocusto = d * 0.45
if d <=200:
    print('sua viagem vai custar R$ {:.2f}'.format(primeirocusto))
else:
    print('sua viagem vai custar {:.2f}'. format(segundocusto))