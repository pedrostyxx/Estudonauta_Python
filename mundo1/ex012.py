# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

product = float(input('Digite o prço do produto: '))

calc = product * 5 / 100
discount = product - calc

print(f'Esse produto custará {discount:.2f} com 5% de desconto')
