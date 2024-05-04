a = float(input('Digite o comprimento da 1° reta: '))
b = float(input('Digite o comprimento da 2° reta: '))
c = float(input('Digite o comprimento da 3° reta: '))
if a < b + c and b < a + c and  c < a + b:
    print('\033[32mOs segmentos de retas fornecidos PODEM formar um triângulo.\033[m')
else:
    print('\033[31mOs segmentos de retas fornecido NÃO PODEM formar um triângulo.\033[m')
