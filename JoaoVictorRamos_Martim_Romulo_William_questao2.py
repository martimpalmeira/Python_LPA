#15. Faça um programa em Python que leia um valor n e calcule e mostre o resultado da  soma dos n primeiros termos da serie abaixo

n = int(input('Digite um valor inteiro: '))
s2 = 0
print('S2 = ', end='')
for i in range(1, n+1):
    s2 += i / (2 * i)
    print(f'{i}/{2*i} ', end='')
    if i != n:
        print('+', end=' ')
    else:
        print(f'= {s2}')
print(f'A soma dos {n} primeiros termos da série é: {s2}')
