#23. Uma empresa possui um esquema de pontuação que determina o valor de um bônus. Essa pontuação é dada através da seguinte fórmula: 
#Pontos = Horas extras – 2/3 * Faltas 
#Escreva um algoritmo/programa em Python que leia de um empregado, as horas extras  trabalhadas e as horas de faltas e determine o bônus que é dado pela seguinte tabela: 

horasExtras = int(input("Informe suas horas extras trabalhadas: "))
horasFaltas = int(input("Informe suas horas de falta: "))
pontos = horasExtras - 2/3 * horasFaltas
if pontos > 40:
  print("O bônus é de R$5000,00")
elif pontos > 30 and pontos <= 40:
  print("O bônus é de R$4000,00")
elif pontos > 20 and pontos <= 30:
  print("O bônus é de R$3000,00")
elif pontos > 10 and pontos <= 20:
  print("O bônus é de R$2000,00")
else:
  print("O bônus é de R$1000,00")