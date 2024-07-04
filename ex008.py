# 008 Escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros.
n1 = float(input('digite uma distância em metros: '))
c = n1 * 100
m = n1 * 1000
print ('A distância de {} metros, equivale a {:.0f} centimetros e {:.0f} milimetros' .format(n1, c, m))