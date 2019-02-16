""""Exercicio 12:
Crie um programa de cálculo do FGTS e INSS de empregados em regime CLT.
A partir de seu salário bruto, calcule e exiba esses valores conforme essas tabelas:
INSS: http://www.calculador.com.br/tabela/trabalhista/tabelas-vigentes
FGTS: http://www.calculoexato.net/calculos-trabalhistas/como-calcular-fgts/"""


salario = float(input('Digite o seu salario bruto R$ '))
fgts = salario * 0.08
inss = 0

if salario > 1903.98 and salario <= 2826.65:
    inss = salario * 0.075
    print('Com o seu salario atual de R${:.2f} voce paga R${:.2f} de INSS por mes e voce ganha R${:.2f} por mes de FGTS'.format(salario, inss, fgts))
elif salario > 2826.65 and salario <= 3751.05:
    inss = salario * 0.15
    print('Com o seu salario atual de R${:.2f} voce paga R${:.2f} de INSS por mes e voce ganha R${:.2f} por mes de FGTS'.format(salario, inss, fgts))
elif salario > 3751.05 and salario <= 4664.68:
    inss = salario * 0.225
    print('Com o seu salario atual de R${:.2f} voce paga R${:2f} de INSS por mes e voce ganha R${:.2f} por mes de FGTS'.format(salario, inss, fgts))
elif salario <= 0:
    print('Nao é possivel voce nao ganhar nada!')
elif salario > 4664.68:
    inss = salario * 0.275
    print('Com o seu salario atual de R${:.2f} voce paga R${:2f} de INSS por mes e voce ganha R${:.2f} por mes de FGTS'.format(salario, inss, fgts))
else:
    print('Com o seu salario atual de R${:.2f} voce paga R${:.2f} de INSS por mes e voce ganha R${:.2f} por mes de FGTS'.format(salario, inss, fgts))