"""Escreva um algoritmo que recebe um inteiro positivo n
e imprime todos os divisores positivos de n.
▪ Utilize o laço for."""

n = int(input("Digite um numero inteiro positivo: "))

for i in range(1, n, 1):
    if n % i == 0:
        print(f"{i} é divisor de {n}")