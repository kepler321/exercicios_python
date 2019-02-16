"""Exercício 10:
Solicite o valor da compra para o usuário
Depois, pergunte em quantas parcelas ele vai querer pagar

Se ele informar que é apenas 1, o valor a pagar terá um desconto de 5%.
Exiba o valor a pagar

Se o número de parcelas for maior que 1, calcule o valor da prestação e exiba:
"Você vai pagar x parcelas de Y",
onde X é o número de parcelar e Y o valor da prestação.

Caso o usuário informe um valor menos que 1, exiba "É mesmo, engraçadinho?" """

compra = float(input('Digite o valor da compra R$: '))
parcelas = int(input('Em quantas parcelas voce quer pagar?: '))

if parcelas < 1:
    print('É mesmo, engracadinho?')
elif parcelas == 1:
    compra = compra - (compra * 0.05)
    print('O valor a pagar é de R${:.2f} !'.format(compra))
else:
    print('Voce vai pagar {} parcelas de R${:.2f} !'.format(parcelas, compra / parcelas))
