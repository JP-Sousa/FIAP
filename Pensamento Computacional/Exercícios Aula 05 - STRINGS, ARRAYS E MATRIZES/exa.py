"""▪ Dado um conjunto de nomes de quatro pessoas,
 escreva um algoritmo que imprima todas as possíveis duplas que podem ser formadas.
  ▪ Primeiro, crie um vetor e coloque quatro nomes nele. ▪ A seguir, exiba as possíveis duplas."""
from sqlalchemy.testing.plugin.pytestplugin import pytest_runtest_teardown

name = ["Max", "Bob", "Carlos", "Ana"]

for i in range(0, len(name), 1):
    for j in range(len(name)-1, i, -1):
        print(f"Dupla = {name[i]} x {name[j]}")