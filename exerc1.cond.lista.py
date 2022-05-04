#1. Escreva um programa que o usuário informa a sigla de um estado (por ex.: BA, CE, PE).
#→ O programa então informa qual é a capital daquele estado.
#→ Faça para 5 estados quaisquer.
#→ Se o usuário informar algo errado, diga que a opção é inválida.
#→ Ao final, exiba uma mensagem de fim de programa.

sigla_estado = input("Escreva a sigla de um dos seguintes estados: \n(BA)\n(SP)\n(RS)\n(AM)\n(GO)\nResposta: ")
if sigla_estado == "BA":
  print("A capital do estado da Bahia é a cidade de Salvador")
elif sigla_estado == "SP":
  print("A capital do estado de São Paulo é a cidade de São Paulo")
elif sigla_estado == "RS":
  print("A capital do estado do Rio Grande do Sul é a cidade de Porto Alegre")
elif sigla_estado == "AM":
  print("A capital do estado de Amazonas é a cidade de Manaus")
elif sigla_estado == "GO":
  print("A capital do estado de Goiás é a cidade de Goiânia")
else: print("Opção inválida")
print("Fim de programa.")
