# Escreva um programa em Python que seja capaz de ler um arquivo que contém 
# uma lista de séries de televisão/netflix. Esta lista possui tamanho desconhecido. 
# Seu programa deve ler e exibir na tela as séries e seus dados uma por uma. Uma 
# série deve conter os seguintes atributos: nome, ano, temporadas e gênero. 
# (Atenção: É necessária a criação do arquivo antes de realizar a operação de leitura)

with open('lista_series.txt', 'r', encoding='UTF-8') as series:
    serie = series.readline()
    while serie != '':
        print(serie, end='')
        serie = series.readline()
