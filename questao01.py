# Escreva um programa em Python que salve em um arquivo chamado ‘lista_alunos.txt’ 
# uma lista de nomes de alunos de uma turma de lógica de programação. O usuário deve 
# informar quantos alunos quer registrar e em seguida informar tais nomes. Além de 
# salvar esta lista, seu programa deve ser capaz de ler o arquivo criado e exibi-lo 
# na tela. Crie uma função para salvar a lista no arquivo e outra função para ler o arquivo.

# Formar a lista
n = int(input("Informe o número de alunos: "))
listaAlunos = []
for i in range(n):
  nome = input("Digite o nome do(a) aluno(a): ")
  listaAlunos.append(nome)

# Nome do arquivo
arquivo = "lista_alunos.txt"

# Função que escreve
def escreveArq(lista, arquivo):
  with open(arquivo, "w") as escrita:
    for i in lista:
      escrita.write(f"{i}\n")
  
# Função que lê
def lerArq(arquivo):
  with open(arquivo, "r") as leitura: 
   print("\nAlunos cadastrados:\n" + leitura.read())
     
# Chamada das funções
escreveArq(listaAlunos, arquivo)
lerArq(arquivo)
