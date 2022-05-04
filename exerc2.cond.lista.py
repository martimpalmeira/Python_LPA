#2. Escreva um programa que peça para a pessoa informar o tamanho do salgado (M ou G) e o tamanho do suco (M ou G).
#→ Caso a pessoa peça salgado e suco médios, o preço é de R$10,00.
#→ Caso a pessoa peça salgado M e suco G, o preço é R$12,00.
#→ Caso a pessoa peça salgado G e suco M, o preço é R$13,00.
#→ Caso a pessoa peça salgado e suco grandes, o preço é de R$15,00.
#→ No final, o preço do combo é exibido.
#→ Se a pessoa informar uma opção inválida para salgado ou suco, o programa deve exibir uma interrogação como preço final. Mas para este exercício, você não pode usar o comando else.

tam_salg = input("Informe o tamanho do salgado\n(M) Para Médio\n(G) Para Grande\nResposta: ")
tam_suco = input("Informe o tamanho do suco\n(M) Para Médio\n(G) Para Grande\nResposta: ")
if tam_salg != "M" and tam_salg != "G" and tam_suco != "M" and tam_suco != "G":
  print("R$?")
elif (tam_salg == "M" or tam_salg == "G") and (tam_suco == "M" or tam_suco == "G"):
  if tam_salg == "M" and tam_suco == "M":
    print("O preço do combo é de R$10,00")
  elif tam_salg == "M" and tam_suco == "G":
    print("O preço do combo é de R$12,00")
  elif tam_salg == "G" and tam_suco == "M":
    print("O preço do combo é de R$13,00")
  elif tam_salg == "G" and tam_suco == "G":
    print("O preço do combo é de R$15,00")