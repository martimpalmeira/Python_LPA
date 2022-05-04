#25. Faça um programa em Python que leia uma quantidade não determinada de números  inteiros. Calcule a quantidade de números positivos e negativos. O número que encerrará  a leitura será zero. 

numero= int
positivo = 0
negativo = 0
while numero != 0:
    numero = int(input('Digite um número inteiro qualquer. Digite 0 para encerrar a leitura: '))
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
print(f'Você digitou {positivo} números positivos e {negativo} números negativos.')