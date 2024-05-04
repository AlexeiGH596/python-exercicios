nome_completo = str(input('Digite seu nome completo: ')).strip()
titulo = nome_completo.title()
print(f'Seu nome possui "Silva"?\n{'Silva' in titulo}')
