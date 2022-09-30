# Faça um programa que leia a largura e a altura de uma parede em metros e
# calcule sua área e a quantidade de tinta necessária para pintá-la
# sabendo que cada litro de tinta, pinta uma área de 2m².

height = float(input('Digite a altura da parede: '))
width = float(input('Digite a largura da parede: '))

liter = 2
area = height * width
result = (area/liter)

print(f'É necessário {result} litros de tinta para pintar essa parede')