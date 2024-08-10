from random import randint
from time import sleep
print('|=|' * 20)
print('Vamos jogar um jogo de adivinhação?')
numero_1 = randint(1, 5)
numero_2 = int(input('Tente adivinhar em que número de 1-5 eu pensei!: '))
print('Analisando...')
sleep(2.5)
if numero_2 == numero_1:
    print(f'\033[32mParabéns, você ganhou! Pensamos no número {numero_1}\033[m')
else:
    print(f'\033[31mVocê perdeu... Pensei no número {numero_1}, não no {numero_2}\033[m')
print('|=|' * 20)
