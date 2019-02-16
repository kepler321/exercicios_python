'''Exercício 2:
Um programa que solicite o nome e a idade do usuário.
Depois, exiba "Você se chama X e tem Y anos", onde X é o nome digitado e Y é a idade digitada
-------------------------------'''
nome = str(input('Digite o seu nome : '))
idade = int(input('Digite a sua idade :'))

print('Voce se chama {} e tem {} anos'.format(nome, idade))