"""Faça um programa que leia 3 valores que representam os lados de um triângulo A, B e C e ordene-os
em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
tipo de triângulo que estes três lados formam, com base nos seguintes casos:
▪ Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
▪ Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
▪ Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;"""

a = int(input("Digite o Valor do lado A: "))
b = int(input("Digite o Valor do lado B: "))
c = int(input("Digite o Valor do lado C: "))

maior = a

if b > maior:
    maior = b
    if c > maior:
        maior = c
        meio = b
        menor = a
    else:
        if c > a:
            meio = c
            menor = a
        else:
            meio = a
            menor = c
else:
    if c > maior:
        maior = c
        meio = a
        menor = b
    else:
        if c > b:
            meio = c
            menor = b
        else:
            meio = b
            menor = c

a = maior
b = meio
c = menor

"""
▪ Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
▪ Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
▪ Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;"""


if a >= (b+c):
    print("Não forma triângulo")

if a**2 == (b**2 + c**2):
    print("Triângulo Retângulo")

if a**2 > (b**2 + c**2):
    print("Triângulo Obtusangulo")

if a**2 < (b**2 + c**2):
    print("Triângulo Acutângulo")

if a == b and b == c:
    print("Triângulo Equilâtero")

if (a == b and a == c and b != c) or (b == a and b == c and a != c) or (c == a and c == b and a != b):
    print("Triângulo Isosceles")