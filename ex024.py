#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
'''n = input('Digite o nome de uma cidade: ')
print(n)
print('Santo' in n)'''


def tem_silva(nome):
  """
  Verifica se o nome completo da pessoa contém "Silva".

  Argumentos:
    nome: Uma string contendo o nome completo da pessoa.

  Retorna:
    True se o nome contiver "Silva", False caso contrário.
  """
  nome_maiusculo = nome.upper()
  return "SANTO" in nome_maiusculo

nome = input("Digite seu nome completo: ")

if tem_silva(nome):
  print("Sua cidade contém Santo no nome!")
else:
  print("Sua cidade contém Santo no nome.")

