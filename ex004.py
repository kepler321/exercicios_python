
"""
Exercício 4:
Solicite nome, idade, peso e salario atual de uma pessoa.
Calcule quanto a pessoa ganha por peso de acordo com a idade atual.
Ao final mostre: "O Sr. X vale R$ Y por kilograma"
-------------------------------
"""

nome = str(input('Digite seu nome: '))
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
salario = float(input('Digite seu salario atual: '))

valor_final = (salario / peso) * idade
print("O Sr. {} vale R$ {:.2f} por kilograma".format(nome, valor_final))
