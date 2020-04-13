import requests

try:
    requests.get("http://www.pudim.com.br")
except:
    print('\033[31mO site Pudim não está disponível no momento!\033[m')
else:
    print('\033[32mO site Pudim está disponível no momento!\033[m')