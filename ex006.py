'''Exercício 6:
O usuário informa seu nome, então aparece uma mensagem de bom dia e o nome do usuário.
Em seguida aparece uma mensagem pedindo para o usuário informar sua idade e com quantos anos deseja morrer.
Então esse número é subtraído pela sua idade e o programa informa: "Você irá viver mais X anos, ou Y meses ou Z dias ou W horas".
-------------------------------
'''
nome = str(input('Qual o seu nome? '))
print('Bom dia {}'.format(nome))

idade = int(input('Qual a sua idade? '))
morte = int(input('Com quantos anos voce deseja morrer?'))
morte2 = morte - idade
print('Voce ira viver mais {} anos'.format(morte2))