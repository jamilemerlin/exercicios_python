from math import sin, cos, tan, radians

entrada = float(input('Digite o valor de um ângulo: '))
seno = sin(radians(entrada))
cos = cos(radians(entrada))
tan = tan(radians(entrada))
print(f'Para o ângulo {entrada:.2f} temos o seno {seno:.2f}, o cosseno {cos:.2f} e a tangente {tan:.2f}.')

