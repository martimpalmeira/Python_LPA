# Escreva um programa que contenha uma função. Essa função deve receber por 
# parâmetro uma lista de números inteiros de tamanho definido pelo usuário. 
# A função deve construir uma outra lista de números inteiros de mesmo tamanho 
# que deverá conter o fatorial de cada elemento. Depois mostrar na tela o conteúdo das listas.

# Formar lista escolhida pelo Usuário
n = int(input("Informe o tamanho da lista: "))
primeiraLista = []
for i in range(n):
  numDaLista = int(input("Informe um número para a lista: "))
  primeiraLista.append(numDaLista)

# Função que calcula o fatorial 
def fatorial(numero):
    if numero == 0:
        return 1
    return numero * fatorial(numero - 1)

# Função que percorre a primeira lista, calcula o fatorial de cada elemento e adiciona na segunda lista
def fatorialLista(primeiraLista):
  segundaLista = []
  for i in primeiraLista:
    segundaLista.append(fatorial(i))
  print(segundaLista)

# Chamada da função anterior que recebe a primeira lista como parâmetro 
fatorialLista(primeiraLista)
