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
3-analisat um endpoint
    conta sucesso
    calcula percentual
    verifica se tem erro
    classifica
    
4-percorre toda a matriz"""