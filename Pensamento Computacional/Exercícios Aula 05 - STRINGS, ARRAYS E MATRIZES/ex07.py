"""▪ Crie um programa com uma matriz 3x4 ▪ 3 linhas ▪ 4 colunas
 ▪ Atribua valores aleatórios à todas posições da matriz.
  ▪ Exiba essa matriz."""
import random

num = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]

for _ in range(len(num)):
    print(num[_])