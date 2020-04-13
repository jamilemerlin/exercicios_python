totaltime = input("Por favor, entre com o número de segundos que deseja converter: ")
secondint = int(totaltime)
day = secondint // 86400
hour_remaining = secondint % 86400
hourint = hour_remaining // 3600
second_remaining = secondint % 3600
minute = second_remaining // 60
second_remaining_final = second_remaining % 60
print(
    day,
    "dias,",
    hourint,
    "horas,",
    minute,
    "minutos e",
    second_remaining_final,
    "segundos.",
)
