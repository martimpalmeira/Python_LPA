# Escreva um programa que leia duas listas de dados A e B de 10 posições 
# ordenadas e passe-as para uma função que deve construir uma nova lista C 
# ordenada de forma crescentemente com os elementos de A e B.

lista_a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista_b = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Ordena uma lista que recebe valores ordenados de outras duas
def ordenaSemSort(lista_a, lista_b):
  lista_c = lista_a + lista_b
  for i in range(len(lista_c)): 
    # O "i" representa as posições da lista
    for j in range(i + 1, len(lista_c)):
      # O "j" representa as posições dos itens seguintes aos item "i"
      if lista_c[i] > lista_c[j]:
				# Faz a substuição dos valores entre si
        lista_c[i], lista_c[j] = lista_c[j], lista_c[i]
  return lista_c

print(f'Lista A = {lista_a}')
print(f'Lista B = {lista_b}')
print(f'Lista C = {ordenaSemSort(lista_a, lista_b)}')
