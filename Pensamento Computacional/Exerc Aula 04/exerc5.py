"""Faça um programa que receba 5 valores digitados pelo usuário
 e, ao final, informe qual é o maior
deles."""

i = 0
maior = 0

while i < 5:
    n = int(input("Digite um numero: "))
    if n > maior:
        maior = n
    i += 1

print("Maior:", maior)