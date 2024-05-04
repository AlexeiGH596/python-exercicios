from math import sin, cos, tan, radians
ângulo = int(input('Me informe o ângulo: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(f'Seno: {seno}\nCosseno: {cosseno}\nTangente: {tangente}')
