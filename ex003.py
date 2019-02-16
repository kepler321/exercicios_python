'''Exercício 3:
Um programa que solicite o nome, o peso e a altura do usuário.
Calcule o IMC e exiba "Olá, X. Você tem um IMC de Y", onde X é o nome informado e Y é o IMC calculado
-------------------------------
'''
nome = str(input('Digite o seu nome: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

print('Olá {}. Voce tem um IMC de {:.1f}'.format(nome, imc))