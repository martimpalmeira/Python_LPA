#10. Faça uma função que receba estrutura de dados com 10 números e informe a quantidade de ocorrências do último número lido. Por exemplo, para a sequência 38 4 23 5 6 7 4 12 4, o resultado deve ser ‘O número 4 apareceu 3 vezes’.

numeros = [38, 4, 3, 5, 6, 7, 4, 12, 5, 4]
def freqUltNum(numeros):
  x=0
  for n in numeros:  
    if n == (numeros[9]):
      x+=1
  print(f"O número {numeros[9]} apareceu {x} vezes")
freqUltNum(numeros)