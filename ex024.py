#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
'''n = input('Digite o nome de uma cidade: ')
print(n)
print('Santo' in n)'''


def tem_silva(nome):
  """
  Verifica se o nome da cidade contém "Santo".

  Argumentos:
    nome: Uma string contendo o nome cidade da pessoa.

  Retorna:
    True se o nome contiver "Santo", False caso contrário.
  """
  nome_maiusculo = nome.upper()
  return "SANTO" in nome_maiusculo

nome = input("Digite o nome de uma cidade: ")

if tem_silva(nome):
  print("Sua cidade contém Santo no nome!")
else:
  print("Sua cidade não contém Santo no nome.")

