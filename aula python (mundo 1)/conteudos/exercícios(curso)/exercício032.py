from datetime import date
ano = int(input('qual o ano que você deseja saber se é BISSEXTO ? Digite 0 para saber se o ano atual é BISSEXTO '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('o ano {} é BISSEXTO'.format(ano))
else:
    print('o ano {} não é BISSEXTO'.format(ano))