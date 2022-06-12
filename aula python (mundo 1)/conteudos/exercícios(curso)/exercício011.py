larg = float(input('largura da parede: '))
alt= float(input('altura da parede: '))
área = larg * alt
print('sua parede tem a dimensão de {} X {} e sua área é de {}m²'.format(larg,alt,área))
tinta = área / 2 
print('para pintar a parede você precisa de {}L de tinta'.format(tinta))