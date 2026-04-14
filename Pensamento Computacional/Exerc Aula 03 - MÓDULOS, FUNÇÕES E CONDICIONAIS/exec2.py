#Faça um programa que leia um número, e informe se ele é par ou impar

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O {num} é par")
else:
    print(f"O {num} é impar")

