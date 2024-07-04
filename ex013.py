# 013 Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento
s1 = float(input('Digite o seu salário:'))
s2 = s1
s3 = 15 * s1
s4 = s3 / 100
s5 = s1 + s4
print('seu novo salário com aumento de 15% é {:.2f}'.format(s5))
