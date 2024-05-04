cidade = str(input('Digite o nome de uma cidade: ')).strip()
santo = cidade[0:5].capitalize()
print(f'O nome da cidade fornecida começa com "Santo"?\n{santo == 'Santo'}')
