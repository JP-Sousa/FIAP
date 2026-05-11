"""▪ Faça um programa que realize a soma de duas matrizes, com mesmas dimensões.
 Seu programa deve ter 2 matrizes A e B de números inteiros.
  A terceira matriz deve ser a soma de A com B. ▪ Exemplo de soma:"""

import random

line_size = random.randint(1, 10)
column_size = random.randint(1, 10)

a = [[random.randint(1, 10) for _ in range(column_size)] for _ in range(line_size)]
b = [[random.randint(1, 10) for _ in range(column_size)] for _ in range(line_size)]
c = [[None for _ in range(column_size)] for _ in range(line_size)]

print(f"Tamanho da Matriz: {line_size}, Tamanho do Vetor: {column_size}")

for i in range(line_size):

    print()

    for j in range(column_size):
        c[i][j] = a[i][j] + b[i][j]
        print(f"{a[i][j]} + {b[i][j]} = {c[i][j]}", end=" | ")