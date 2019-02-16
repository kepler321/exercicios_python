"""Exercício 9:
Perguntar ao usuário qual seu salário bruto.
Depois perguntar quanto % vai para o INSS.
Depois % vai para o FGTS.
Depois quanto % vai para o IR. 
Perguntar ainda quanto ele ganha de VR.
Um dado: considere que no mês de férias o bruto é 30% a mais que nos demais meses e e dezembro, 90% a mais.
O salário líquido é o valor bruto menos INSS, menos FGTS, menos IR, mais VR.
Ao final, exiba "Seu salário líquido ordinário é R$X.".
Depois "No seu mês de férias, ganha líquido R$Y".
Depois "Em dezembro seu líquido é R$Z\" """

bruto = float(input('Qual é o seu salario bruto? R$: '))
INSS = float(input('Quanto em por cento vai para o INSS? R$: '))
FGTS = float(input('Quanto em por cento vai para o FGTS? R$: '))
IR = float(input('Quanto em por cento vai para o IR? R$: '))
VR = float(input('Quanto voce ganha de VR? R$: '))

# os cálculos das porcentagens podem ser feitas uma vez e salvas em variáveis, evitar repetições
# usar o padrão snake_case

brutoferias = bruto + (bruto * 0.3)
brutodezembro = bruto + (bruto * 0.9)
liquido = bruto - (bruto * ((INSS / 100) + (FGTS / 100) + (IR / 100))) + VR
liquidoferias = brutoferias - (brutoferias * ((INSS / 100) + (FGTS / 100) + (IR / 100))) + VR
liquidodezembro = brutodezembro - (brutodezembro * ((INSS / 100) + (FGTS / 100) + (IR / 100))) + VR
print('Seu salario liquido ordinario é R$ {:.2f}'.format(liquido))
print('No seu mes de ferias, voce ganha liquido R$ {:.2f}'.format(liquidoferias))
print('Em Dezembro seu liquido é R$ {:.2f}'.format(liquidodezembro))
