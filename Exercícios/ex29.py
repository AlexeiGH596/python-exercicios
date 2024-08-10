velocidade = int(input('Qual é a velocidade atual do carro? km/h: '))
if velocidade > 80:
    print(f'{velocidade}km/h ultrapassa nosso limite. Você deverá pagar um multa de R${(velocidade - 80) * 7}')
else:
    print(f'{velocidade}km/h está entre os conformes. Continue assim!')
