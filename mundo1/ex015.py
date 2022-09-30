"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

kilometersTraveled = float(input('Quantos quilometros você andou com o carro: '))
daysUsed = float(input('Digite quantos dias você ficou com o carro: '))

amountToBePaid = (0.15 * kilometersTraveled) + (60 * daysUsed)

print(f'Você deve pagar R${amountToBePaid:.2f} pelo carro alugado')
