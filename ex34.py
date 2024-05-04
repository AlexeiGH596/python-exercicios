salario = float(input('Qual o salário atual? R$: '))
if salario <= 1250:
    salario = salario + salario*15/100
else:
    salario = salario + salario*10/100
print(f'Seu novo salário com o aumento será de R${salario} ')
