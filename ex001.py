'''Exercício 1:
Um programa que solicite 3 números ao usuário e exiba a média aritimética entre eles
-------------------------------'''
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número'))
n3 = float(input('Terceiro número'))
media = (n1 + n2 + n3) / 3

print('A média aritimética entre os numeros é : {:.1f}'.format(media))
