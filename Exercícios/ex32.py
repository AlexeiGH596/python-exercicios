from datetime import date
ano = int(input('Digite um ano (digite 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bixessto!')
else:
    print(f'{ano} não é um ano bixessto...')
