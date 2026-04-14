"""▪ Determine e mostre todos os números primos no intervalo de 2 a 2000.
Dicas:
▪ Para resolver esse problema, primeiro faça um algoritmo que verifica se um número inteiro qualquer é
primo ou não.
▪ A seguir, com esse código em mãos, faça os ajustes necessários para mostrar todos os números primos
no intervalo solicitado.
▪ Você precisará colocar uma estrutura de repetição dentro da outra.
▪ Laços aninhados!!!! """
from sympy import false

def even(num):
    if num % 2 == 0:
        return True
    return False

def prime(num):

    if num == 2:
        return True

    if even(num):
        return False

    div = 0

    for i in range(1, num+1, 1):
        if num % i == 0:
           div += 1

    if div == 2:
        return True

    return False

for i in range(2001):

    if prime(i):
        print(f"{i},", end=" ")

    if i % 100 == 0:
        print()