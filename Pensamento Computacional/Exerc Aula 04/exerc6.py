"""Faça um programa capaz de exibir todos os valores pares entre 2
e um valor fornecido pelo usuário"""

def even(num):
    if num % 2 == 0:
        return True
    return False

n = int(input("Digite um numero inteiro positivo: "))

for i in range(2, n+1, 2):
    #if even(i):
    print(f"{i}", end=" ")  