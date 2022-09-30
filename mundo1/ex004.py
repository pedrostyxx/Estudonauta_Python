# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

value = input('Digite algo: ')

print(f'Type: {type(value)}\n'
    f'Space: {value.isspace()}\n'
    f'Numeric: {value.isnumeric()}\n'
    f'Alphabet: {value.isalpha()}\n'
    f'Uppercase: {value.isupper()}\n'
    f'Lowercase: {value.islower()}\n'
    f'Capitalize: {value.istitle()}')