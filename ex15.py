dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('E quantos km você percorreu com ele? '))
print(f'Você alugou um carro por {dias} dias e percorreu {km}km com ele.')
preço_dias = dias * 60
preço_km = km * 0.15
valor_total = preço_dias + preço_km
print(f'O valor a ser pago pelos dias alugados é de R${preço_dias} e pela distância percorrida é de R${preço_km}')
print(f'Logo, o valor total a ser pago é de R${valor_total}')
print('Obs.: cada dia do aluguel custá 60R$, e por cada quilômetro percorrido custará 0,15R$.')
