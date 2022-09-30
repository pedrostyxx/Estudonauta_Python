# Escreva um programa que converta uma temperatura em º C e converta para º F

value = float(input('Digite a temperatura em Graus Celsius: '))

conversion = (value * 9/5) + 32

print(f'Isso equivale a {conversion:.0f} graus fahrenheit')
