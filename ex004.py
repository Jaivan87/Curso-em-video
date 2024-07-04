#Faça uma programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possiveis sobre ele.
n= input ('Digite Algo: ')
print('O tipo primitico desse valor é ', type(n))
print('Só tem espaços? ',n.isspace()) # (n) tem espaços?
print('É um número? ', n.isnumeric()) # (n) é um número?
print('É alfabético? ', n.isalpha()) # (n) é alfbético?
print('É alfanumérico? ', n.isalnum()) # (n) é um alfnumerico?
print('Está em maiúsculas? ', n.isupper()) # (n) Está em maiúsculas?
print('Está em minúsculas? ', n.islower()) # (n) Está em minúsculas?
print('Está capitalizada? ', n.istitle()) # (n) Está Capitalizada (Inicia com maiúcula)?




