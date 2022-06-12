from math import hypot
co = float(input('qual o valor do cateto oposto ?'))
ca = float(input('qual o valor do cateto adjacente?'))
hi = hypot(co, ca)
print('a hipotenusa é {:.2f}'.format(hi))
