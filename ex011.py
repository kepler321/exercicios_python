"""Exercício 11:
Crie um programa de cálculo de IMC que, a partir da altura, peso e gênero do usuário.
exiba a situação de seu IMC.
Verifique as regras e compare os resultados de seu programa com os deste site:
http://www.calcule.net/imc.calculo.indice.de.massa.corporal.a.php"""
"""(peso / (altura * altura)"""
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
genero = str(input('Digite o seu genero (m/f): '))
imc = (peso / (altura * altura))
if genero != 'm' and genero != 'f':
    print('Isso nao é um genero')
if genero == 'm':
    if imc <= 24.99: