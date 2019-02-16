"""Exercício 14:
Crie um programa de um mini boletim.
a) Solicite o nome da disciplina. Se nada for digitado, encerre o programa.
	Se qualquer coisa for digitada, prossiga para b)
b) Solicite o valor das notas 1, 2, e 3. Calcule então o "1º sub total", que é a média entre elas vezes 0,40.
	Se o subtotal for menor que 2,00, exiba "Deu muito ruim" e encerre o programa.
	Caso contrário, prossiga para c)
c) Solicite o valor das notas 4 e 5. Calcule então o "2º sub total", que é a média entre elas vezes 0,60.
	Se o subtotal for menor que 3,00, exiba "Deu ruim" e encerre o programa.
	Caso contrário, prossiga para d)
d) Calcule a nota final, que é a soma dos 2 sub totais, exibindo:
"Na disciplina X, seu resultado foi", mais...
Total <5 "Reprovou"
Total >=5 e <7 "Na média"
Total >=7 e <9 "Acima da média"
Total >=9 "Excelente média"""


def total(disciplina, totalsubtotal):
    if totalsubtotal < 5:
        print('Na disciplina {} voce Reprovou'.format(disciplina))
    if totalsubtotal >= 5 and totalsubtotal < 7:
        print('Na disciplina {} voce esta na média'.format(disciplina))
    if totalsubtotal >= 7 and totalsubtotal < 9:
        print('Na disciplina {} voce esta acima da media!'.format(disciplina))
    if totalsubtotal >= 9:
        print('Na disciplina {} voce tem uma excelente média'.format(disciplina))


# mode mudar a clausula if, para não precisar do else
# não foi necessário os exit()
# no if e else deve-se tomar cuidado para ficar encadeado

disciplina = str(input('Digite o nome da disciplina: '))
if disciplina == '':
    exit()
else:
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    nota3 = float(input('Terceira nota: '))
    subtotal1 = ((nota1 + nota2 + nota3) / 3) * 0.40

    if subtotal1 < 2.00:
        print('Deu muito ruin!')
        exit()
    else:
        nota4 = float(input('Quarta nota: '))
        nota5 = float(input('Quinta nota: '))
        nota6 = float(input('Sexta nota: '))  # não precisa desta
        subtotal2 = ((nota4 + nota5 + nota6) / 3) * 0.60  # divisão por 2

        if subtotal2 < 3.00:
            print('Deu ruin!')
            exit()
        else:
            totalsubtotal = subtotal1 + subtotal2
            total(disciplina, totalsubtotal)
