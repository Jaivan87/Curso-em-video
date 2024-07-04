#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#ex: Digite um número: 1834
#Unidade: 4
#dezena: 3
#centena: 8
#milhar: 1
n = input('Digite seu numero: ')
print('Unidade:' ,n[3])
print('dezena:' ,n[2])
print('centena:',n[1])
print('milhar:',n[0])