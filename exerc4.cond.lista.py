#4. Escreva um programa que a pessoa possua saldo inicial de R$5000,00 para uma viagem.
#→ Inicialmente, o programa apresenta duas opções para o usuário viajar: (1) Brasil ou (2) Exterior.
#→ Se o usuário escolher a viagem dentro do país, em seguida deve informar se quer viajar de (1) avião ou (2) cruzeiro.
#→ Se escolher avião, subtraia R$1000,00 do saldo.
#→ Se escolher cruzeiro, subtraia R$5000,00 do saldo. 
#→ Caso o usuário queira a viagem internacional, deve informar se quer viajar de (1) classe econômica ou (2) primeira classe.
#→ Se escolher classe econômica, subtraia R$2000,00 do saldo.
#→ Se a escolha for primeira classe, subtraia R$4000,00 do saldo.
#→ No final, mostre uma mensagem com o saldo restante.
saldo_inicial = float(5000)
print(f"O seu saldo inicial é de: R${saldo_inicial}\n")
tipo_viagem = int(input("Qual das opções você prefere viajar?\n(1) Brasil\n(2) Exterior\nResposta: "))
if tipo_viagem == 1:
  meio_transp = int(input("Qual o meio de transporte desejado?\n(1) Avião\n(2) Cruzeiro\nResposta: "))
  if meio_transp == 1:
    saldo_restante = saldo_inicial - 1000
  elif meio_transp == 2:
    saldo_restante = saldo_inicial - 5000
elif tipo_viagem == 2:
  qual_classe = int(input("Em qual classe deseja viajar?\n(1) Classe econômica\n(2) Primeira classe\nResposta: "))
  if qual_classe == 1:
      saldo_restante = saldo_inicial - 2000
  elif qual_classe == 2:
      saldo_restante = saldo_inicial - 4000
print(f"O seu saldo restante é de: R${saldo_restante:.2f}")
