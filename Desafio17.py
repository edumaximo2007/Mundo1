from math import hypot
print('-=-'*10)
print('''\033[7m          DESAFIO 17          \033[m''')
print('-=-'*10)
print('')
print('\033[1mFaça um programa que leia o comprimento oposto e do cateto adjacente de um triangulo \nretângulo, calcule e mostre o comprimento da hipotenusa\033[m')
print('')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hi))