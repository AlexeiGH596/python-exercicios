nome_completo = str(input('Digite seu nome completo: ')).strip()
print(f'Olá, {nome_completo}!')
dividido = nome_completo.split()
print(f'Seu primeiro nome é {dividido[0]} e seu último nome é {dividido[-1]}.')
