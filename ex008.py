"""Exercício 8:
Usuário informa seu nome. 
Perguntar quantas horas, quantos minutos e quantos segundos o carro do usuário ficou no estacionamento
Perguntar o valor da hora no estacionamento.
Fazer a conta considerando horas "quebradas" (minutos e segundos)
Exibir "Sr(a) NOME, sua conta ficou em R$X,XX" """

nome = str(input('Digite o seu nome: '))
horas = int(input('Digite quantas horas voce ficou no estacionamento: '))
minutos = int(input('Digite quantos minutos voce ficou no estacionamento: '))
segundos = int(input('Digite quantos segundos voce ficou no estacionamento: '))
valor = float(input('Digite o valor do estacionamento: '))
minutosemhoras = minutos / 60
segundosemhoras = (segundos / 60) / 60
total = (horas + minutosemhoras + segundosemhoras) * valor

print('Sr(a) {}, sua conta ficou em RS{:.2f}'.format(nome, total))
