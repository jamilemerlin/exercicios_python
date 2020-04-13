import math

x1 = int(input("Digite a coordenada X do primeiro plano: "))
y1 = int(input("Digite a coordenada Y do primeiro plano: "))
x2 = int(input("Digite a coordenada X do segundo plano: "))
y2 = int(input("Digite a coordenada Y do segunda plano: "))

# Distancia entre dois pontos cartesianos
distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

# Distancia LIMITE para ser considerado longe
max_distance = 10

if distancia >= max_distance:
    print("Longe")
else:
    print("Perto")

