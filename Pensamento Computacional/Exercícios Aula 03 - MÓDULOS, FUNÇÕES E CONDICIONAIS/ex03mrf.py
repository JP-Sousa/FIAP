#Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Números iguais")