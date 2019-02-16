"""
Exercício 5:
Deverá calcular quantos clones de uma pessoa sobre ela mesmo até a lua e o sol, posteriormente.
Veja estas distâncias na internet.
Solicite o nome e altura da pessoa.
-------------------------------
lua = 384.400 km
sol = 149.600.000 km
"""

nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
altura_km = altura / 1000
lua_distancia = 384400 / altura_km
sol_distancia = 149600000 / altura_km
print('voce precisaria de {:.1f} clones para chegar a lua e de {:.1f} '
      'para chegar ao sol'.format(lua_distancia, sol_distancia))
