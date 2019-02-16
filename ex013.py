"""Exercício 13:
Crie um programa que calcula o líquido que um empregado no regime PJ ganha.
Solicite ao usuário:
seu ganho bruto
mensalidade do contador
TFE anual
Calcule o líquido conforme a seguinte fórmula:
Liquido = Bruto - Contador - TFE mensal - Imposto (sempre 6% sobre o Bruto)"""



ganho_bruto = float(input('Digite seu ganho bruto :R$'))
mensalidade_do_contador = float(input('Digite a mensalidade do contador: R$'))
tfe_anual = float(input('Digite o seu tfe anual'))
ganho_liquido = (ganho_bruto - mensalidade_do_contador - (tfe_anual / 12) - (ganho_bruto * 0.06))
print('O seu ganho liquido é de R${:.2f}'.format(ganho_liquido))

