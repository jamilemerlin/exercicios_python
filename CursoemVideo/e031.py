distancia = float(input('Digite a distância da viagem: '))
if distancia <= 200:
    calc = distancia * 0.50
    print(f'Sua viagem vai custar R${calc:.2f}')
else:
    cal = distancia * 0.45
    print(f'Sua viagem vai custar R${cal:.2f}')

