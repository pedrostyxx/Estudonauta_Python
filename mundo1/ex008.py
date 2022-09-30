# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

value = float(input('Digite umvalor em metros: '))

centimeters = value * 100
millimeter = value * 1000

print(f'{value} metros equivale a {centimeters:.0f} centimetros\n'
    f'{value} metros equivale a {millimeter:.0f} milímetros')