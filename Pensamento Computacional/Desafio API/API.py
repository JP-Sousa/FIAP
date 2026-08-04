endpoints = ["/login", "/produtos", "/pedidos"]

status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

"""Cada linha representa um endpoint e cada coluna, uma requisição."""

"""
1-indentificar um sucesso criar funcao
2-detectar 2 erros seguidos
3-analisar um endpoint
    conta sucesso
    calcula percentual
    verifica se tem erro
    classifica
    
4-percorre toda a matriz"""

def check(n):
    if 200 <= n < 300:
        return True
    else:
        return False

def criticalError(sts):
    for i in range(len(sts) - 1):
        if not check(sts[i]) and not check(sts[i+1]):
            return True
    return False

def sucess(sts):

    suc = 0

    for s in sts:
        if check(s):
            suc += 1

    return  suc

def mostError(status1):

    position = 0
    most = len(status1[position]) - sucess(status[position])

    for i in range(1, len(status1), 1):
        temp = len(status1[i]) - sucess(status[i])
        if temp > most:
            most = temp
            position = i

    return position

for i in range(len(endpoints)):
    print("\nendpoint: ", endpoints[i])

    temp = sucess(status[i])
    perc = temp / len(status[i]) * 100

    print("Sucess: ", temp)
    print("Error: ", len(status[i]) - temp)
    print(f"Percentage: {perc}%\t")
    if criticalError(status[i]):
        print("Critical")
    elif perc >= 80:
        print("Stable")
    else:
        print("unstable")

print("\nMost error endpoint: ", endpoints[mostError(status)])