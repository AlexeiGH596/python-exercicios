# Primeira e segunda análise
nome_completo = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome completo em letras maiúsculas: {nome_completo.upper()}. Em letras minúsculas,: {nome_completo.lower()}.')
# Terceira análise
tamanho = len(nome_completo) - nome_completo.count(' ')
print(f'Seu nome completo possui {tamanho} letras.')
# Quarta análise
nome_dividido = nome_completo.split()
primeiro_nome = nome_dividido[0]
primeiro_nome_tamanho = len(primeiro_nome)
print(f'E seu primeiro nome é {primeiro_nome}, e ele possui {primeiro_nome_tamanho} letras.')
