#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#ex: Digite um número: 1834
#Unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
num = int(input('Digite seu numero: '))
u = num // 1 % 10  #divisão inteira por 1 e tirar o resto da divisão por 10
d = num // 10 % 10 #divisão inteira por 10 e tirar o resto da divisão por 10
c = num // 100 % 10 #divisão inteira por 100 e tirar o resto da divisão por 10
m = num // 1000 % 10 #divisão inteira por 1000 e tirar o resto da divisão por 10
print('Analisando o número {}'.format(num))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
