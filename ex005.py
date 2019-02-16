'''Exercício 5:
Deverá calcular quantos clones de uma pessoa sobre ela mesmo até a lua e o sol, posteriormente.
Veja estas distâncias na internet.
Solicite o nome e altura da pessoa.
-------------------------------
lua = 384.400 km
sol = 149.600.000 km
'''

nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
alturakm = altura / 1000
luadistancia = 384400 / alturakm
soldistancia = 149600000  / alturakm
print('voce precisaria de {:.1f} clones para chegar a lua e de {:.1f} para chegar ao sol'.format(luadistancia, soldistancia))
