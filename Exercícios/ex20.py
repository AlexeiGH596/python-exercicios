from random import sample
nome_1 = str(input('Digite seu nome: '))
nome_2 = str(input('Digite seu nome: '))
nome_3 = str(input('Digite seu nome: '))
nome_4 = str(input('Digite seu nome: '))
lista = [nome_1, nome_2, nome_3, nome_4]
print(f'A ordem escolhida foi:\n{sample(lista, k=4)}')
