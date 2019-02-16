""" Exercício 7:
Uma Revendedora de veículos paga a seus funcionários (vendedores) um salário fixo por mês,
mais uma comissão também fixa para cada carro vendidos, com taxas diferentes para novos e usados.
Escreva um programa que pergunte quanto é a % de comissão para novos, a % para usados e o salário do funcionário.
Depois perguntes quantos carros novos e quantos carros usados um funcionário vendeu
(perguntado o valor de cada carro, considerando que todo carro usado tem o mesmo valor e todo novo também).
Ao final, exiba seu salário bruto. """

salario = float(input('Qual é o salário do funcionario?: '))
comicaonovo = float(input('Qual é a porcentagem da comicao para carros novos?: '))
comicaovelho = float(input('Qual é a porcentagem da comicao para carros velhos?: '))
vendanovo = int(input('Quantos carros novos o funcionario vendeu?: '))
vendavelho = int(input('Quantos carros velhos o funcionario vendeu?: '))

# perguntar o valor da venda de um carro novo e de um velho
# calcular a comissão com base nos valores informados e quantidade vendido
# usar o padrão snake_case em nome de variáveis

if vendanovo == 0 and vendavelho == 0:
    print(salario)
else:
    comicaonovo = (comicaonovo / 100) * vendanovo
    comicaovelho = (comicaovelho / 100) * vendavelho
    a = (salario * comicaovelho)
    b = (salario * comicaonovo)
    salario = salario + a + b

print('O salario do funcionario é de R${:.2f}!'.format(salario))
