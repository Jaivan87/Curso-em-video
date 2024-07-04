#Crie um programa que leia o nome completo de uma pessoa e mostre:.
#-O nome com todas as letras maiúculas
#-O nome com todas as letras minúsculas
#-quantas letras ao todo (sem cosiderar espaços)
#-Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
print('{} possui {} letras'.format(dividido[0], len(dividido[0])))