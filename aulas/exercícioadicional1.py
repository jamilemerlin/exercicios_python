client_name = input("Digite o nome do cliente: ")

due_day = input("Digite o dia do vencimento: ")

due_month = input("Digite o mês do vencimento: ")

value = input("Digite o valor da fatura: ")

print(
    "Olá,", client_name,
)
print(
    "A sua fatura com vencimento em",
    due_day,
    "de",
    due_month,
    "no valor de R$",
    value,
    "está fechada.",
)
