# Faça um programa que receba 5 valores digitados pelo usuário
# e, ao final, informe qual é a soma deles"""

i = 0
soma = 0

while i < 5:
    n = int(input("Digite um numero: "))
    soma += n
    i += 1

print("Soma:",soma)