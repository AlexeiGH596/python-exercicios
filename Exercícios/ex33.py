a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))
c = int(input('Agora, o último: '))
#Verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
#Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if maior == menor:
    print('\033[7mOs números fornecidos possuem o mesmo valor.\033[m')
else:
    print(f'\033[34mO maior número é o {maior}\033[m')
    print(f'\033[33mO menor número é o {menor}\033[m')
