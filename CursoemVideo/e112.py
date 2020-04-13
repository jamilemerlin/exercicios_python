from utilidadescev.moeda import moeda110
from utilidadescev.dado import dado


entrada = dado.leiadinheiro('Digite o preço: R$ ')
moeda110.resumo(entrada, 35, 20)

# exercício para receber float com vírgula e ser válido.