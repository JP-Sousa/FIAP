"""Escreva um programa que dado um inteiro n positivo calcula
e imprime a soma de todos os números
inteiros entre 1 e n.
▪ Valide a entrada do usuário, só aceite números positivos!!"""

n = int(input("Digite um numero inteiro positivo: "))

while n < 0:
    n = int(input("Numero negativo, por favor insira outro número: "))

soma = 0

for i in range(n+1):
    soma += i

print(soma)