#17. Escreva um programa em Python que leia dois números inteiros e faça a multiplicação  de um número pelo outro sem utilizar o operador de multiplicação (*). Imprimir na tela o  valor encontrado.  
#Obs: Lembrar que uma multiplicação pode ser definida por uma sucessão de somas.

n1 = int(input("Digite primeiro numero: "))
n2 = int(input("Digite segundo numero: "))
soma=0
if n2>=0:
  for i in range(n2):
    soma+=n1
  print(f"O resultado da multiplicação de {n1} por {n2} é: {soma}")
else:
  n2 = abs(n2)
  if n1>0:
    for i in range(n2):
      soma+=n1
    n2 = (-n2)
    print(f"O resultado da multiplicação de {n1} por {n2} é: {-soma}")
  elif n1<0:
    for i in range(n2):
      soma+=n1
    n2 = (-n2)
    soma = abs(soma)
    print(f"O resultado da multiplicação de {n1} por {n2} é: {soma}")
  else:
     n2 = (-n2)
     print(f"O resultado da multiplicação de {n1} por {n2} é: {soma}")