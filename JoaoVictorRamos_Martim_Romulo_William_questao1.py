#23. Uma empresa possui um esquema de pontuação que determina o valor de um bônus. Essa pontuação é dada através da seguinte fórmula: 
#Pontos = Horas extras – 2/3 * Faltas 
#Escreva um algoritmo/programa em Python que leia de um empregado, as horas extras  trabalhadas e as horas de faltas e determine o bônus que é dado pela seguinte tabela: 

h_e = int(input("Quantas horas extras você fez esse mês?\n"))
f = int(input("Quantas faltas você teve esse mês?\n"))
p = h_e - (2/3) * f
b = 0
if p > 40:
  b = 5000
elif p > 30 and p <= 40:
  b = 4000
elif p > 20 and p <= 30:
  b = 3000
elif p > 10 and p <= 20:
  b = 2000
elif p <= 10:
  b = 1000

print(f"Sua bonificação extra desse mês será de R${b:.2f}.")