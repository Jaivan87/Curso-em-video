# 010 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar.
n1 = int(input('quanto você tem na carteira: '))
d = n1 // 3.27
print('Quantos dolares posso comprar com R${}'.format(n1))
print('R${} equivale a US${} dolares'.format(n1,d))