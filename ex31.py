distancia = int(input('Qual a distância da viagem? km/h: '))
if distancia > 200:
    print(f'A passagem custará R${0.45 * distancia}. Aproveite a promoção!')
else:
    print(f'A passagem custará R${0.50 * distancia}')
