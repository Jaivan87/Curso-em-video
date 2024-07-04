#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
''''n = input('Digite um nome de uma pessoa: ')
#print(n)
print('Silva' in n)'''

def tem_silva(nome):
  """
  Verifica se o nome completo da pessoa contém "Silva".

  Argumentos:
    nome: Uma string contendo o nome completo da pessoa.

  Retorna:
    True se o nome contiver "Silva", False caso contrário.
  """
  nome_maiusculo = nome.upper()
  return "SILVA" in nome_maiusculo

nome = input("Digite seu nome completo: ")

if tem_silva(nome):
  print("Seu nome contém Silva!")
else:
  print("Seu nome não contém Silva.")