# 011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessária para pinta-lá, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.
a1 = float(input('qual a altura da parede? :'))
l1 = float(input('Qual a largura da parede? :'))
ar = a1 * l1
m1 = 2
li = ar // m1 + 1
print('A área da parede é de {:.2f}m2'.format(ar))
print('Será necessário {} litros de tinta para cobrir {:.2f} m2'.format(li,ar))