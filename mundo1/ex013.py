# Faça um algoritmo que leia o salário de um funcionário, e mostre seu novo salário com 15% de aumento.

wage = float(input('Digite o seu salário: '))

increase = wage * 15 / 100
result = wage + increase

print(f'Seu salário com 15% de aumento ficou no valor de R${result:.2f}')