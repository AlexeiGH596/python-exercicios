from random import choice
nome_1 = input('Digite seu nome: ')
nome_2 = input('Digite seu nome: ')
nome_3 = input('Digite seu nome: ')
nome_4 = input('Digite seu nome: ')
lista = [nome_1, nome_2, nome_3, nome_4]
print(f'O escolhido foi: {choice(lista)}')
