# 012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p1 = float(input('Qual o preço do produto? R$'))
p2 = p1
p3 = 5 * p1
p4 = p3 / 100
p5 = p1 - p4
#d = p1 - p3
print('O novo preço com desconto de 5% é R${}'.format(p5))

