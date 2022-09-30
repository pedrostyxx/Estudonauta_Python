# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número inteiro: '))

count = 0
for num_ in range(10):
    count = count + 1
    print(f'{num} X {count} é {num*count}')